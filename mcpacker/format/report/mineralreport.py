from mcpacker.format.report.composer import ReportComposer
from mcpacker.model.ecology.biome import Biome
from mcpacker.model.geology.mineral import Mineral
from mcpacker.model.modpack import ModPack
from pathlib import Path


# Class ############################################################################################

class MineralReport(ReportComposer):

    def doCompose(self):
        for mineral in self.pack.world.minerals:
            self.line(f"Mineral: {mineral.name}").line().indent()

            self.line("Replacements:").line().indent()
            for replacement in mineral.replacements:
                self.line(str(replacement))
            self.outdent().line() # replacements

            self.line("Spawns:").line().indent()
            for spawn in self.pack.world.mineralSpawns:
                if spawn.mineral != mineral: continue

                self.text(spawn.name).line(":").line().indent()
                self.text("altitude: ").line(spawn.habitat.altitude)
                self.text("biomeFilters: ")
                self.line(" -or- ".join(str(f) for f in spawn.habitat.biomeFilters))
                self.text("bulk: ").line(spawn.ecotype.bulk)
                self.text("scarcity: ").line(spawn.ecotype.scarcity)
                self.outdent().line() # spawn.name
            self.outdent() # spawns

            self.line("Biomes:").line().indent()
            for biome in self._collateBiomes(mineral):
                self.line(str(biome))
            self.outdent().line() # biomes

            self.outdent() # mineral

    def _collateBiomes(self, mineral:Mineral) -> list[Biome]:
        result:set[Biome] = set()
        spawns = [s for s in self.pack.world.mineralSpawns if s.mineral == mineral]
        for biome in self.pack.world.biomes:
            for spawn in spawns:
                if not spawn.habitat.accepts(biome): continue
                result.add(biome)

        return sorted(result)
