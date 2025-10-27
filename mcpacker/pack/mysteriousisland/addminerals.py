from mcpacker.model.geology.mineral import Mineral
from mcpacker.model.geology.replacement import Replacement
from mcpacker.model.modpack import ModPack


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

def makeEvaporate(name:str, blockId:str) -> Mineral:
    return Mineral(name, [
        Replacement("minecraft:sand", blockId),
        Replacement("minecraft:sandstone", blockId)
    ])

def makeOreMineral(name:str) -> Mineral:
    return Mineral(name, [
        Replacement.inStone(f"{name}_ore"),
        Replacement.inDeepslate(f"deepslate_{name}_ore")
    ])

def makeImmersiveEngineeringOreMineral(name:str) -> Mineral:
    return Mineral(name, [
        Replacement.inStone(f"{IE}:ore_{name}"),
        Replacement.inDeepslate(f"{IE}:deepslate_ore_{name}")
    ])

def makeRailcraftOreMineral(name:str) -> Mineral:
    return Mineral(name, [
        Replacement.inStone(f"{RC}:{name}_ore"),
        Replacement.inDeepslate(f"{RC}:deepslate_{name}_ore")
    ])


# Catalog ##########################################################################################

def addMinerals(pack:ModPack):
    minerals = pack.world.minerals

    # Metals
    minerals.add(makeImmersiveEngineeringOreMineral("aluminum"))
    minerals.add(makeImmersiveEngineeringOreMineral("lead"))
    minerals.add(makeImmersiveEngineeringOreMineral("nickel"))
    minerals.add(makeImmersiveEngineeringOreMineral("silver"))
    minerals.add(makeImmersiveEngineeringOreMineral("uranium"))
    minerals.add(makeOreMineral("copper"))
    minerals.add(makeOreMineral("gold"))
    minerals.add(makeOreMineral("iron"))
    minerals.add(makeRailcraftOreMineral("tin"))
    minerals.add(makeRailcraftOreMineral("zinc"))

    # Organic Minerals
    minerals.add(makeOreMineral("coal"))
    minerals.add(makeMineral("peat", "kubejs:peat_block"))
    minerals.add(makeMineral("loam", "farmersdelight:rich_soil"))

    # Industrial Minerals
    minerals.add(makeEvaporate("salt", "butcher:saltblock"))
    minerals.add(makeRailcraftOreMineral("sulfur"))
    minerals.add(makeEvaporate("nitrate", f"{RC}:saltpeter_ore"))

    # Crystaline Minerals
    minerals.add(makeMineral("amethyst", "amethyst_block"))
    minerals.add(makeMineral("glowstone", "glowstone"))
    minerals.add(makeMineral("quartz", f"{OQ}:quartz_ore", f"{OQ}:deepslate_quartz_ore"))
    minerals.add(makeOreMineral("diamond"))
    minerals.add(makeOreMineral("emerald"))
    minerals.add(makeOreMineral("lapis"))
    minerals.add(makeOreMineral("redstone"))

    # Earth, gravel, etc.
    minerals.add(makeMineral("clay", "clay"))
    minerals.add(makeMineral("coarsedirt", "coarse_dirt"))
    minerals.add(makeMineral("dirt", "dirt"))
    minerals.add(makeMineral("gravel", "gravel"))
    minerals.add(makeMineral("packedice", "packed_ice"))
    minerals.add(makeMineral("redsand", "redsand"))
    minerals.add(makeMineral("sand", "sand"))
    minerals.add(makeMineral("soulsand", "soulsand"))

    # Stone
    minerals.add(makeMineral("andesite", "andesite"))
    minerals.add(makeMineral("arkrose", "red_sandstone"))
    minerals.add(makeMineral("basalt", "basalt"))
    minerals.add(makeMineral("breccia", "cobblestone"))
    minerals.add(makeMineral("chalk", "calcite"))
    minerals.add(makeMineral("diorite", "diorite"))
    minerals.add(makeMineral("dolostone", "end_stone"))
    minerals.add(makeMineral("gneiss", "deepslate"))
    minerals.add(makeMineral("granite", "granite"))
    minerals.add(makeMineral("greywacke", "stone"))
    minerals.add(makeMineral("komatite", "blackstone"))
    minerals.add(makeMineral("limestone", "dripstone_block"))
    minerals.add(makeMineral("magma", "magma_block"))
    minerals.add(makeMineral("marble", f"{RC}:quarried_stone"))
    minerals.add(makeMineral("obsidian", "obsidian"))
    minerals.add(makeMineral("pumice", "netherrack"))
    minerals.add(makeMineral("sandstone", "sandstone"))
    minerals.add(makeMineral("tuff", "tuff"))
