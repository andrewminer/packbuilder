from collections.abc import Iterable
from mcpacker.model.core.geology.replacement import Replacement
from mcpacker.model.core.resourceid import ResourceId


# Class ############################################################################################

class Mineral:

    def __init__(self, name:str, replacements:Iterable[Replacement]|None=None):
        self.name = name
        self.gameId = name
        self.replacements = list(replacements or [])

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return "".join([str(p) for p in [
            f"Mineral(" +
                "name=", repr(self.name), ", ",
                "replacements=", repr(self.replacements),
            ")"
        ]])
