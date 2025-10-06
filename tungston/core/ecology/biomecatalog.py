from tungston.core.ecology.biome import Biome
from tungston.core.ecology.biomefilter import BiomeFilter


# Classes ##########################################################################################

class BiomeCatalog:
    """
    A comprehensive list of all available biomes in the modpack.
    """

    def __init__(self, biomes):
        self.biomes = sorted(biomes, key=lambda b: b.city)

    def all(self) -> list[Biome]:
        return list(self.biomes)

    def matching(self, biomeFilter:BiomeFilter) -> list[Biome]:
        result = []

        for biome in self.biomes:
            if biomeFilter.accepts(biome):
                result.append(biome)

        return result
