from mcpacker.write.markdown.markdownwriter import MarkdownWriter
from mcpacker.model.modpack                 import ModPack
from pathlib                                import Path


# Class ############################################################################################

class BiomeReport(MarkdownWriter):

    def __init__(self, pack:ModPack, outputDir:Path):
        super().__init__("biomes.md", pack, outputDir)

    def compose(self):
        for biome in self.pack.world.biomes:
            self.line(f"# Biome: {biome.gameId} ({biome.city})")
            self.line()

            self.indent()
            for trait in biome.traits():
                self.text("* ").line(trait)
            self.outdent()

            self.line()
