from mcpacker.emit.markdown.report import Report
from mcpacker.model.modpack        import ModPack


# Class ############################################################################################

class MineralReport(Report):

    def __init__(self, pack:ModPack):
        super().__init__("minerals.md", pack)

    def build(self):
        for mineral in self.pack.world.minerals:
            self.line(f"# Mineral: {mineral.name}")
            self.line()

            self.indent()
            for replacement in mineral.replacements:
                self.text("* ").line(str(replacement))
            self.outdent()

            self.line()
