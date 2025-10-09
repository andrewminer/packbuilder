from mcpacker.emit.markdown.reportwriter import ReportWriter
from mcpacker.emit.markdown.biomereport import BiomeReport
from mcpacker.emit.markdown.mineralreport import MineralReport
from mcpacker.emit.markdown.mobreport import MobReport
from mcpacker.model.modpack import ModPack

import inspect
import os
import sys


# Constants ########################################################################################

OUTPUT_PATH = "output"


# Class ############################################################################################

class Runner:

    def __init__(self, pack:ModPack|None=None):
        self.pack = pack or ModPack("untitled")

    def abort(self, message:str, status:int=-1):
        print(message)
        sys.exit(status)

    def run(self, argv:list[str]):
        if len(sys.argv) < 2:
            self.abort("Please provide a command name")

        commandName = "_command_" + argv[1]
        for name, doCommand in inspect.getmembers(self):
            if name == commandName:
                doCommand(*argv[2:])
                sys.exit(0)

        self.abort("No command named: " + argv[1])

    # Commands #################################################################

    def _command_writeReports(self):
        writer = ReportWriter([
            BiomeReport(self.pack),
            MineralReport(self.pack),
            MobReport(self.pack),
        ])
        writer.write(os.path.join(OUTPUT_PATH, self.pack.name, "markdown"))
