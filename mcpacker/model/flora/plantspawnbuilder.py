from mcpacker.model.ecotype import Ecotype
from mcpacker.model.flora.plant import Plant
from mcpacker.model.flora.plantspawn import PlantSpawn
from mcpacker.model.flora.plantspawncatalog import PlantSpawnCatalog
from mcpacker.model.spawnbuilder import SpawnBuilder
from typing import Self


# Class ############################################################################################

class PlantSpawnBuilder(SpawnBuilder[Plant, Ecotype, PlantSpawn]):

    def __init__(self, catalog:PlantSpawnCatalog):
        super().__init__(catalog, PlantSpawn)

    def _createEcotype(self) -> Ecotype:
        return Ecotype(self.scarcity)
