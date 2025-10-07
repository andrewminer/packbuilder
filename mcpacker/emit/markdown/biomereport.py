from mcpacker.emit.markdown.report import Report
from mcpacker.model.core.world import World


# Class ############################################################################################

class BiomeReport(Report):

    def __init__(self, world:World):
        super().__init__("biomes.md", world)

    def build(self):
        for biome in self.world.biomes.all():
            self.line(f"# Biome: {biome.city} <{biome.gameId}>")
            self.line()

            self.indent()
            for trait in biome.traits():
                self.text("* ").line(trait)
            self.outdent()

            self.line()
