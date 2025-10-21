from mcpacker.model.core.blockstate import BlockState
from mcpacker.model.core.flora.patch import Patch
from mcpacker.model.core.flora.tree import Tree
from mcpacker.model.modpack import ModPack

import mcpacker.model.core.flora.canopyshape as CA
import mcpacker.model.core.flora.density as DE
import mcpacker.model.core.flora.immersion as IM
import mcpacker.model.core.flora.trunkshape as TR


# Constants ########################################################################################

CD = "corndelight"
FD = "farmersdelight"
IE = "immersiveengineering"
IH = "immersivehealing"
MC = "minecraft"
RD = "rusticdelight"
RW = "realisticwheat"
UD = "fruitsdelight"
SU = "supplementaries"


# Functions ########################################################################################

def addPlants(pack:ModPack):
    plants = pack.world.plants

    # Crop Patches #############################################################

    plants.add(Patch(
        name = "athelas",
        blocks = f"{IH}:medica_herb_block",
        density = DE.THIN,
        radius = 3,
    ))

    plants.add(Patch(
        name = "beetroot",
        blocks = f"{FD}:wild_beetroots",
        density = DE.THIN,
        radius = 4,
    ))

    plants.add(Patch(
        name = "bellpepper",
        blocks = f"{RD}:wild_bell_peppers",
        density = DE.THIN,
        radius = 4,
    ))

    plants.add(Patch(
        name = "blueberry",
        blocks = BlockState(f"{UD}:blueberry_bush", {"age": 4}),
        density = DE.THICK,
        radius = 5,
    ))

    plants.add(Patch(
        name = "brownmushroom",
        blocks = BlockState(f"{FD}:brown_mushroom_colony", {"age": 3}),
        density = DE.PACKED,
        radius = 3,
    ))

    plants.add(Patch(
        name = "cabbage",
        blocks = f"{FD}:wild_cabbages",
        density = DE.THIN,
        radius = 4,
    ))

    plants.add(Patch(
        name = "carrot",
        blocks = f"{FD}:wild_carrots",
        density = DE.THIN,
        radius = 4,
    ))

    plants.add(Patch(
        name = "coffee",
        blocks = f"{RD}:wild_coffee",
        density = DE.THIN,
        radius = 5,
    ))

    plants.add(Patch(
        name = "corn",
        blocks = f"{CD}:wild_corn",
        density = DE.THICK,
        radius = 5,
    ))

    plants.add(Patch(
        name = "cotton",
        blocks = f"{CD}:wild_cotton",
        density = DE.THICK,
        radius = 6,
    ))

    plants.add(Patch(
        name = "currant",
        blocks = BlockState(f"{MC}:sweet_berry_bush", {"age": 3}),
        density = DE.THICK,
        radius = 5,
    ))

    plants.add(Patch(
        name = "cranberry",
        blocks = f"{UD}:cranberry_bush",
        density = DE.CARPET,
        immersion = IM.ADJACENT,
        radius = 4,
    ))

    plants.add(Patch(
        name = "flax",
        blocks = f"{SU}:wild_flax",
        density = DE.THICK,
        radius = 5,
    ))

    plants.add(Patch(
        name = "hamimelon",
        blocks = f"{UD}:hamimelon",
        density = DE.PACKED,
        radius = 5,
    ))

    plants.add(Patch(
        name = "hemp",
        blocks = BlockState(f"{IE}:hemp", {"half": "lower"}),
        density = DE.THICK,
        radius = 6,
    ))

    plants.add(Patch(
        name = "lemon",
        blocks = BlockState(f"{UD}:lemon_tree", {"age": 4}),
        density = DE.SPARSE,
        radius = 3,
    ))

    plants.add(Patch(
        name = "melon",
        blocks = f"{MC}:melon",
        density = DE.PACKED,
        radius = 5,
    ))

    plants.add(Patch(
        name = "onion",
        blocks = f"{FD}:wild_onions",
        density = DE.THIN,
        radius = 4,
    ))

    plants.add(Patch(
        name = "pineapple",
        blocks = BlockState(f"{UD}:pineapple", {"age": 4}),
        density = DE.SPARSE,
        radius = 4,
    ))

    plants.add(Patch(
        name = "potato",
        blocks = f"{FD}:wild_potatoes",
        density = DE.THIN,
        radius = 4,
    ))

    plants.add(Patch(
        name = "pumpkin",
        blocks = f"{MC}:pumpkin",
        density = DE.PACKED,
        radius = 5,
    ))

    plants.add(Patch(
        name = "redmushroom",
        blocks = BlockState(f"{FD}:red_mushroom_colony", {"age": 3}),
        density = DE.PACKED,
        radius = 3,
    ))

    plants.add(Patch(
        name = "rice",
        blocks = f"{FD}:wild_rice",
        density = DE.THICK,
        immersion = IM.SUBMERGED,
        radius = 7,
    ))

    plants.add(Patch(
        name = "sugarcane",
        blocks = f"{MC}:sugar_cane",
        immersion = IM.ADJACENT,
        density = DE.THICK,
        radius = 5,
    ))

    plants.add(Patch(
        name = "sunflower",
        blocks = BlockState(f"{MC}:sunflower", {"half": "lower"}),
        density = DE.THIN,
        radius = 5,
    ))

    plants.add(Patch(
        name = "tomato",
        blocks = f"{FD}:wild_tomatoes",
        density = DE.THIN,
        radius = 5,
    ))

    plants.add(Patch(
        name = "wheat",
        blocks = f"{RW}:wild_wheat",
        density = DE.THIN,
        radius = 6,
    ))


    # Flower Patches ###########################################################

    plants.add(Patch(
        name = "allium",
        blocks = f"{MC}:allium",
        density = DE.SPARSE,
        radius = 3,
    ))

    plants.add(Patch(
        name = "azurebluet",
        blocks = f"{MC}:azure_bluet",
        density = DE.THIN,
        radius = 4,
    ))

    plants.add(Patch(
        name = "blueorchid",
        blocks = f"{MC}:blue_orchid",
        density = DE.SPARSE,
        radius = 3,
    ))

    plants.add(Patch(
        name = "cornflower",
        blocks = f"{MC}:cornflower",
        density = DE.THIN,
        radius = 4,
    ))

    plants.add(Patch(
        name = "daisy",
        blocks = f"{MC}:oxeye_daisy",
        density = DE.THIN,
        radius = 4,
    ))

    plants.add(Patch(
        name = "dandelion",
        blocks = f"{MC}:dandelion",
        density = DE.CARPET,
        radius = 5,
    ))

    plants.add(Patch(
        name = "lilac",
        blocks = f"{MC}:lilac",
        density = DE.SPARSE,
        radius = 3,
    ))

    plants.add(Patch(
        name = "lily",
        blocks = f"{MC}:lily_of_the_valley",
        density = DE.THICK,
        radius = 3,
    ))

    plants.add(Patch(
        name = "peony",
        blocks = f"{MC}:peony",
        density = DE.SPARSE,
        radius = 3,
    ))

    plants.add(Patch(
        name = "poppy",
        blocks = f"{MC}:poppy",
        density = DE.THIN,
        radius = 4,
    ))

    plants.add(Patch(
        name = "rose_black",
        blocks = f"{MC}:wither_rose",
        density = DE.SPARSE,
        radius = 2,
    ))

    plants.add(Patch(
        name = "rose_bush",
        blocks = BlockState(f"{MC}:rose_bush", {"half": "lower"}),
        density = DE.SPARSE,
        radius = 3,
    ))

    plants.add(Patch(
        name = "tulip_orange",
        blocks = f"{MC}:orange_tulip",
        density = DE.THIN,
        radius = 4,
    ))

    plants.add(Patch(
        name = "tulip_pink",
        blocks = f"{MC}:pink_tulip",
        density = DE.THIN,
        radius = 4,
    ))

    plants.add(Patch(
        name = "tulip_red",
        blocks = f"{MC}:red_tulip",
        density = DE.THIN,
        radius = 4,
    ))

    plants.add(Patch(
        name = "tulip_white",
        blocks = f"{MC}:white_tulip",
        density = DE.THIN,
        radius = 4,
    ))


    # Trees ####################################################################

    plants.add(Tree(
        name = "apple",
        foliage = f"{UD}:apple_leaves",
        log = f"{MC}:oak_log",
        trunkShape = TR.STRAIGHT,
        trunkHeightMin = 3,
        trunkHeightMax = 5,
        canopyShape = CA.BLOB,
        canopyHeight = 3,
        canopyRadius = 2
    ))

    plants.add(Tree(
        name = "bayberry",
        foliage = f"{UD}:bayberry_leaves",
        log = f"{MC}:oak_log",
        trunkShape = TR.STRAIGHT,
        trunkHeightMin = 1,
        trunkHeightMax = 1,
        canopyShape = CA.BUSH,
        canopyHeight = 2,
        canopyRadius = 2
    ))

    plants.add(Tree(
        name = "durian",
        foliage = f"{UD}:durian_leaves",
        log = f"{MC}:jungle_log",
        trunkShape = TR.STRAIGHT,
        trunkHeightMin = 12,
        trunkHeightMax = 25,
        canopyShape = CA.FANCY,
        canopyHeight = 6,
        canopyRadius = 4
    ))

    plants.add(Tree(
        name = "fig",
        foliage = f"{UD}:fig_leaves",
        log = f"{MC}:acacia_log",
        trunkShape = TR.STRAIGHT,
        trunkHeightMin = 3,
        trunkHeightMax = 5,
        canopyShape = CA.BLOB,
        canopyHeight = 3,
        canopyRadius = 2
    ))

    plants.add(Tree(
        name = "hawberry",
        foliage = f"{UD}:hawberry_leaves",
        log = f"{MC}:oak_log",
        trunkShape = TR.STRAIGHT,
        trunkHeightMin = 2,
        trunkHeightMax = 7,
        canopyShape = CA.BLOB,
        canopyHeight = 3,
        canopyRadius = 2
    ))

    plants.add(Tree(
        name = "lychee",
        foliage = f"{UD}:lychee_leaves",
        log = f"{MC}:jungle_log",
        trunkShape = TR.STRAIGHT,
        trunkHeightMin = 3,
        trunkHeightMax = 7,
        canopyShape = CA.BLOB,
        canopyHeight = 3,
        canopyRadius = 2
    ))

    plants.add(Tree(
        name = "mango",
        foliage = f"{UD}:mango_leaves",
        log = f"{MC}:jungle_log",
        trunkShape = TR.FORKING,
        trunkHeightMin = 10,
        trunkHeightMax = 15,
        canopyShape = CA.ACACIA,
        canopyHeight = 5,
        canopyRadius = 4
    ))

    plants.add(Tree(
        name = "mangosteen",
        foliage = f"{UD}:mangosteen_leaves",
        log = f"{MC}:jungle_log",
        trunkShape = TR.STRAIGHT,
        trunkHeightMin = 3,
        trunkHeightMax = 12,
        canopyShape = CA.BLOB,
        canopyHeight = 3,
        canopyRadius = 3
    ))

    plants.add(Tree(
        name = "orange",
        foliage = f"{UD}:orange_leaves",
        log = f"{MC}:acacia_log",
        trunkShape = TR.STRAIGHT,
        trunkHeightMin = 3,
        trunkHeightMax = 5,
        canopyShape = CA.BLOB,
        canopyHeight = 2,
        canopyRadius = 1
    ))

    plants.add(Tree(
        name = "peach",
        foliage = f"{UD}:peach_leaves",
        log = f"{MC}:cherry_log",
        trunkShape = TR.STRAIGHT,
        trunkHeightMin = 1,
        trunkHeightMax = 2,
        canopyShape = CA.BLOB,
        canopyHeight = 2,
        canopyRadius = 1
    ))

    plants.add(Tree(
        name = "pear",
        foliage = f"{UD}:pear_leaves",
        log = f"{MC}:birch_log",
        trunkShape = TR.STRAIGHT,
        trunkHeightMin = 6,
        trunkHeightMax = 10,
        canopyShape = CA.PINE,
        canopyHeight = 4,
        canopyRadius = 2
    ))

    plants.add(Tree(
        name = "persimmon",
        foliage = f"{UD}:persimmon_leaves",
        log = f"{MC}:dark_oak_log",
        trunkShape = TR.STRAIGHT,
        trunkHeightMin = 3,
        trunkHeightMax = 9,
        canopyShape = CA.BLOB,
        canopyHeight = 4,
        canopyRadius = 2
    ))
