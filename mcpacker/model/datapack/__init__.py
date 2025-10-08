from collections.abc import Iterable
from mcpacker.model.datapack.mod import Mod


# Class ############################################################################################

class DataPack:

    def __init__(self, name:str, mods:Iterable[Mod]|None=None):
        self.name = name
        self._mods = {}
        self._defaultMod = None

        for mod in (mods or []):
            self.add(mod)

    def add(self, mod:Mod) -> "Datapack":
        if not self._defaultMod:
            self._defaultMod = mod

        self._mods[mod.name] = mod
        return self

    def get(self, modName:str) -> Mod:
        return self._mods.get(modName, None)

    @property
    def defaultMod(self) -> Mod:
        return self._defaultMod

    @defaultMod.setter
    def setDefaultMod(self, mod:Mod) -> "Datapack":
        existingMod = self.get(mod.name)
        if not existingMod:
            self.add(mod)
        elif existingMod != mod:
            raise Exception(f"Datapack already has a mod named {mod.name}")

        self._defaultMod = mod
