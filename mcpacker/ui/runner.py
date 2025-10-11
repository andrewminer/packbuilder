from mcpacker.model.modpack                 import ModPack
from mcpacker.write.incontrol.spawnerwriter import SpawnerWriter
from mcpacker.write.markdown.biomereport    import BiomeReport
from mcpacker.write.markdown.mineralreport  import MineralReport
from mcpacker.write.markdown.mobspawnreport import MobSpawnReport
from mcpacker.write.markdown.reportwriter   import ReportWriter
from mcpacker.write.compositewriter         import CompositeWriter
from mcpacker.write.staticwriter            import StaticWriter
from pathlib                                import Path

import inspect
import os
import sys


# Constants ########################################################################################

OUTPUT_PATH = Path("output")


# Class ############################################################################################

class Runner:

    def __init__(self, pack:ModPack|None=None, outputDir:Path=OUTPUT_PATH):
        self.pack = pack or ModPack("untitled")
        self.outputDir = outputDir

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
        CompositeWriter(self.pack, self.outputDir, [
            BiomeReport,
            MineralReport,
            MobSpawnReport,
        ]).write()

    def _command_writeModPack(self):
        CompositeWriter(self.pack, self.outputDir, [
            StaticWriter,
            SpawnerWriter,
        ]).write()
