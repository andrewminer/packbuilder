from collections.abc import Iterable
from collections.abc import Iterator
from mcpacker.format.resourcepack.modresource import ModResource


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

        self._mods[mod.mod] = mod
        return self

    def get(self, name:str) -> ModResource:
        result = self._mods.get(name, None)
        if not result:
            result = self._mods[name] = ModResource(name)

        return result

    @property
    def defaultMod(self) -> ModResource|None:
        return self._defaultMod

    @defaultMod.setter
    def defaultMod(self, mod:ModResource):
        if mod:
            existingMod = self.get(mod.mod)
            if not existingMod:
                self.add(mod)
            elif existingMod != mod:
                raise Exception(f"Resourcepack already has a mod named {mod.mod}")

        self._defaultMod = mod

    @property
    def mods(self) -> Iterator[ModResource]:
        for mod in self._mods.values():
            yield mod
