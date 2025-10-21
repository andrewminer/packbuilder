from collections.abc import Iterable
from mcpacker.model.ecology.biome import Biome
from mcpacker.model.habitat import Habitat
from mcpacker.model.fauna.mob import Mob
from mcpacker.model.spawn import Spawn


# Class ############################################################################################

class MobSpawn(Spawn):
    """
    A description of where a creature should appear in the world.
    """

    def __init__(self, mob:Mob, habitats:Iterable[Habitat]|Habitat|None=None):
        self.mob = mob
        super().__init__(habitats)

    def __str__(self) -> str:
        return self.name

    @property
    def name(self) -> str:
        return self.mob.name

    def acceptedBy(self, biome:Biome) -> list[Habitat]:
        result = []

        for habitat in self.habitats:
            if habitat.accepts(biome):
                result.append(habitat)

        return result
