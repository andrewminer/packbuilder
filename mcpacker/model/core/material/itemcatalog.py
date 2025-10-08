from mcpacker.model.core.material.item import Item
from typing import Iterator


# Class ############################################################################################

class ItemCatalog:

    def __init__(self, items:tuple[Item]=None):
        self._items = {}

        for item in (items or []):
            self.add(item)

    def add(self, item:Item) -> "ItemCatalog":
        if item.gameId in self._items:
            raise Exception(f"Catalog already contains an entry for {item.gameId}")

        self._items[item.gameId] = item

    def all(self) -> Iterator[Item]:
        for item in self._items.values():
            yield item

    def get(self, gameId:str) -> Item|None:
        return self._items.get(gameId, None)

