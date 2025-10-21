from collections.abc import Iterable
from mcpacker.model.material.loottable import LootTable
from mcpacker.model.material.soundtype import SoundType
from mcpacker.model.resourceid import ResourceId

import mcpacker.model.material.soundtype as ST


# Class ############################################################################################

class Block:

    def __init__(
        self,
        name:str,
        gameId:str,
        loot:LootTable,
        requiresTool:bool=False,
        soundType:SoundType=ST.STONE,
        tags:Iterable[str]|None=None,
    ):
        self.gameId        = gameId
        self.loot          = loot
        self.name          = name
        self.requiresTool  = requiresTool
        self.silkTouchLoot = loot
        self.soundType     = soundType
        self.tags          = tags or []
