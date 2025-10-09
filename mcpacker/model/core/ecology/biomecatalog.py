from mcpacker.model.catalog                  import Catalog
from mcpacker.model.core.ecology.biome       import Biome
from mcpacker.model.core.ecology.biomefilter import BiomeFilter
from typing                                  import Iterator


# Classes ##########################################################################################

class BiomeCatalog(Catalog[Biome]):

    def matching(self, biomeFilter:BiomeFilter) -> Iterator[Biome]:
        for biome in self:
            if biomeFilter.accepts(biome):
                yield biome
