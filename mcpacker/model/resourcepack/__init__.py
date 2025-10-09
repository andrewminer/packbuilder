from collections.abc import Iterable
from mcpacker.model.resourcepack.modresource import ModResource


# Class ############################################################################################

class ResourcePack:

    def __init__(self, name:str, mods:Iterable[ModResource]|None=None):
        self.name = name
        self._mods:dict[str,ModResource] = {}
        self._defaultMod:ModResource|None = None

        for mod in (mods or []):
            self.add(mod)

    def add(self, mod:ModResource) -> "ResourcePack":
        if not self._defaultMod:
            self._defaultMod = mod

        self._mods[mod.name] = mod
        return self

    def get(self, name:str) -> ModResource|None:
        return self._mods.get(name, None)

    @property
    def defaultMod(self) -> ModResource|None:
        return self._defaultMod

    @defaultMod.setter
    def defaultMod(self, mod:ModResource):
        if mod:
            existingMod = self.get(mod.name)
            if not existingMod:
                self.add(mod)
            elif existingMod != mod:
                raise Exception(f"Resourcepack already has a mod named {mod.name}")

        self._defaultMod = mod

