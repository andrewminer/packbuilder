from collections.abc import Iterable
from mcpacker.model.altitude import Altitude
from mcpacker.model.ecology.biome import Biome
from mcpacker.model.ecology.biomefilter import BiomeFilter
from mcpacker.model.season import Season

import mcpacker.model.altitude as AL
import mcpacker.model.season as SE


# Class ############################################################################################

class Habitat:
    """
    A description of where and when various features may be present.
    """

    def __init__(
        self,

        altitude:Altitude=AL.ANYWHERE,
        biomeFilters:Iterable[BiomeFilter]|BiomeFilter|None=None,
        seasons:Iterable[Season]|Season=SE.ALL,
    ):
        if not biomeFilters:
            biomeFilters = BiomeFilter()
        if isinstance(biomeFilters, BiomeFilter):
            biomeFilters = [biomeFilters]

        if isinstance(seasons, Season):
            seasons = [seasons]

        self.altitude = altitude
        self.biomeFilters = biomeFilters
        self.seasons = seasons

        self._source:Habitat|None = None

    def __str__(self) -> str:
        return (
            f"{self.altitude!s}|"
            f"{self.biomeFilters!s}|"
            f"{self.seasons!s}"
        )

    def __repr__(self) -> str:
        return "".join([str(p) for p in [
            "Habitat(",
                f"altitude={self.altitude!r}, "
                f"biomeFilters={self.biomeFilters!r}, "
                f"seasons={self.seasons!r}"
            ")"
        ]])

    def accepts(self, biome:Biome) -> bool:
        for biomeFilter in self.biomeFilters:
            if not biomeFilter.accepts(biome): return False

        return True
