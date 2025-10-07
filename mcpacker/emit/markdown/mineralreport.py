from mcpacker.emit.markdown.report import Report
from mcpacker.model.core.world import World


# Class ############################################################################################

class MineralReport(Report):

    def __init__(self, world:World):
        super().__init__("minerals.md", world)

    def build(self):
        for mineral in self.world.minerals.all():
            self.line(f"# Mineral: {mineral.name}")
            self.line()

            self.indent()
            for replacement in mineral.replacements:
                self.text("* ").line(str(replacement))
            self.outdent()

            self.line()
