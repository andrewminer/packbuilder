from collections.abc import Iterable
from mcpacker.model.core.altitude import Altitude
from mcpacker.model.core.ecology.biome import Biome
from mcpacker.model.core.ecology.biomefilter import BiomeFilter
from mcpacker.model.core.geology.bulk import Bulk
from mcpacker.model.core.geology.mineral import Mineral
from mcpacker.model.core.scarcity import Scarcity

import mcpacker.model.core.altitude as altitude
import mcpacker.model.core.scarcity as scarcity


# Class ############################################################################################

class Deposit:

    def __init__(
        self,
        name:str,
        altitude:Altitude=altitude.ANYWHERE,
        biomeFilters:Iterable[BiomeFilter]|BiomeFilter|None=None,
        scarcity:Scarcity=scarcity.SPARSE,
    ):
        self.altitude = altitude
        self.biomeFilters:list[BiomeFilter] = []
        self.gameId = name
        self.name = name
        self.scarcity = scarcity

        if not biomeFilters:
            biomeFilters = [BiomeFilter()]

        if isinstance(biomeFilters, BiomeFilter):
            biomeFilters = [biomeFilters]

        for biomeFilter in biomeFilters:
            self.biomeFilters.append(biomeFilter)

    def __repr__(self) -> str:
        return "".join([str(p) for p in [
            "Deposit(",
                "name=", self.name, ", ",
                "altitude=", repr(self.altitude), ", ",
                "biomeFilters=[", ", ".join(repr(self.biomeFilters)), "], ",
                "scarcity=", repr(self.scarcity),
            ")"
        ]])

    def __str__(self) -> str:
        return self.name

    def acceptsBiome(self, biome:Biome) -> bool:
        for biomeFilter in self.biomeFilters:
            if biomeFilter.accepts(biome): return True

        return False
