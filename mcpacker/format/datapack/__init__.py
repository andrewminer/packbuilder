from collections.abc import Iterable
from mcpacker.format.datapack.moddata import ModData


# Class ############################################################################################

class DataPack:
    """
    A collection of data used to configure a Minecraft instance.

    see: https://minecraft.wiki/w/Data_pack
    """

    def __init__(self, name:str, mods:Iterable[ModData]|None=None):
        self.name = name
        self._mods:dict[str,ModData] = {}
        self._defaultMod:ModData|None = None

        for mod in (mods or []):
            self.add(mod)

    def add(self, mod:ModData) -> "DataPack":
        if not self._defaultMod:
            self._defaultMod = mod

        self._mods[mod.name] = mod
        return self

    def get(self, name:str) -> ModData:
        result = self._mods.get(name, None)
        if not result:
            result = self._mods[name] = ModData(name)

        return result

    @property
    def defaultMod(self) -> ModData|None:
        return self._defaultMod

    @defaultMod.setter
    def defaultMod(self, mod:ModData):
        if mod:
            existingModData = self.get(mod.name)
            if not existingModData:
                self.add(mod)
            elif existingModData != mod:
                raise Exception(f"Datapack already has a mod named {mod.name}")

        self._defaultMod = mod
