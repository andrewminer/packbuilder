from collections.abc import Iterable
from mcpacker.format.datapack import DataPack
from mcpacker.model.resourceid import ResourceId
from mcpacker.model.world import World
from mcpacker.model.mod import Mod
from mcpacker.format.resourcepack import ResourcePack
from typing import Callable
from typing import Self


# Type Helpers #####################################################################################

type AugmentFunc = Callable[[ModPack], None]


# Class ############################################################################################

class ModPack:

    def __init__(
        self,
        name:str,
        mods:Iterable[Mod]|None=None,
        world:World|None=None,
        dataPack:DataPack|None=None,
        resourcePack:ResourcePack|None=None,
        disabledFeatures:Iterable[ResourceId]|None=None
    ):
        self.name = name

        self.dataPack = dataPack or DataPack(self.name)
        self.mods = {mod.name: mod for mod in (mods or [])}
        self.disabledFeatures = list(disabledFeatures or [])
        self.resourcePack = resourcePack or ResourcePack(self.name)
        self.world = world or World()

    def augment(self, doAugment:AugmentFunc) -> Self:
        doAugment(self)
        return self
