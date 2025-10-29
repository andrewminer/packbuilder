from mcpacker.format.report.composer import ReportComposer
from mcpacker.model.altitude import Altitude
from mcpacker.model.ecology.biome import Biome
from mcpacker.model.fauna.mob import Mob
from mcpacker.model.flora.plant import Plant
from mcpacker.model.geology.mineralspawn import MineralSpawn
from mcpacker.model.modpack import ModPack
from pathlib import Path

import mcpacker.model.altitude as AL
import mcpacker.model.fauna.location as LO


# Class ############################################################################################

class BiomeReport(ReportComposer):

    def doCompose(self):
        for biome in self.pack.world.biomes:
            self.line(f"Biome: {biome.gameId} ({biome.name})")
            self.indent() # biome

            self._composeTraitsLine(biome)
            self._composeGeologySection(biome)
            self._composeFloraSection(biome)
            self._composeFaunaSection(biome)

            self.outdent() # biome
            self.line()

    def _composeGeologySection(self, biome:Biome):
        self.line().line("Geology:").indent()
        mineralCount = 0
        for spawn in self.pack.world.mineralSpawns:
            if "plutonic" in spawn.name: continue

            if not spawn.habitat.accepts(biome): continue
            self.line(f"{spawn.name} ({spawn.ecotype.scarcity})")
            mineralCount += 1

        if mineralCount == 0:
            self.line("<no minerals>")
        self.outdent() # minerals

    def _composeFaunaSection(self, biome:Biome):
        self.line().line("Fauna:").indent()
        faunaLines:list[tuple[Mob, Altitude]] = []

        for mob in self.pack.world.mobs:
            altitude = None
            for spawn in self.pack.world.mobSpawns:
                if spawn.mob != mob: continue
                if not spawn.habitat.accepts(biome): continue
                if spawn.ecotype.location == LO.CAVE: continue

                altitude = AL.span(altitude or spawn.habitat.altitude, spawn.habitat.altitude)

            if altitude != None:
                faunaLines.append((mob, altitude))

        for line in sorted(faunaLines, reverse=True, key=lambda p: (p[1].bottom, p[1].top)):
            self.line(f"{line[0]} @ {line[1]}")

        if len(faunaLines) == 0:
            self.line("<no fauna>")

        self.outdent() # fauna

    def _composeFloraSection(self, biome:Biome):
        self.line().line("Flora:").indent()
        floraLines:list[tuple[Plant, Altitude]] = []
        for spawn in self.pack.world.plantSpawns:
            if not spawn.habitat.accepts(biome): continue
            floraLines.append((spawn.plant, spawn.habitat.altitude))

        for line in sorted(floraLines, reverse=True, key=lambda p: (p[1].bottom, p[1].top)):
            self.line(f"{line[0]} @ {line[1]}")

        if len(floraLines) == 0:
            self.line("<no flora>")

        self.outdent() # flora

    def _composeTraitsLine(self, biome:Biome):
        needsDelimiter = False
        self.line().text("Traits: ")
        for trait in biome.traits():
            if needsDelimiter: self.text(", ")
            needsDelimiter = True
            self.text(trait)
        self.line()
