from mcpacker.model.core.material.loot import Loot


# Class ############################################################################################

class LootTable:

    def __init__(self, items:list[Loot]):
        self.items = items
