from collections.abc import Iterable
from mcpacker.model.catalog import Catalog
from mcpacker.model.core.material.item import Item
from mcpacker.model.core.resourceid import ResourceId
from typing import Iterator


# Class ############################################################################################

class ItemCatalog(Catalog[Item]):
    pass
