from mcpacker.model.core.resourceid import ResourceId
from mcpacker.model.modpack import ModPack

# Helper Functions #################################################################################

def addDisabledFeatures(pack:ModPack):
    d = pack.disabledFeatures

    def add(resourceText:str):
        pack.disabledFeatures.append(ResourceId.parse(resourceText))

    # Disable Vanilla ore generation
    add("minecraft:ore_coal_lower")
    add("minecraft:ore_coal_upper")
    add("minecraft:ore_copper_large")
    add("minecraft:ore_copper")
    add("minecraft:ore_diamond_buried")
    add("minecraft:ore_diamond_large")
    add("minecraft:ore_diamond_medium")
    add("minecraft:ore_diamond")
    add("minecraft:ore_emerald")
    add("minecraft:ore_gold_deltas")
    add("minecraft:ore_gold_extra")
    add("minecraft:ore_gold_lower")
    add("minecraft:ore_gold")
    add("minecraft:ore_iron_middle")
    add("minecraft:ore_iron_small")
    add("minecraft:ore_iron_upper")
    add("minecraft:ore_lapis_buried")
    add("minecraft:ore_lapis")
    add("minecraft:ore_redstone_lower")
    add("minecraft:ore_redstone")
