from mcpacker.model.habitat import Habitat
from mcpacker.model.fauna.mob import Mob
from mcpacker.model.fauna.mobecotype import MobEcotype
from mcpacker.model.spawn import Spawn


# Class ############################################################################################

class MobSpawn(Spawn[Mob, MobEcotype]):
    """
    Describes a certain habitat for a particular animal with its local variations.
    """

    def __init__(self, name:str, habitat:Habitat, mob:Mob, ecotype:MobEcotype):
        super().__init__(name, habitat, mob, ecotype)

    @property
    def mob(self) -> Mob:
        return self.spawnable
