from collections.abc import Iterable
from mcpacker.model.altitude import Altitude
from mcpacker.model.catalog import Catalog
from mcpacker.model.ecology.biomefilter import BiomeFilter
from mcpacker.model.ecotype import Ecotype
from mcpacker.model.habitat import Habitat
from mcpacker.model.season import Season
from mcpacker.model.scarcity import Scarcity
from mcpacker.model.spawn import Spawn
from mcpacker.model.spawnable import Spawnable
from typing import Self
from typing import Generic
from typing import TypeVar

import mcpacker.model.altitude as AL
import mcpacker.model.scarcity as SC
import mcpacker.model.season as SE


# Class ############################################################################################

class SpawnBuilder[SpawnableKind:Spawnable, EcotypeKind:Ecotype, SpawnKind:Spawn]:

    def __init__(self, catalog:Catalog[SpawnKind], spawnClass:type[SpawnKind]):
        self._catalog = catalog
        self._spawnable:SpawnableKind|None = None
        self._spawnClass = spawnClass
        self._reset()

    def start(self, spawnable:SpawnableKind) -> Self:
        self._reset()
        self._spawnable = spawnable
        return self

    def save(self, name:str) -> Self:
        if not self._spawnable: raise RuntimeError("you must call start before save")

        self._catalog.add(
            self._spawnClass(name, self._createHabitat(), self._spawnable, self._createEcotype())
        )
        return self

    # Properties ###############################################################

    @property
    def altitude(self) -> Altitude:
        return self._altitude

    @altitude.setter
    def altitude(self, value:Altitude|None):
        if value == None:
            value = AL.ANYWHERE

        self._altitude = value

    @property
    def biomeFilters(self) -> list[BiomeFilter]:
        return self._biomeFilters

    @biomeFilters.setter
    def biomeFilters(self, value:Iterable[BiomeFilter]|BiomeFilter|None):
        if value == None:
            value = BiomeFilter()
        if isinstance(value, BiomeFilter):
            value = [value]

        self._biomeFilters = list(value)

    @property
    def scarcity(self) -> Scarcity:
        return self._scarcity

    @scarcity.setter
    def scarcity(self, value:Scarcity|None):
        if value == None:
            value = SC.SPARSE

        self._scarcity = value

    @property
    def seasons(self) -> list[Season]:
        return self._seasons

    @seasons.setter
    def seasons(self, value:Iterable[Season]|Season|None):
        if value == None:
            value = SE.ALL
        if isinstance(value, Season):
            value = [value]

        self._seasons = list(value)

    # Subclass Overrides #######################################################

    def _createEcotype(self) -> EcotypeKind:
        raise NotImplementedError()

    def _reset(self):
        self.altitude = None
        self.biomeFilters = None
        self.scarcity = None
        self.seasons = None

    # Private Methods ##########################################################

    def _createHabitat(self) -> Habitat:
        return Habitat(self.altitude, self.biomeFilters, self.seasons)
