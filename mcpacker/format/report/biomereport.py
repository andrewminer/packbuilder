from mcpacker.model.modpack import ModPack
from mcpacker.model.ecology.biome import Biome
from mcpacker.format.report.composer import ReportComposer
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
        depositCount = 0
        for deposit in self.pack.world.deposits:
            if not deposit.acceptsBiome(biome): continue
            self.line(f"{deposit.name} ({deposit.scarcity})")
            depositCount += 1

        if depositCount == 0:
            self.line("<no deposits>")
        self.outdent() # deposits

    def _composeFaunaSection(self, biome:Biome):
        self.line().line("Fauna:").indent()
        faunaLineCount = 0

        for mob in self.pack.world.mobs:
            altitude = None
            for spawn in self.pack.world.mobSpawns:
                if not spawn.habitat.accepts(biome): continue
                if spawn.ecotype.location == LO.CAVE: continue

                altitude = AL.span(altitude or spawn.habitat.altitude, spawn.habitat.altitude)

            if altitude != None:
                self.line(f"{mob.name} @ {altitude}")
                faunaLineCount += 1

        if faunaLineCount == 0:
            self.line("<no fauna>")

        self.outdent() # fauna

    def _composeFloraSection(self, biome:Biome):
        self.line().line("Flora:").indent()
        floraLineCount = 0
        for spawn in self.pack.world.plantSpawns:
            if not spawn.habitat.accepts(biome): continue
            self.line(f"{spawn.plant.name} @ {spawn.habitat.altitude}")
            floraLineCount += 1

        if floraLineCount == 0:
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
