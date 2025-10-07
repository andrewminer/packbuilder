from mcpacker.model.core.geology.mineral import Mineral
from typing import Iterator


# Class ############################################################################################

class MineralCatalog:

    def __init__(self, minerals:tuple[Mineral]=None):
        self._minerals = {}

        for mineral in (minerals or []):
            self.add(mineral)

    def add(self, mineral:Mineral) -> "MineralCatalog":
        if mineral.name in self._minerals:
            raise Exception(f"Catalog already contains an entry for {mineral.name}")

        self._minerals[mineral.name] = mineral

    def all(self) -> Iterator[Mineral]:
        for mineral in self._minerals.values():
            yield mineral

    def get(self, name:str) -> Mineral|None:
        return self._minerals.get(name, None)
