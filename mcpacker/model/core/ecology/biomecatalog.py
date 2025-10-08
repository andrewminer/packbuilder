from collections.abc import Iterable
from mcpacker.model.core.ecology.biome import Biome
from mcpacker.model.core.ecology.biomefilter import BiomeFilter


# Classes ##########################################################################################

class BiomeCatalog:
    """
    A comprehensive list of all available biomes in the modpack.
    """

    def __init__(self, biomes:Iterable[Biome]|None=None):
        self._biomes = {}

        for biome in (biomes or []):
            self.add(biome)

    def add(self, biome:Biome) -> "BiomeCatalog":
        if biome.gameId in self._biomes:
            raise Exception(f"Catalog already contains {biome.gameId}")

        self._biomes[biome.gameId] = biome

    def all(self) -> Iterable[Biome]:
        for gameId in sorted([b.gameId for b in self._biomes.values()]):
            yield self._biomes[gameId]

    def matching(self, biomeFilter:BiomeFilter) -> Iterable[Biome]:
        for biome in self.all():
            if biomeFilter.accepts(biome):
                yield biome
