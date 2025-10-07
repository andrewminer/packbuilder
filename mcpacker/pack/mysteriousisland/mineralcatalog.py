from mcpacker.model.core.geology.mineral import Mineral
from mcpacker.model.core.geology.mineralcatalog import MineralCatalog
from mcpacker.model.core.geology.replacement import Replacement


# Constants ########################################################################################

IE = "immersiveengineering"
OQ = "overworldquartzore"
RC = "railcraft"


# Helpers ##########################################################################################

def makeMineral(name:str, blockId:str, deepslateBlockId:None|str=None) -> Mineral:
    deepslateBlockId = deepslateBlockId if deepslateBlockId else blockId

    return Mineral(name, [
        Replacement.inStone(blockId),
        Replacement.inDeepslate(blockId)
    ])

def makeOreMineral(name:str) -> Mineral:
    return Mineral(name, [
        Replacement.inStone(f"{name}_ore"),
        Replacement.inDeepslate(f"deepslate_{name}_ore")
    ])

def makeImmersiveEngineeringOreMineral(name:str) -> Mineral:
    return Mineral(name, [
        Replacement.inStone(f"{IE}:ore_{name}"),
        Replacement.inDeepslate("{IE}:deepslate_ore_{name}")
    ])

def makeRailcraftOreMineral(name:str) -> Mineral:
    return Mineral(name, [
        Replacement.inStone(f"{RC}:{name}_ore"),
        Replacement.inDeepslate("{RC}:deepslate_{name}_ore")
    ])


# Catalog ##########################################################################################

CATALOG = C = MineralCatalog()

# Basic Ores
C.add(makeOreMineral("coal"))
C.add(makeOreMineral("copper"))
C.add(makeOreMineral("diamond"))
C.add(makeOreMineral("emerald"))
C.add(makeOreMineral("gold"))
C.add(makeOreMineral("iron"))
C.add(makeOreMineral("lapis"))
C.add(makeOreMineral("redstone"))

# Crystals
C.add(makeMineral("amethyst",   "amethyst_block"))
C.add(makeMineral("glowstone",  "glowstone"))
C.add(makeMineral("quartz",    f"{OQ}:quartz_ore", f"{OQ}:deepslate_quartz_ore"))
C.add(makeMineral("salt",       "butcher:saltblock"))

# Earth, gravel, etc.
C.add(makeMineral("clay",       "clay"))
C.add(makeMineral("coarsedirt", "coarse_dirt"))
C.add(makeMineral("dirt",       "dirt"))
C.add(makeMineral("gravel",     "gravel"))
C.add(makeMineral("loam",       "farmersdelight:rich_soil"))
C.add(makeMineral("packedice",  "packed_ice"))
C.add(makeMineral("peat",       "kubejs:peat_block"))
C.add(makeMineral("redsand",    "redsand"))
C.add(makeMineral("sand",       "sand"))
C.add(makeMineral("soulsand",   "soulsand"))

# Stone
C.add(makeMineral("andesite",   "andesite"))
C.add(makeMineral("arkrose",    "red_sandstone"))
C.add(makeMineral("basalt",     "basalt"))
C.add(makeMineral("breccia",    "cobblestone"))
C.add(makeMineral("chalk",      "calcite"))
C.add(makeMineral("diorite",    "diorite"))
C.add(makeMineral("dolostone",  "end_stone"))
C.add(makeMineral("gneiss",     "deepslate"))
C.add(makeMineral("granite",    "granite"))
C.add(makeMineral("greywacke",  "stone"))
C.add(makeMineral("komatite",   "blackstone"))
C.add(makeMineral("limestone",  "dripstone_block"))
C.add(makeMineral("magma",      "magma_block"))
C.add(makeMineral("marble",    f"{RC}:quarried_stone"))
C.add(makeMineral("netherite",  "ancient_debris"))
C.add(makeMineral("obsidian",   "obsidian"))
C.add(makeMineral("pumice",     "netherrack"))
C.add(makeMineral("sandstone",  "sandstone"))
C.add(makeMineral("tuff",       "tuff"))

# Immersive Engineering Ores
C.add(makeImmersiveEngineeringOreMineral("aluminum"))
C.add(makeImmersiveEngineeringOreMineral("lead"))
C.add(makeImmersiveEngineeringOreMineral("nickel"))
C.add(makeImmersiveEngineeringOreMineral("silver"))
C.add(makeImmersiveEngineeringOreMineral("uranium"))

# Railcraft Ores
C.add(Mineral("saltpeter", [
    Replacement("sand", f"{RC}:saltpeter_ore"),
    Replacement("sandstone", f"{RC}:saltpeter_ore"),
]))
C.add(makeRailcraftOreMineral("sulfur"))
C.add(makeRailcraftOreMineral("tin"))
C.add(makeRailcraftOreMineral("zinc"))
