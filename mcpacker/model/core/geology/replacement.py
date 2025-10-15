from mcpacker.model.core.resourceid import ResourceId


# Constants ########################################################################################

STONE_REPLACEABLES = "#minecraft:stone_ore_replaceables"
DEEPSLATE_REPLACEABLES = "#minecraft:deepslate_ore_replaceables"


# Class ############################################################################################

class Replacement:

    @staticmethod
    def inStone(target:str, weight:int=100):
        return Replacement(STONE_REPLACEABLES, target, weight)

    @staticmethod
    def inDeepslate(target:str, weight:int=100):
        return Replacement(DEEPSLATE_REPLACEABLES, target, weight)

    def __init__(self, source:str, target:str, weight:int=100):
        self.source = ResourceId.canonical(source)
        self.target = ResourceId.canonical(target)
        self.weight = weight

    def __str__(self) -> str:
        if self.weight == 100:
            return f"{self.source} => {self.target}"

        return f"{self.source} => {self.target} ({self.weight}%)"

    def __repr__(self) -> str:
        return "".join([str(p) for p in [
            "Replacement(" +
                "source=", repr(self.source), ", ",
                "target=", repr(self.target), ", ",
                "weight=", repr(self.weight),
            ")"
        ]])
