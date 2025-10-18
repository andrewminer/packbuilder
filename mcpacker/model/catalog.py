from collections.abc import Iterable
from typing import Any
from typing import Callable
from typing import Generic
from typing import Iterator
from typing import Protocol
from typing import TypeVar


# Type Support #####################################################################################

class HasName(Protocol):

    @property
    def name(self) -> str: ...

CatalogItem = TypeVar("CatalogItem", bound=HasName)

MapTarget = TypeVar("MapTarget")


# Class ############################################################################################

class Catalog(Generic[CatalogItem]):

    def __init__(self, items:Iterable[CatalogItem]|None=None):
        self._items:dict[str,CatalogItem] = {}

        for item in (items or []):
            self.add(item)

    def __contains__(self, name:str) -> bool:
        return name in self._items

    def __delitem__(self, name:str):
        del self._items[name]

    def __getitem__(self, name:str) -> CatalogItem:
        return self._items[name]

    def __iter__(self) -> Iterator[CatalogItem]:
        for name in sorted([i.name for i in self._items.values()]):
            yield self._items[name]

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return "".join(str(p) for p in [
            type(self).__name__, "(",
                "items=", repr(self._items),
            ")"
        ])

    def add(self, item:CatalogItem) -> "Catalog[CatalogItem]":
        if item.name in self._items:
            raise Exception(f"Catalog already contains {item.name}")

        self._items[item.name] = item
        return self

    def filter(self, isAllowed:Callable[[CatalogItem], bool]) -> Iterator[CatalogItem]:
        for item in self:
            if isAllowed(item):
                yield item

    def map(self, doTransform:Callable[[CatalogItem], MapTarget]) -> Iterator[MapTarget]:
        for item in self:
            yield doTransform(item)
