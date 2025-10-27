from mcpacker.model.catalog import Catalog
from mcpacker.model.ecotype import Ecotype
from mcpacker.model.geology.bulk import Bulk
from mcpacker.model.geology.deposittype import DepositType
from mcpacker.model.geology.mineral import Mineral
from mcpacker.model.geology.mineralecotype import MineralEcotype
from mcpacker.model.geology.mineralspawn import MineralSpawn
from mcpacker.model.resourceid import ResourceId
from mcpacker.model.spawnbuilder import SpawnBuilder
from typing import Self

import mcpacker.model.geology.bulk as BU
import mcpacker.model.geology.deposittype as DE


# Class ############################################################################################

class MineralSpawnBuilder(SpawnBuilder[Mineral, MineralEcotype, MineralSpawn]):

    def __init__(self, catalog:Catalog[MineralSpawn]):
        super().__init__(catalog, MineralSpawn)

    def _createEcotype(self) -> MineralEcotype:
        return MineralEcotype(self.scarcity, self.bulk, self.depositType)

    def _reset(self):
        super()._reset()
        self.bulk = None
        self.depositType = None

    @property
    def bulk(self) -> Bulk:
        return self._bulk

    @bulk.setter
    def bulk(self, value:Bulk|None):
        if value == None:
            value = BU.MEDIUM

        self._bulk = value

    @property
    def depositType(self) -> DepositType:
        return self._depositType

    @depositType.setter
    def depositType(self, value:DepositType|None):
        if value == None:
            value = DE.VEIN

        self._depositType = value
