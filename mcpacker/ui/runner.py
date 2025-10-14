from mcpacker.format.report.biomereport import BiomeReport
from mcpacker.format.report.mineralreport import MineralReport
from mcpacker.format.report.mobspawnreport import MobSpawnReport
from mcpacker.model.modpack import ModPack
from mcpacker.write.compositewriter import CompositeWriter
from mcpacker.write.datapack.metawriter import MetaWriter
from mcpacker.write.datapack.writer import DataPackWriter
from mcpacker.write.incontrol.spawnerwriter import SpawnerWriter
from mcpacker.write.report.writer import ReportWriter
from mcpacker.write.staticwriter import StaticWriter
from pathlib import Path

import inspect
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
            ReportWriter(self.pack, BiomeReport, self.outputDir, "biomes.md"),
            ReportWriter(self.pack, MineralReport, self.outputDir, "minerals.md"),
            ReportWriter(self.pack, MobSpawnReport, self.outputDir, "mobspawns.md"),
        ]).write()

    def _command_writeModPack(self):
        CompositeWriter(self.pack, self.outputDir, [
            StaticWriter(self.pack, self.outputDir),
            SpawnerWriter(self.pack, self.outputDir),
            DataPackWriter(self.pack, self.outputDir, [
                MetaWriter(self.pack, self.outputDir),
            ]),
        ]).write()
