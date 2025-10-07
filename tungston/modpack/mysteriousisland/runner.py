from tungston.interface.runner import Runner as BaseRunner
from tungston.core.world import World
from tungston.modpack.mysteriousisland.biomecatalog import CATALOG as biomes
from tungston.modpack.mysteriousisland.depositcatalog import CATALOG as deposits
from tungston.modpack.mysteriousisland.mineralcatalog import CATALOG as minerals
from tungston.modpack.mysteriousisland.mobcatalog import CATALOG as mobs
from tungston.generator.markdown.reportwriter import ReportWriter
from tungston.generator.markdown.biomereport import BiomeReport
from tungston.generator.markdown.mineralreport import MineralReport
from tungston.generator.markdown.mobreport import MobReport

import sys


# Constants ########################################################################################

REPORT_PATH = "./output/markdown/mysteriousisland"


# Class ############################################################################################

class Runner(BaseRunner):

    def _command_writeReports(self):
        writer = ReportWriter([
            BiomeReport(self.world),
            MineralReport(self.world),
            MobReport(self.world),
        ])
        writer.write(REPORT_PATH)



# Script ###########################################################################################

if __name__ == "__main__":
    Runner(World(biomes, deposits, minerals, mobs)).run(sys.argv)
