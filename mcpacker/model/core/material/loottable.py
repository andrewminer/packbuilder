from collections.abc                   import Iterable
from mcpacker.model.core.material.loot import Loot


# Class ############################################################################################

class LootTable:

    def __init__(self, items:Iterable[Loot]|Loot|None):
        if isinstance(items, Loot):
            items = [items]

        self.items = items or []
