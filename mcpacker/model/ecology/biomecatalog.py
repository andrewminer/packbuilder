from collections.abc import Iterable
from mcpacker.model.catalog import Catalog
from mcpacker.model.ecology.biome import Biome
from mcpacker.model.ecology.biomefilter import BiomeFilter
from typing import Iterator


# Classes ##########################################################################################

class BiomeCatalog(Catalog[Biome]):

    def find(self, biomeFilters:Iterable[BiomeFilter]) -> Iterator[Biome]:
        for biome in self:
            accepted = True
            for biomeFilter in biomeFilters:
                if not biomeFilter.accepts(biome):
                    accepted = False
                    break

            if accepted:
                yield biome
