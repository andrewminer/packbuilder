from mcpacker.model.resourceid import ResourceId


# Constants ########################################################################################

DEEPSLATE_REPLACEABLES = "#minecraft:deepslate_ore_replaceables"
NETHERRACK_REPLACEABLES = "#minecraft:base_stone_nether"
STONE_REPLACEABLES = "#minecraft:stone_ore_replaceables"


# Class ############################################################################################

class Replacement:

    @staticmethod
    def inDeepslate(target:ResourceId|str):
        return Replacement(DEEPSLATE_REPLACEABLES, target)

    @staticmethod
    def inNetherrack(target:ResourceId|str):
        return Replacement(NETHERRACK_REPLACEABLES, target)

    @staticmethod
    def inStone(target:ResourceId|str):
        return Replacement(STONE_REPLACEABLES, target)

    def __init__(self, source:ResourceId|str, target:ResourceId|str):
        self.source = ResourceId.parse(source)
        self.target = ResourceId.parse(target)

    def __str__(self) -> str:
        return f"{self.source} => {self.target}"

    def __repr__(self) -> str:
        return (
            "Replacement("
                f"source={self.source!r}, "
                f"target={self.target!r}"
            ")"
        )
