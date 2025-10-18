from mcpacker.model.modpack import ModPack
from mcpacker.format.report.composer import ReportComposer
from pathlib import Path


# Class ############################################################################################

class BiomeReport(ReportComposer):

    def doCompose(self):
        for biome in self.pack.world.biomes:
            self.line(f"Biome: {biome.gameId} ({biome.name})")
            self.line()

            self.indent()
            needsDelimiter = False
            self.text("Traits: ")
            for trait in biome.traits():
                if needsDelimiter: self.text(", ")
                needsDelimiter = True
                self.text(trait)
            self.line()

            self.line()
            self.line("Deposits:")
            self.indent()
            depositCount = 0
            for deposit in self.pack.world.deposits:
                if not deposit.acceptsBiome(biome): continue
                self.line(deposit.name)
                depositCount += 1

            if depositCount == 0:
                self.line("<no deposits>")
            self.outdent()

            self.outdent()
            self.line()
