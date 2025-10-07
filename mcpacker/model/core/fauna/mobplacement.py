from mcpacker.model.core.habitat import Habitat
from mcpacker.model.core.fauna.mob import Mob
from mcpacker.model.core.placement import Placement


# Class ############################################################################################

class MobPlacement(Placement):
    """
    A description of where a creature should appear in the world.
    """

    def __init__(self, mob:Mob, habitats:list[Habitat]=None):
        super().__init__(habitats)
        self.mob = mob
