from mcpacker.format.report.composer import ReportComposer
from mcpacker.model.modpack import ModPack
from pathlib import Path


# Class ############################################################################################

class MineralReport(ReportComposer):

    def doCompose(self):
        for mineral in self.pack.world.minerals:
            self.line(f"# Mineral: {mineral.name}")
            self.line()

            self.indent()
            for replacement in mineral.replacements:
                self.text("* ").line(str(replacement))
            self.outdent()

            self.line()
