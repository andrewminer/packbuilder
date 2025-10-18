from collections.abc               import Iterable
from mcpacker.model.core.habitat   import Habitat
from mcpacker.model.core.fauna.mob import Mob
from mcpacker.model.core.spawn     import Spawn


# Class ############################################################################################

class MobSpawn(Spawn):
    """
    A description of where a creature should appear in the world.
    """

    def __init__(self, mob:Mob, habitats:Iterable[Habitat]|Habitat|None=None):
        super().__init__(habitats)
        self.mob = mob

    @property
    def name(self) -> str:
        return self.mob.name
