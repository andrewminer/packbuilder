from tungston.core.geology.replacement import Replacement
from tungston.core.resourceid import ResourceId


# Class ############################################################################################

class Mineral:

    def __init__(self, name:str, replacements:None|tuple[Replacement]=None):
        self.name = name
        self.replacements = replacements or []

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return "".join([str(p) for p in [
            f"Mineral<{self.name}>", "{",
                "replacements: [",
                    ", ".join([str(r) for r in self.replacements]),
                "]",
            "}"
        ]])

    def addStoneReplacement(self, blockId:str) -> "Mineral":
        blockId = ResourceId.canonical(blockId)
        self.replacements.append(Replacement(STONE_REPLACEABLES, blockId))
        return self

    def addDeepslateReplacement(self, blockId:str) -> "Mineral":
        blockId = ResourceId.canonical(blockId)
        self.replacements.append(Replacement(DEEPSLATE_REPLACEABLES, blockId))
