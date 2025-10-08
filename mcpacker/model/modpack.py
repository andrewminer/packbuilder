from collections.abc             import Iterable
from mcpacker.model.core.world   import World
from mcpacker.model.datapack     import DataPack
from mcpacker.model.mod          import Mod
from mcpacker.model.resourcepack import ResourcePack
from typing                      import Callable


# Class ############################################################################################

class ModPack:

    def __init__(
        self,
        name:str,
        mods:Iterable[Mod]|None=None,
        world:World|None=None,
        dataPack:DataPack|None=None,
        resourcePack:ResourcePack|None=None,
    ):
        self.name         = name
        self.world        = world or World()
        self.dataPack     = dataPack or DataPack(self.name)
        self.resourcePack = resourcePack or ResourcePack(self.name)

        self._mods = {}
        for mod in (mods or []):
            self._mods[mod.name] = mod

    def augment(self, doAugment:"Callable[[ModPack], None]") -> "ModPack":
        doAugment(self)
