from mcpacker.model.geology.mineralecotype import MineralEcotype
from mcpacker.model.geology.mineral import Mineral
from mcpacker.model.habitat import Habitat
from mcpacker.model.spawn import Spawn


# Class ############################################################################################

class MineralSpawn(Spawn[Mineral, MineralEcotype]):

    def __init__(self, name:str, habitat:Habitat, deposit:Mineral, ecotype:MineralEcotype):
        super().__init__(name, habitat, deposit, ecotype)

    @property
    def mineral(self) -> Mineral:
        return self.spawnable
