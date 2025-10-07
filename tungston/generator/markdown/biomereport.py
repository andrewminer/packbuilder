from tungston.core.world import World
from tungston.generator.markdown.report import Report


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
