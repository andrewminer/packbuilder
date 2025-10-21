from collections.abc import Iterable
from mcpacker.model.altitude import Altitude
from mcpacker.model.ecology.biome import Biome
from mcpacker.model.ecology.biomefilter import BiomeFilter
from mcpacker.model.flora.plant import Plant
from mcpacker.model.scarcity import Scarcity

import mcpacker.model.altitude as AL
import mcpacker.model.scarcity as SC


# Class ############################################################################################

class PlantSpawn:

    def __init__(
        self,
        plant:Plant,
        altitude:Altitude=AL.ANYWHERE,
        biomeFilters:Iterable[BiomeFilter]|BiomeFilter|None=None,
        scarcity:Scarcity=SC.SPARSE,
    ):
        if not biomeFilters:
            biomeFilters = BiomeFilter()
        if not isinstance(biomeFilters, Iterable):
            biomeFilters = [biomeFilters]

        self.altitude = altitude
        self.biomeFilters = list(biomeFilters)
        self.plant = plant
        self.scarcity = scarcity

    def __repr__(self) -> str:
        return "".join([
            "PlantSpawn(",
                "altitude=", repr(self.altitude), ", ",
                "biomeFilters=", repr(self.biomeFilters), ", ",
                "plant=", repr(self.plant), ", ",
                "scarcity=", repr(self.scarcity),
            ")"
        ])

    @property
    def name(self) -> str:
        return self.plant.name

    def acceptsBiome(self, biome:Biome) -> bool:
        for biomeFilter in self.biomeFilters:
            if biomeFilter.accepts(biome): return True

        return False
