from mcpacker.model.core.material.block         import Block
from mcpacker.model.core.material.blockcatalog  import BlockCatalog
from mcpacker.model.core.material.item          import Item
from mcpacker.model.core.material.loottable     import LootTable
from mcpacker.model.core.material.loot          import Loot
from mcpacker.model.modpack                     import ModPack

import mcpacker.model.core.material.soundtype as SO


# Functions ########################################################################################

def addBlocks(pack:ModPack):
    blocks = pack.world.blocks
    items = pack.world.items

    blocks.add(Block(
        gameId    = "kubejs:peat_block",
        loot      = LootTable(Loot.of(items.get("kubejs:peat_chunk"), 2, 9)),
        name      = "Peat Block",
        soundType = SO.DIRT,
        tags      = ["minecraft:mineable/shovel"],
    ))
