from collections.abc import Iterable
from mcpacker.model.catalog import Catalog
from mcpacker.model.material.item import Item
from mcpacker.model.resourceid import ResourceId
from typing import Iterator


# Class ############################################################################################

class ItemCatalog(Catalog[Item]):
    pass
