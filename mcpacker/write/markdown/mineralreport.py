from mcpacker.write.markdown.markdownwriter import MarkdownWriter
from mcpacker.model.modpack                 import ModPack
from pathlib                                import Path


# Class ############################################################################################

class MineralReport(MarkdownWriter):

    def __init__(self, pack:ModPack, outputDir:Path):
        super().__init__("minerals.md", pack, outputDir)

    def compose(self):
        for mineral in self.pack.world.minerals:
            self.line(f"# Mineral: {mineral.name}")
            self.line()

            self.indent()
            for replacement in mineral.replacements:
                self.text("* ").line(str(replacement))
            self.outdent()

            self.line()
