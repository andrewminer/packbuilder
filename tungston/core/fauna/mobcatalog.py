from collections.abc import Iterator
from tungston.core.fauna.mobplacement import MobPlacement


# Class ############################################################################################

class MobCatalog:

    def __init__(self, mobs:tuple[MobPlacement]):
        self._mobs = {}

        for mob in mobs:
            self.add(mob)

    def add(self, placement:MobPlacement) -> "MobCatalog":
        if placement.mob.name in self._mobs:
            raise Exception("Catalog already has an entry for {mob.name}")

        self._mobs[placement.mob.name] = placement

    def all(self) -> Iterator[MobPlacement]:
        for placement in self._mobs.values():
            yield placement

    def get(self, name:str) -> MobPlacement:
        return self._mobs.get(name, None)
