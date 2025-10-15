from mcpacker.format.report.composer import ReportComposer
from mcpacker.model.core.geology.deposit.mineraldeposit import MineralDeposit
from mcpacker.model.modpack import ModPack
from pathlib import Path


# Class ############################################################################################

class DepositReport(ReportComposer):

    def doCompose(self):
        biomes = self.pack.world.biomes

        for deposit in self.pack.world.deposits:
            self.line(f"Deposit: {deposit.name}")
            self.line()
            self.indent()
            self.text("altitude: ").line(deposit.altitude)
            self.text("biome filters: ").line(", ".join(str(b) for b in deposit.biomeFilters))
            self.text("scarcity: ").line(deposit.scarcity)
            if isinstance(deposit, MineralDeposit):
                self.text("bulk: ").line(deposit.bulk)
                self.text("inclusions: ").line(", ".join(str(i) for i in deposit.inclusions))
                self.text("proportion: ").line(deposit.proportion)

            self.line()
            self.line("Found in:")
            self.indent()

            biomeCount = 0
            for biome in biomes.filter(lambda b: deposit.acceptsBiome(b)):
                self.line(biome)
                biomeCount += 1

            if biomeCount == 0:
                self.line("WARNING: no suitable biomes")

            self.outdent()

            self.outdent()
            self.line()
