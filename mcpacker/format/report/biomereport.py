from mcpacker.model.modpack import ModPack
from mcpacker.format.report.composer import ReportComposer
from pathlib import Path


# Class ############################################################################################

class BiomeReport(ReportComposer):

    def doCompose(self):
        for biome in self.pack.world.biomes:
            self.line(f"# Biome: {biome.gameId} ({biome.city})")
            self.line()

            self.indent()
            for trait in biome.traits():
                self.text("* ").line(trait)
            self.outdent()

            self.line()
