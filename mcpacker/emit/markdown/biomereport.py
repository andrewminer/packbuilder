from mcpacker.emit.markdown.report import Report
from mcpacker.model.modpack import ModPack


# Class ############################################################################################

class BiomeReport(Report):

    def __init__(self, pack:ModPack):
        super().__init__("biomes.md", pack)

    def build(self):
        for biome in self.pack.world.biomes:
            self.line(f"# Biome: {biome.gameId} ({biome.city})")
            self.line()

            self.indent()
            for trait in biome.traits():
                self.text("* ").line(trait)
            self.outdent()

            self.line()
