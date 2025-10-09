from collections.abc import Iterable
from typing          import Any
from typing          import Callable
from typing          import Generic
from typing          import Iterator
from typing          import Protocol
from typing          import TypeVar


# Type Support #####################################################################################

class HasGameId(Protocol):

    @property
    def gameId(self) -> str: ...

CatalogItem = TypeVar("CatalogItem", bound=HasGameId)

MapTarget = TypeVar("MapTarget")


# Class ############################################################################################

class Catalog(Generic[CatalogItem]):

    def __init__(self, items:Iterable[CatalogItem]|None=None):
        self._items:dict[str,CatalogItem] = {}

        for item in (items or []):
            self.add(item)

    def __contains__(self, gameId:str) -> bool:
        return gameId in self._items

    def __delitem__(self, gameId:str):
        del self._items[gameId]

    def __eq__(self, other:Any) -> bool:
        if type(self) != type(other): return False
        if self._items != other._items: return False
        return True

    def __getitem__(self, gameId:str) -> CatalogItem:
        return self._items[gameId]

    def __iter__(self) -> Iterator[CatalogItem]:
        for gameId in sorted([i.gameId for i in self._items.values()]):
            yield self._items[gameId]

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return "".join(str(p) for p in [
            self.__class__.__name__, "[",
                ", ".join(str(i) for i in self),
            "]"
        ])

    def add(self, item:CatalogItem) -> "Catalog[CatalogItem]":
        if item.gameId in self._items:
            raise Exception(f"Catalog already contains {item.gameId}")

        self._items[item.gameId] = item
        return self

    def filter(self, isAllowed:Callable[[CatalogItem], bool]) -> Iterator[CatalogItem]:
        for item in self:
            if isAllowed(item):
                yield item

    def map(self, doTransform:Callable[[CatalogItem], MapTarget]) -> Iterator[MapTarget]:
        for item in self:
            yield doTransform(item)
