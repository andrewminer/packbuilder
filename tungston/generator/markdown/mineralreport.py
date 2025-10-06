from tungston.core.world import World
from tungston.generator.markdown.report import Report


# Class ############################################################################################

class MineralReport(Report):

    def build(self):
        for mineral in self.world.minerals.all():
            self.line(f"# Mineral: {mineral.name}")
            self.line()

            self.indent()
            for replacement in mineral.replacements:
                self.line(str(replacement))
            self.outdent()

            self.line()
