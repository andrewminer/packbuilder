from mcpacker.model.fauna.group import Group
from mcpacker.model.fauna.location import Location
from mcpacker.model.fauna.mob import Mob
from mcpacker.model.fauna.mobecotype import MobEcotype
from mcpacker.model.fauna.mobspawn import MobSpawn
from mcpacker.model.fauna.mobspawncatalog import MobSpawnCatalog
from mcpacker.model.scarcity import Scarcity
from mcpacker.model.spawnbuilder import SpawnBuilder
from typing import Self

import mcpacker.model.fauna.group as GR
import mcpacker.model.fauna.location as LO


# Class ############################################################################################

class MobSpawnBuilder(SpawnBuilder[Mob, MobEcotype, MobSpawn]):

    def __init__(self, catalog:MobSpawnCatalog):
        super().__init__(catalog, MobSpawn)

    @property
    def group(self) -> Group:
        return self._group

    @group.setter
    def group(self, value:Group|None):
        if not value:
            value = GR.SOLO

        self._group = value

    @property
    def location(self) -> Location:
        return self._location

    @location.setter
    def location(self, value:Location|None):
        if not value:
            value = LO.OUTSIDE

        self._location = value

    def _createEcotype(self) -> MobEcotype:
        return MobEcotype(self.scarcity, self.group, self.location)

    def _reset(self):
        super()._reset()
        self.group = None
        self.location = None
