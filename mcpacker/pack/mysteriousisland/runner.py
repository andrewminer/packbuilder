from mcpacker.emit.markdown.biomereport import BiomeReport
from mcpacker.emit.markdown.mineralreport import MineralReport
from mcpacker.emit.markdown.mobreport import MobReport
from mcpacker.emit.markdown.reportwriter import ReportWriter
from mcpacker.pack.mysteriousisland.world import WORLD
from mcpacker.ui.runner import Runner as BaseRunner

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
    Runner(WORLD).run(sys.argv)
