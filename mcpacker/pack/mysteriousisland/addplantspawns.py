from mcpacker.model.altitude import Altitude
from mcpacker.model.ecology.biomefilter import BiomeFilter as BF
from mcpacker.model.flora.plantspawn import PlantSpawn
from mcpacker.model.flora.plantspawnbuilder import PlantSpawnBuilder
from mcpacker.model.modpack import ModPack
from mcpacker.model.resourceid import ResourceId

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
    b = PlantSpawnBuilder(pack.world.plantSpawns)

    # Crop Patches #############################################################

    b.start(plants["athelas"])
    b.altitude = AL.span(AL.LOWLANDS, AL.HILLS)
    b.biomeFilters = BF([FL.CANOPY, HE.TEMPERATE])
    b.scarcity = SC.SPARSE
    b.save("")

    b.start(plants["beetroot"])
    b.altitude = AL.LOWLANDS
    b.biomeFilters = BF([FL.FOREST, HE.BOREAL, SO.ACIDIC])
    b.scarcity = SC.COMMON
    b.save("")

    b.start(plants["bellpepper"])
    b.altitude = AL.LOWLANDS
    b.biomeFilters = BF([FL.CLEARING, HE.TROPICAL, HU.WET, WA.INLAND])
    b.scarcity = SC.COMMON
    b.save("")

    b.start(plants["blueberry"])
    b.altitude = AL.span(AL.UPLANDS, AL.ALPINE)
    b.biomeFilters = BF([FL.within(FL.FOREST, FL.FIELD), HE.BOREAL])
    b.scarcity = SC.SPARSE
    b.save("")

    b.start(plants["brownmushroom"])
    b.altitude = AL.span(AL.SOIL, AL.ALPINE)
    b.biomeFilters = [
        BF([(FL.CANOPY, FL.FOREST), (HE.TEMPERATE, HE.BOREAL), (SO.LOAMY, SO.CLAYEY)], [WA.OCEAN]),
        BF([HU.WET], [HE.FROZEN, WA.OCEAN, WA.RIVER]),
        BF([SO.FUNGAL]),
    ]
    b.scarcity = SC.COMMON
    b.save("")

    b.start(plants["cabbage"])
    b.altitude = AL.HILLS
    b.biomeFilters = BF([(HE.SUBTROPICAL, HE.TEMPERATE), SO.SANDY, WA.COAST])
    b.scarcity = SC.COMMON
    b.save("")

    b.start(plants["carrot"])
    b.altitude = AL.LOWLANDS
    b.biomeFilters = BF(
        [(FL.FOREST, FL.CLEARING), HE.TEMPERATE, SO.LOAMY], [ResourceId.parse("flower_forest")],
    )
    b.scarcity = SC.COMMON
    b.save("")

    b.start(plants["coffee"])
    b.altitude = AL.span(AL.HILLS, AL.ALPINE)
    b.biomeFilters = BF([FL.CANOPY, HE.TROPICAL, HU.WET])
    b.scarcity = SC.SPARSE
    b.save("")

    b.start(plants["corn"])
    b.altitude = AL.span(AL.LOWLANDS, AL.UPLANDS)
    b.biomeFilters = BF([FL.FIELD, HE.SUBTROPICAL, (SO.LOAMY, SO.SANDY)])
    b.scarcity = SC.COMMON
    b.save("")

    b.start(plants["cotton"])
    b.altitude = AL.LOWLANDS
    b.biomeFilters = BF([FL.FIELD, HE.SUBTROPICAL, HU.DRY, (SO.LOAMY, SO.SANDY)])
    b.scarcity = SC.UNCOMMON
    b.save("")

    b.start(plants["currant"])
    b.altitude = AL.span(AL.UPLANDS, AL.ALPINE)
    b.biomeFilters = BF([FL.within(FL.FOREST, FL.FIELD), (HE.BOREAL, HE.FROZEN)])
    b.scarcity = SC.UNCOMMON
    b.save("")

    b.start(plants["cranberry"])
    b.altitude = AL.DUNES
    b.biomeFilters = BF([HU.WET, SO.PEATY])
    b.scarcity = SC.UNCOMMON
    b.save("")

    # NOTE: Due to a bug in Supplementaries, flax can *only* be planted on sand, despite the actual
    #       plant requiring an entirely different soil. Therefore, we're imaginging *this* so-called
    #       "flax" as a fiberous, desert-dwelling cousin.
    b.start(plants["flax"])
    b.altitude = AL.DUNES
    b.biomeFilters = BF([FL.BARREN, HU.DRY, SO.SANDY])
    b.scarcity = SC.COMMON
    b.save("")

    b.start(plants["hamimelon"])
    b.altitude = AL.span(AL.LOWLANDS, AL.UPLANDS)
    b.biomeFilters = BF([FL.FIELD, HE.SUBTROPICAL, HU.DRY, (SO.LOAMY, SO.SANDY)])
    b.scarcity = SC.RARE
    b.save("")

    b.start(plants["hemp"])
    b.altitude = AL.span(AL.DUNES, AL.UPLANDS)
    b.biomeFilters = BF(
        [FL.FIELD, HE.TEMPERATE, HU.DAMP, SO.LOAMY], [ResourceId.parse("sunflower_plains")]
    ),
    b.scarcity = SC.UNCOMMON
    b.save("")

    b.start(plants["lemon"])
    b.altitude = AL.UPLANDS
    b.biomeFilters = BF([FL.FIELD, HE.SUBTROPICAL, HU.DRY])
    b.scarcity = SC.SPARSE
    b.save("")

    b.start(plants["melon"])
    b.altitude = AL.LOWLANDS
    b.biomeFilters = BF([FL.CLEARING, HE.TROPICAL, HU.WET], [SO.FUNGAL])
    b.scarcity = SC.SPARSE
    b.save("")

    b.start(plants["onion"])
    b.altitude = AL.span(AL.UPLANDS, AL.HILLS)
    b.biomeFilters = BF([FL.FOREST, HE.TEMPERATE, HU.DAMP, SO.ACIDIC])
    b.scarcity = SC.SPARSE
    b.save("")

    # NOTE: Due to a bug in Fruits Delight, pineapple can *only* be planted on sand: despite this
    #       in now way reflecting the plant's actual ecology. As such, we have to imagine these as
    #       a more cactus-like cousin of actual pineapples.
    b.start(plants["pineapple"])
    b.altitude = AL.LOWLANDS
    b.biomeFilters = BF([FL.BARREN, HE.TROPICAL, HU.DRY, SO.SANDY])
    b.scarcity = SC.SPARSE
    # TODO: add sand as substrate in addplants.py
    b.save("")

    b.start(plants["potato"])
    b.altitude = AL.span(AL.UPLANDS, AL.HILLS)
    b.biomeFilters = BF([FL.FOREST, HE.BOREAL, HU.DAMP, SO.ACIDIC])
    b.scarcity = SC.UNCOMMON
    b.save("")

    b.start(plants["pumpkin"])
    b.altitude = AL.LOWLANDS
    b.biomeFilters = BF([FL.FIELD, HE.TEMPERATE, SO.LOAMY])
    b.scarcity = SC.UNUSUAL
    b.save("")

    b.start(plants["redmushroom"])
    b.altitude = AL.span(AL.SOIL, AL.ALPINE)
    b.biomeFilters = [
        BF([(FL.CANOPY, FL.FOREST), (HE.TEMPERATE, HE.BOREAL), (SO.LOAMY, SO.CLAYEY)]),
        BF([HU.WET], [HE.FROZEN, WA.OCEAN, WA.RIVER]),
        BF([SO.FUNGAL]),
    ]
    b.scarcity = SC.UNCOMMON
    b.save("")

    b.start(plants["rice"])
    b.altitude = AL.SURFACE
    b.biomeFilters = BF([(HE.SUBTROPICAL, HE.TEMPERATE), (WA.RIVER, WA.SWAMP)])
    b.scarcity = SC.COMMON
    b.save("")

    b.start(plants["sugarcane"])
    b.altitude = AL.DUNES
    b.biomeFilters = BF([(HE.TROPICAL, HE.TEMPERATE), (WA.RIVER, WA.SWAMP)])
    b.scarcity = SC.COMMON
    b.save("")

    b.start(plants["sunflower"])
    b.altitude = AL.span(AL.LOWLANDS, AL.UPLANDS)
    b.biomeFilters = BF([ResourceId.parse("sunflower_plains")])
    b.scarcity = SC.CARPET
    b.save("")

    b.start(plants["tomato"])
    b.altitude = AL.span(AL.UPLANDS, AL.HILLS)
    b.biomeFilters = BF([FL.CLEARING, HE.TROPICAL, HU.WET], [SO.FUNGAL])
    b.scarcity = SC.UNCOMMON
    b.save("")

    b.start(plants["wheat"])
    b.altitude = AL.span(AL.LOWLANDS, AL.UPLANDS)
    b.biomeFilters = BF([FL.FIELD, HE.TEMPERATE, HU.DAMP, SO.LOAMY])
    b.scarcity = SC.COMMON
    b.save("")

    # Flower Patches ###########################################################

    b.start(plants["allium"])
    b.altitude = AL.span(AL.UPLANDS, AL.HILLS)
    b.biomeFilters = BF([FL.FOREST, HE.TEMPERATE, HU.DAMP, SO.ACIDIC])
    b.scarcity = SC.UNCOMMON
    b.save("")

    b.start(plants["azurebluet"])
    b.altitude = AL.span(AL.UPLANDS, AL.ALPINE)
    b.biomeFilters = BF([FL.FIELD, (HE.TEMPERATE, HE.BOREAL), HU.DAMP, (SO.LOAMY, SO.PEATY)])
    b.scarcity = SC.SPARSE
    b.save("")

    b.start(plants["blueorchid"])
    b.altitude = AL.span(AL.LOWLANDS, AL.UPLANDS)
    b.biomeFilters = BF([FL.CANOPY, HE.TROPICAL, HU.WET])
    b.scarcity = SC.RARE
    b.save("")

    b.start(plants["cornflower"])
    b.altitude = AL.span(AL.UPLANDS, AL.ALPINE)
    b.biomeFilters = BF([FL.FIELD, HE.TEMPERATE, (SO.LOAMY, SO.PEATY)])
    b.scarcity = SC.COMMON
    b.save("")

    b.start(plants["daisy"])
    b.altitude = AL.span(AL.UPLANDS, AL.ALPINE)
    b.biomeFilters = BF([FL.FIELD, (HE.TEMPERATE, HE.BOREAL)])
    b.scarcity = SC.UNCOMMON
    b.save("")

    b.start(plants["dandelion"])
    b.altitude = AL.span(AL.DUNES, AL.HILLS)
    b.biomeFilters = BF(
        [(FL.CLEARING, FL.FIELD)],
        [HE.FROZEN, HU.WET, SO.FUNGAL, SO.ROCKY, ResourceId.parse("flower_forest")]
    )
    b.scarcity = SC.COMMON
    b.save("")

    b.start(plants["lilac"])
    b.altitude = AL.LOWLANDS
    b.biomeFilters = BF([FL.FOREST, HE.TEMPERATE, HU.DAMP, SO.LOAMY])
    b.scarcity = SC.UNUSUAL
    b.save("")

    b.start(plants["lily"])
    b.altitude = AL.span(AL.LOWLANDS, AL.UPLANDS)
    b.biomeFilters = BF([FL.FOREST, (HE.TEMPERATE, HE.BOREAL), HU.DAMP, SO.ACIDIC])
    b.scarcity = SC.RARE
    b.save("")

    b.start(plants["peony"])
    b.altitude = AL.LOWLANDS
    b.biomeFilters = BF([FL.CLEARING, HE.TEMPERATE, HU.DAMP, SO.ROCKY])
    b.scarcity = SC.SPARSE
    b.save("")

    b.start(plants["poppy"])
    b.altitude = AL.span(AL.DUNES, AL.UPLANDS)
    b.biomeFilters = BF(
        [FL.FIELD, (HE.SUBTROPICAL, HE.TEMPERATE), (HU.DRY, HU.DAMP)],
        [SO.FUNGAL]
    ),
    b.scarcity = SC.SPARSE
    b.save("")

    b.start(plants["rose_black"])
    b.altitude = AL.HILLS
    b.biomeFilters = BF([FL.CANOPY, HE.TEMPERATE])
    b.scarcity = SC.RARE
    b.save("")

    b.start(plants["rose_bush"])
    b.altitude = AL.span(AL.UPLANDS, AL.ALPINE)
    b.biomeFilters = BF([FL.FOREST, (HE.TEMPERATE, HE.BOREAL), SO.LOAMY])
    b.scarcity = SC.UNUSUAL
    b.save("")

    b.start(plants["tulip_orange"])
    b.altitude = AL.span(AL.DUNES, AL.LOWLANDS)
    b.biomeFilters = BF([ResourceId.parse("flower_forest")])
    b.scarcity = SC.UNUSUAL
    b.save("")

    b.start(plants["tulip_pink"])
    b.altitude = AL.span(AL.DUNES, AL.LOWLANDS)
    b.biomeFilters = BF([ResourceId.parse("flower_forest")])
    b.scarcity = SC.SPARSE
    b.save("")

    b.start(plants["tulip_red"])
    b.altitude = AL.span(AL.DUNES, AL.LOWLANDS)
    b.biomeFilters = BF([ResourceId.parse("flower_forest")])
    b.scarcity = SC.COMMON
    b.save("")

    b.start(plants["tulip_white"])
    b.altitude = AL.span(AL.DUNES, AL.LOWLANDS)
    b.biomeFilters = BF([ResourceId.parse("flower_forest")])
    b.scarcity = SC.UNCOMMON
    b.save("")

    # Trees ####################################################################

    b.start(plants["apple"])
    b.altitude = AL.span(AL.LOWLANDS, AL.UPLANDS)
    b.biomeFilters = BF(
        [(FL.FOREST, FL.CLEARING), HE.TEMPERATE, SO.LOAMY],
        [ResourceId.parse("flower_forest")],
    )
    b.scarcity = SC.SPARSE
    b.save("")

    b.start(plants["bayberry"])
    b.altitude = AL.span(AL.DUNES, AL.UPLANDS)
    b.biomeFilters = BF([HE.TEMPERATE, (SO.ROCKY, SO.SANDY), WA.COAST])
    b.scarcity = SC.SPARSE
    b.save("")

    b.start(plants["durian"])
    b.altitude = AL.HILLS
    b.biomeFilters = BF([FL.within(FL.CANOPY, FL.CLEARING), HE.TROPICAL, HU.WET, SO.ACIDIC])
    b.scarcity = SC.UNUSUAL
    b.save("")

    b.start(plants["fig"])
    b.altitude = AL.span(AL.UPLANDS, AL.HILLS)
    b.biomeFilters = BF([HE.SUBTROPICAL, HU.DRY, SO.SANDY], [FL.BARREN])
    b.scarcity = SC.UNCOMMON
    b.save("")

    b.start(plants["hawberry"])
    b.altitude = AL.span(AL.UPLANDS, AL.HILLS)
    b.biomeFilters = BF([(FL.FOREST, FL.CLEARING), HE.TEMPERATE, (SO.ACIDIC, SO.LOAMY)])
    b.scarcity = SC.SPARSE
    b.save("")

    b.start(plants["lychee"])
    b.altitude = AL.UPLANDS
    b.biomeFilters = BF([FL.CLEARING, HE.TROPICAL, HU.WET], [SO.FUNGAL])
    b.scarcity = SC.SPARSE
    b.save("")

    b.start(plants["mango"])
    b.altitude = AL.LOWLANDS
    b.biomeFilters = BF(
        [FL.within(FL.CANOPY, FL.CLEARING), HE.TROPICAL, (HU.DAMP, HU.WET), SO.ACIDIC]
    )
    b.scarcity = SC.UNCOMMON
    b.save("")

    b.start(plants["mangosteen"])
    b.altitude = AL.UPLANDS
    b.biomeFilters = BF([FL.CANOPY, HE.TROPICAL, HU.WET, SO.ACIDIC])
    b.scarcity = SC.UNUSUAL
    b.save("")

    b.start(plants["orange"])
    b.altitude = AL.LOWLANDS
    b.biomeFilters = BF([FL.FIELD, HE.SUBTROPICAL, HU.DRY])
    b.scarcity = SC.SPARSE
    b.save("")

    b.start(plants["peach"])
    b.altitude = AL.span(AL.LOWLANDS, AL.UPLANDS)
    b.biomeFilters = BF([FL.CLEARING, HE.TEMPERATE, HU.DAMP, SO.ROCKY])
    b.scarcity = SC.UNCOMMON
    b.save("")

    b.start(plants["pear"])
    b.altitude = AL.span(AL.LOWLANDS, AL.UPLANDS)
    b.biomeFilters = BF([FL.CLEARING, HE.TEMPERATE, HU.DAMP, (SO.ACIDIC, SO.LOAMY)])
    b.scarcity = SC.UNCOMMON
    b.save("")

    b.start(plants["persimmon"])
    b.altitude = AL.span(AL.LOWLANDS, AL.UPLANDS)
    b.biomeFilters = BF([FL.FOREST, HE.TEMPERATE, SO.LOAMY])
    b.scarcity = SC.UNCOMMON
    b.save("")
