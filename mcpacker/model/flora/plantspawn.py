from mcpacker.model.ecotype import Ecotype
from mcpacker.model.habitat import Habitat
from mcpacker.model.spawn import Spawn
from mcpacker.model.flora.plant import Plant


# Class ############################################################################################

class PlantSpawn(Spawn[Plant, Ecotype]):
    """
    Describes a certain habitat for a particular animal with its local variations.
    """

    def __init__(self, name:str, habitat:Habitat, plant:Plant, ecotype:Ecotype):
        super().__init__(name, habitat, plant, ecotype)

    @property
    def plant(self) -> Plant:
        return self.spawnable
