from mcpacker.model.material.item import Item
from mcpacker.model.modpack import ModPack


# Constants ########################################################################################

def addItems(pack:ModPack):
    pack.world.items.add(Item("kubejs:peat_chunk"))
