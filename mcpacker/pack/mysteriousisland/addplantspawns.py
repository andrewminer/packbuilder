from mcpacker.model.altitude import Altitude
from mcpacker.model.ecology.biomefilter import BiomeFilter as BF
from mcpacker.model.flora.plantspawn import PlantSpawn
from mcpacker.model.resourceid import ResourceId
from mcpacker.model.modpack import ModPack

import mcpacker.model.altitude as AL
import mcpacker.model.ecology.flora as FL
import mcpacker.model.ecology.geology as GE
import mcpacker.model.ecology.heat as HE
import mcpacker.model.ecology.humidity as HU
import mcpacker.model.ecology.soil as SO
import mcpacker.model.ecology.water as WA
import mcpacker.model.scarcity as SC


# Functions ########################################################################################

def addPlantSpawns(pack:ModPack):
    plants = pack.world.plants
    spawns = pack.world.plantSpawns

    # Crop Patches #############################################################

    spawns.add(PlantSpawn(
        plant = plants["athelas"],
        altitude = AL.span(AL.LOWLANDS, AL.HILLS),
        biomeFilters = BF([FL.CANOPY, HE.TEMPERATE]),
        scarcity = SC.SPARSE,
    ))

    spawns.add(PlantSpawn(
        plant = plants["beetroot"],
        altitude = AL.LOWLANDS,
        biomeFilters = BF([FL.FOREST, HE.BOREAL, SO.ACIDIC]),
        scarcity = SC.COMMON,
    ))

    spawns.add(PlantSpawn(
        plant = plants["bellpepper"],
        altitude = AL.LOWLANDS,
        biomeFilters = BF([FL.CLEARING, HE.TROPICAL, HU.WET, WA.INLAND]),
        scarcity = SC.COMMON,
    ))

    spawns.add(PlantSpawn(
        plant = plants["blueberry"],
        altitude = AL.span(AL.UPLANDS, AL.ALPINE),
        biomeFilters = BF([FL.within(FL.FOREST, FL.FIELD), HE.BOREAL]),
        scarcity = SC.SPARSE,
    ))

    spawns.add(PlantSpawn(
        plant = plants["brownmushroom"],
        altitude = AL.span(AL.SOIL, AL.ALPINE),
        biomeFilters = [
            BF(
                [(FL.CANOPY, FL.FOREST), (HE.TEMPERATE, HE.BOREAL), (SO.LOAMY, SO.CLAYEY)],
                [WA.OCEAN]
            ),
            BF([HU.WET], [HE.FROZEN, WA.OCEAN, WA.RIVER]),
            BF([SO.FUNGAL]),
        ],
        scarcity = SC.COMMON,
    ))

    spawns.add(PlantSpawn(
        plant = plants["cabbage"],
        altitude = AL.HILLS,
        biomeFilters = BF([(HE.SUBTROPICAL, HE.TEMPERATE), SO.SANDY, WA.COAST]),
        scarcity = SC.COMMON,
    ))

    spawns.add(PlantSpawn(
        plant = plants["carrot"],
        altitude = AL.LOWLANDS,
        biomeFilters = BF(
            [(FL.FOREST, FL.CLEARING), HE.TEMPERATE, SO.LOAMY],
            [ResourceId.parse("flower_forest")],
        ),
        scarcity = SC.COMMON,
    ))

    spawns.add(PlantSpawn(
        plant = plants["coffee"],
        altitude = AL.span(AL.HILLS, AL.ALPINE),
        biomeFilters = BF([FL.CANOPY, HE.TROPICAL, HU.WET]),
        scarcity = SC.SPARSE,
    ))

    spawns.add(PlantSpawn(
        plant = plants["corn"],
        altitude = AL.span(AL.LOWLANDS, AL.UPLANDS),
        biomeFilters = BF([FL.FIELD, HE.SUBTROPICAL, (SO.LOAMY, SO.SANDY)]),
        scarcity = SC.COMMON,
    ))

    spawns.add(PlantSpawn(
        plant = plants["cotton"],
        altitude = AL.LOWLANDS,
        biomeFilters = BF([FL.FIELD, HE.SUBTROPICAL, HU.DRY, (SO.LOAMY, SO.SANDY)]),
        scarcity = SC.UNCOMMON,
    ))

    spawns.add(PlantSpawn(
        plant = plants["currant"],
        altitude = AL.span(AL.UPLANDS, AL.ALPINE),
        biomeFilters = BF([FL.within(FL.FOREST, FL.FIELD), (HE.BOREAL, HE.FROZEN)]),
        scarcity = SC.UNCOMMON,
    ))

    spawns.add(PlantSpawn(
        plant = plants["cranberry"],
        altitude = AL.DUNES,
        biomeFilters = BF([HU.WET, SO.PEATY]),
        scarcity = SC.UNCOMMON,
    ))

    # NOTE: Due to a bug in Supplementaries, flax can *only* be planted on sand, despite the actual
    #       plant requiring an entirely different soil. Therefore, we're imaginging *this* so-called
    #       "flax" as a fiberous, desert-dwelling cousin.
    spawns.add(PlantSpawn(
        plant = plants["flax"],
        altitude = AL.DUNES,
        biomeFilters = BF([FL.BARREN, HU.DRY, SO.SANDY]),
        scarcity = SC.COMMON,
    ))

    spawns.add(PlantSpawn(
        plant = plants["hamimelon"],
        altitude = AL.span(AL.LOWLANDS, AL.UPLANDS),
        biomeFilters = BF([FL.FIELD, HE.SUBTROPICAL, HU.DRY, (SO.LOAMY, SO.SANDY)]),
        scarcity = SC.RARE,
    ))

    spawns.add(PlantSpawn(
        plant = plants["hemp"],
        altitude = AL.span(AL.DUNES, AL.UPLANDS),
        biomeFilters = BF(
            [FL.FIELD, HE.TEMPERATE, HU.DAMP, SO.LOAMY],
            [ResourceId.parse("sunflower_plains")]
        ),
        scarcity = SC.UNCOMMON,
    ))

    spawns.add(PlantSpawn(
        plant = plants["lemon"],
        altitude = AL.UPLANDS,
        biomeFilters = BF([FL.FIELD, HE.SUBTROPICAL, HU.DRY]),
        scarcity = SC.SPARSE,
    ))

    spawns.add(PlantSpawn(
        plant = plants["melon"],
        altitude = AL.LOWLANDS,
        biomeFilters = BF([FL.CLEARING, HE.TROPICAL, HU.WET], [SO.FUNGAL]),
        scarcity = SC.SPARSE,
    ))

    spawns.add(PlantSpawn(
        plant = plants["onion"],
        altitude = AL.span(AL.UPLANDS, AL.HILLS),
        biomeFilters = BF([FL.FOREST, HE.TEMPERATE, HU.DAMP, SO.ACIDIC]),
        scarcity = SC.SPARSE,
    ))

    # NOTE: Due to a bug in Fruits Delight, pineapple can *only* be planted on sand: despite this
    #       in now way reflecting the plant's actual ecology. As such, we have to imagine these as
    #       a more cactus-like cousin of actual pineapples.
    spawns.add(PlantSpawn(
        plant = plants["pineapple"],
        altitude = AL.LOWLANDS,
        biomeFilters = BF([FL.BARREN, HE.TROPICAL, HU.DRY, SO.SANDY]),
        scarcity = SC.SPARSE,
        # TODO: add sand as substrate in addplants.py
    ))

    spawns.add(PlantSpawn(
        plant = plants["potato"],
        altitude = AL.span(AL.UPLANDS, AL.HILLS),
        biomeFilters = BF([FL.FOREST, HE.BOREAL, HU.DAMP, SO.ACIDIC]),
        scarcity = SC.UNCOMMON,
    ))

    spawns.add(PlantSpawn(
        plant = plants["pumpkin"],
        altitude = AL.LOWLANDS,
        biomeFilters = BF([FL.FIELD, HE.TEMPERATE, SO.LOAMY]),
        scarcity = SC.UNUSUAL,
    ))

    spawns.add(PlantSpawn(
        plant = plants["redmushroom"],
        altitude = AL.span(AL.SOIL, AL.ALPINE),
        biomeFilters = [
            BF([(FL.CANOPY, FL.FOREST), (HE.TEMPERATE, HE.BOREAL), (SO.LOAMY, SO.CLAYEY)]),
            BF([HU.WET], [HE.FROZEN, WA.OCEAN, WA.RIVER]),
            BF([SO.FUNGAL]),
        ],
        scarcity = SC.UNCOMMON,
    ))

    spawns.add(PlantSpawn(
        plant = plants["rice"],
        altitude = AL.SURFACE,
        biomeFilters = BF([(HE.SUBTROPICAL, HE.TEMPERATE), (WA.RIVER, WA.SWAMP)]),
        scarcity = SC.COMMON,
    ))

    spawns.add(PlantSpawn(
        plant = plants["sugarcane"],
        altitude = AL.DUNES,
        biomeFilters = BF([(HE.TROPICAL, HE.TEMPERATE), (WA.RIVER, WA.SWAMP)]),
        scarcity = SC.COMMON,
    ))

    spawns.add(PlantSpawn(
        plant = plants["sunflower"],
        altitude = AL.span(AL.LOWLANDS, AL.UPLANDS),
        biomeFilters = BF([ResourceId.parse("sunflower_plains")]),
        scarcity = SC.CARPET,
    ))

    spawns.add(PlantSpawn(
        plant = plants["tomato"],
        altitude = AL.span(AL.UPLANDS, AL.HILLS),
        biomeFilters = BF([FL.CLEARING, HE.TROPICAL, HU.WET], [SO.FUNGAL]),
        scarcity = SC.UNCOMMON,
    ))

    spawns.add(PlantSpawn(
        plant = plants["wheat"],
        altitude = AL.span(AL.LOWLANDS, AL.UPLANDS),
        biomeFilters = BF([FL.FIELD, HE.TEMPERATE, HU.DAMP, SO.LOAMY]),
        scarcity = SC.COMMON,
    ))

    # Flower Patches ###########################################################

    spawns.add(PlantSpawn(
        plant = plants["allium"],
        altitude = AL.span(AL.UPLANDS, AL.HILLS),
        biomeFilters = BF([FL.FOREST, HE.TEMPERATE, HU.DAMP, SO.ACIDIC]),
        scarcity = SC.UNCOMMON,
    ))

    spawns.add(PlantSpawn(
        plant = plants["azurebluet"],
        altitude = AL.span(AL.UPLANDS, AL.ALPINE),
        biomeFilters = BF([FL.FIELD, (HE.TEMPERATE, HE.BOREAL), HU.DAMP, (SO.LOAMY, SO.PEATY)]),
        scarcity = SC.SPARSE,
    ))

    spawns.add(PlantSpawn(
        plant = plants["blueorchid"],
        altitude = AL.span(AL.LOWLANDS, AL.UPLANDS),
        biomeFilters = BF([FL.CANOPY, HE.TROPICAL, HU.WET]),
        scarcity = SC.RARE,
    ))

    spawns.add(PlantSpawn(
        plant = plants["cornflower"],
        altitude = AL.span(AL.UPLANDS, AL.ALPINE),
        biomeFilters = BF([FL.FIELD, HE.TEMPERATE, (SO.LOAMY, SO.PEATY)]),
        scarcity = SC.COMMON,
    ))

    spawns.add(PlantSpawn(
        plant = plants["daisy"],
        altitude = AL.span(AL.UPLANDS, AL.ALPINE),
        biomeFilters = BF([FL.FIELD, (HE.TEMPERATE, HE.BOREAL)]),
        scarcity = SC.UNCOMMON,
    ))

    spawns.add(PlantSpawn(
        plant = plants["dandelion"],
        altitude = AL.span(AL.DUNES, AL.HILLS),
        biomeFilters = BF(
            [(FL.CLEARING, FL.FIELD)],
            [HE.FROZEN, HU.WET, SO.FUNGAL, SO.ROCKY, ResourceId.parse("flower_forest")]),
        scarcity = SC.COMMON,
    ))

    spawns.add(PlantSpawn(
        plant = plants["lilac"],
        altitude = AL.LOWLANDS,
        biomeFilters = BF([FL.FOREST, HE.TEMPERATE, HU.DAMP, SO.LOAMY]),
        scarcity = SC.UNUSUAL,
    ))

    spawns.add(PlantSpawn(
        plant = plants["lily"],
        altitude = AL.span(AL.LOWLANDS, AL.UPLANDS),
        biomeFilters = BF([FL.FOREST, (HE.TEMPERATE, HE.BOREAL), HU.DAMP, SO.ACIDIC]),
        scarcity = SC.RARE,
    ))

    spawns.add(PlantSpawn(
        plant = plants["peony"],
        altitude = AL.LOWLANDS,
        biomeFilters = BF([FL.CLEARING, HE.TEMPERATE, HU.DAMP, SO.ROCKY]),
        scarcity = SC.SPARSE,
    ))

    spawns.add(PlantSpawn(
        plant = plants["poppy"],
        altitude = AL.span(AL.DUNES, AL.UPLANDS),
        biomeFilters = BF(
            [FL.FIELD, (HE.SUBTROPICAL, HE.TEMPERATE), (HU.DRY, HU.DAMP)],
            [SO.FUNGAL]
        ),
        scarcity = SC.SPARSE,
    ))

    spawns.add(PlantSpawn(
        plant = plants["rose_black"],
        altitude = AL.HILLS,
        biomeFilters = BF([FL.CANOPY, HE.TEMPERATE]),
        scarcity = SC.RARE,
    ))

    spawns.add(PlantSpawn(
        plant = plants["rose_bush"],
        altitude = AL.span(AL.UPLANDS, AL.ALPINE),
        biomeFilters = BF([FL.FOREST, (HE.TEMPERATE, HE.BOREAL), SO.LOAMY]),
        scarcity = SC.UNUSUAL,
    ))

    spawns.add(PlantSpawn(
        plant = plants["tulip_orange"],
        altitude = AL.span(AL.DUNES, AL.LOWLANDS),
        biomeFilters = BF([ResourceId.parse("flower_forest")]),
        scarcity = SC.UNUSUAL,
    ))

    spawns.add(PlantSpawn(
        plant = plants["tulip_pink"],
        altitude = AL.span(AL.DUNES, AL.LOWLANDS),
        biomeFilters = BF([ResourceId.parse("flower_forest")]),
        scarcity = SC.SPARSE,
    ))

    spawns.add(PlantSpawn(
        plant = plants["tulip_red"],
        altitude = AL.span(AL.DUNES, AL.LOWLANDS),
        biomeFilters = BF([ResourceId.parse("flower_forest")]),
        scarcity = SC.COMMON,
    ))

    spawns.add(PlantSpawn(
        plant = plants["tulip_white"],
        altitude = AL.span(AL.DUNES, AL.LOWLANDS),
        biomeFilters = BF([ResourceId.parse("flower_forest")]),
        scarcity = SC.UNCOMMON,
    ))

    # Trees ####################################################################

    spawns.add(PlantSpawn(
        plant = plants["apple"],
        altitude = AL.span(AL.LOWLANDS, AL.UPLANDS),
        biomeFilters = BF(
            [(FL.FOREST, FL.CLEARING), HE.TEMPERATE, SO.LOAMY],
            [ResourceId.parse("flower_forest")],
        ),
        scarcity = SC.SPARSE,
    ))

    spawns.add(PlantSpawn(
        plant = plants["bayberry"],
        altitude = AL.span(AL.DUNES, AL.UPLANDS),
        biomeFilters = BF([HE.TEMPERATE, (SO.ROCKY, SO.SANDY), WA.COAST]),
        scarcity = SC.SPARSE,
    ))

    spawns.add(PlantSpawn(
        plant = plants["durian"],
        altitude = AL.HILLS,
        biomeFilters = BF([FL.within(FL.CANOPY, FL.CLEARING), HE.TROPICAL, HU.WET, SO.ACIDIC]),
        scarcity = SC.UNUSUAL,
    ))

    spawns.add(PlantSpawn(
        plant = plants["fig"],
        altitude = AL.span(AL.UPLANDS, AL.HILLS),
        biomeFilters = BF([HE.SUBTROPICAL, HU.DRY, SO.SANDY], [FL.BARREN]),
        scarcity = SC.UNCOMMON,
    ))

    spawns.add(PlantSpawn(
        plant = plants["hawberry"],
        altitude = AL.span(AL.UPLANDS, AL.HILLS),
        biomeFilters = BF([(FL.FOREST, FL.CLEARING), HE.TEMPERATE, (SO.ACIDIC, SO.LOAMY)]),
        scarcity = SC.SPARSE,
    ))

    spawns.add(PlantSpawn(
        plant = plants["lychee"],
        altitude = AL.UPLANDS,
        biomeFilters = BF([FL.CLEARING, HE.TROPICAL, HU.WET], [SO.FUNGAL]),
        scarcity = SC.SPARSE,
    ))

    spawns.add(PlantSpawn(
        plant = plants["mango"],
        altitude = AL.LOWLANDS,
        biomeFilters = BF(
            [FL.within(FL.CANOPY, FL.CLEARING), HE.TROPICAL, (HU.DAMP, HU.WET), SO.ACIDIC]
        ),
        scarcity = SC.UNCOMMON,
    ))

    spawns.add(PlantSpawn(
        plant = plants["mangosteen"],
        altitude = AL.UPLANDS,
        biomeFilters = BF([FL.CANOPY, HE.TROPICAL, HU.WET, SO.ACIDIC]),
        scarcity = SC.UNUSUAL,
    ))

    spawns.add(PlantSpawn(
        plant = plants["orange"],
        altitude = AL.LOWLANDS,
        biomeFilters = BF([FL.FIELD, HE.SUBTROPICAL, HU.DRY]),
        scarcity = SC.SPARSE,
    ))

    spawns.add(PlantSpawn(
        plant = plants["peach"],
        altitude = AL.span(AL.LOWLANDS, AL.UPLANDS),
        biomeFilters = BF([FL.CLEARING, HE.TEMPERATE, HU.DAMP, SO.ROCKY]),
        scarcity = SC.UNCOMMON,
    ))

    spawns.add(PlantSpawn(
        plant = plants["pear"],
        altitude = AL.span(AL.LOWLANDS, AL.UPLANDS),
        biomeFilters = BF([FL.CLEARING, HE.TEMPERATE, HU.DAMP, (SO.ACIDIC, SO.LOAMY)]),
        scarcity = SC.UNCOMMON,
    ))

    spawns.add(PlantSpawn(
        plant = plants["persimmon"],
        altitude = AL.span(AL.LOWLANDS, AL.UPLANDS),
        biomeFilters = BF([FL.FOREST, HE.TEMPERATE, SO.LOAMY]),
        scarcity = SC.UNCOMMON,
    ))
