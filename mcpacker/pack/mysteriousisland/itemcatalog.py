from mcpacker.model.core.material.item import Item
from mcpacker.model.modpack            import ModPack


# Constants ########################################################################################

def addItems(pack:ModPack):
    pack.world.items.add(Item("kubejs:peak_chunk"))
