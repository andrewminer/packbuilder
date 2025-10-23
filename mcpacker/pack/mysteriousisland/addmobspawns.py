from mcpacker.model.ecology.biomefilter import BiomeFilter as BF
from mcpacker.model.fauna.mob import Mob
from mcpacker.model.fauna.mobcatalog import MobCatalog
from mcpacker.model.fauna.mobspawn import MobSpawn
from mcpacker.model.fauna.mobspawnbuilder import MobSpawnBuilder
from mcpacker.model.habitat import Habitat
from mcpacker.model.resourceid import ResourceId
from mcpacker.model.modpack import ModPack

import mcpacker.model.altitude as AL
import mcpacker.model.ecology.flora as FL
import mcpacker.model.ecology.geology as GE
import mcpacker.model.ecology.heat as HE
import mcpacker.model.ecology.humidity as HU
import mcpacker.model.ecology.soil as SO
import mcpacker.model.ecology.water as WA
import mcpacker.model.fauna.active as AC
import mcpacker.model.fauna.group as GR
import mcpacker.model.fauna.location as LO
import mcpacker.model.scarcity as SC
import mcpacker.model.season as SE


# Constants ########################################################################################

def addMobSpawns(pack:ModPack):
    mobs = pack.world.mobs
    b = MobSpawnBuilder(pack.world.mobSpawns)

    b.start(mobs["animalplus:raccoon"])
    b.altitude = AL.span(AL.LOWLANDS, AL.HILLS)
    b.biomeFilters = BF([(FL.CANOPY, FL.FOREST), HE.within(HE.TEMPERATE, HE.BOREAL)])
    b.seasons = SE.exclude(SE.WINTER)
    b.group = GR.merge(GR.SOLO, GR.PAIR)
    b.scarcity = SC.UNCOMMON
    b.save("raccoon-normal")

    b.seasons = SE.WINTER
    b.scarcity = SC.SPARSE
    b.save("raccoon-winter")

    b.start(mobs["animalplus:red_panda"])
    b.altitude = AL.span(AL.UPLANDS, AL.HILLS)
    b.biomeFilters = BF([ResourceId.parse("bamboo_forest")])
    b.seasons = SE.ALL
    b.group = GR.merge(GR.SOLO, GR.PAIR)
    b.scarcity = SC.SPARSE
    b.save("redpanda-normal")

    b.start(mobs["bearminimum:black_bear"])
    b.altitude = AL.span(AL.LOWLANDS, AL.ALPINE)
    b.biomeFilters = BF([HE.TEMPERATE, FL.FOREST])
    b.seasons = SE.AUTUMN
    b.group = GR.merge(GR.SOLO, GR.FAMILY)
    b.scarcity = SC.UNCOMMON
    b.save("blackbear-temperate-autumn")

    b.seasons = [SE.SPRING, SE.SUMMER]
    b.scarcity = SC.SPARSE
    b.save("blackbear-temperate-springsummer")

    b.seasons = SE.WINTER
    b.scarcity = SC.UNUSUAL
    b.save("blackbear-temperate-winter")

    b.biomeFilters = BF([HE.BOREAL, (FL.CANOPY, FL.FOREST)])
    b.seasons = SE.AUTUMN
    b.scarcity = SC.SPARSE
    b.save("blackbear-boreal-autumn")

    b.seasons = [SE.SPRING, SE.SUMMER]
    b.scarcity = SC.UNUSUAL
    b.save("blackbear-boreal-springsummer")

    b.seasons = SE.WINTER
    b.scarcity = SC.RARE
    b.save("blackbear-boreal-winter")

    b.start(mobs["minecraft:armadillo"])
    b.altitude = AL.LOWLANDS
    b.biomeFilters = BF([HE.SUBTROPICAL, HU.DRY, SO.CLAYEY])
    b.seasons = SE.SUMMER
    b.group = GR.merge(GR.SOLO, GR.PAIR)
    b.scarcity = SC.COMMON
    b.save("armadillo-lowlands-summer")

    b.altitude = AL.UPLANDS
    b.scarcity = SC.SPARSE
    b.save("armadillo-uplands-summer")

    b.altitude = AL.LOWLANDS
    b.scarcity = SC.UNCOMMON
    b.seasons = SE.exclude(SE.SUMMER)
    b.save("armadillo-lowlands-normal")

    b.altitude = AL.UPLANDS
    b.scarcity = SC.UNUSUAL
    b.save("armadillo-uplands-normal")

    b.start(mobs["minecraft:blaze"])
    b.altitude = AL.PLUTONIC
    b.location = LO.CAVE
    b.group = GR.SOLO
    b.scarcity = SC.UNCOMMON
    b.save("blaze-normal")

    b.start(mobs["bearminimum:brown_bear"])
    b.altitude = AL.span(AL.LOWLANDS, AL.ALPINE)
    b.biomeFilters = BF([HE.BOREAL, (FL.CANOPY, FL.FOREST)])
    b.seasons = SE.AUTUMN
    b.group = GR.SOLO
    b.scarcity = SC.SPARSE
    b.save("brownbear-autumn")

    b.seasons = [SE.SPRING, SE.SUMMER]
    b.scarcity = SC.UNUSUAL
    b.save("brownbear-springsummer")

    b.seasons = SE.WINTER
    b.scarcity = SC.RARE
    b.save("brownbear-winter")

    b.start(mobs["minecraft:camel"])
    b.altitude = AL.span(AL.DUNES, AL.LOWLANDS)
    b.biomeFilters = BF([HE.TROPICAL, HU.DRY, FL.BARREN, SO.SANDY])
    b.seasons = SE.DRY
    b.group = GR.FAMILY
    b.scarcity = SC.UNUSUAL
    b.save("camel-dry")

    b.seasons = SE.WET
    b.scarcity = SC.RARE
    b.save("camel-wet")

    b.start(mobs["minecraft:cave_spider"])
    b.altitude = AL.span(AL.OVERBURDEN, AL.HILLS)
    b.location = LO.CAVE
    b.group = GR.SOLO
    b.scarcity = SC.UNCOMMON
    b.save("cavespider-normal")

    b.start(mobs["cold_sweat:chameleon"])
    b.altitude = AL.span(AL.DUNES, AL.UPLANDS)
    b.biomeFilters = BF([(FL.CANOPY, FL.FOREST), HE.TROPICAL, HU.WET, WA.INLAND])
    b.seasons = SE.WET
    b.group = GR.merge(GR.SOLO, GR.FAMILY)
    b.scarcity = SC.COMMON
    b.save("chameleon-wet")

    b.seasons = SE.DRY
    b.scarcity = SC.UNCOMMON
    b.save("chameleon-dry")

    b.start(mobs["minecraft:chicken"])
    b.altitude = AL.span(AL.LOWLANDS, AL.UPLANDS)
    b.biomeFilters = BF([FL.CLEARING, HE.TROPICAL, HU.WET], [SO.FUNGAL])
    b.seasons = SE.SUMMER
    b.group = GR.TROUP
    b.scarcity = SC.COMMON
    b.save("chicken-summer")

    b.seasons = SE.exclude(SE.SUMMER)
    b.scarcity = SC.UNCOMMON
    b.save("chicken-normal")

    b.start(mobs["minecraft:cod"])
    b.altitude = AL.span(AL.SHALLOWS, AL.DEEPS)
    b.biomeFilters = BF([HE.BOREAL, WA.OCEAN])
    b.seasons = SE.ALL
    b.group = GR.HERD
    b.scarcity = SC.COMMON
    b.save("cod-normal")

    b.start(mobs["minecraft:cow"])
    b.altitude = AL.span(AL.LOWLANDS, AL.UPLANDS)
    b.biomeFilters = \
        BF([HE.within(HE.SUBTROPICAL, HE.BOREAL), [HU.DAMP, HU.DRY], FL.FIELD], [SO.FUNGAL])
    b.seasons = [SE.SPRING, SE.SUMMER]
    b.group = GR.HERD
    b.scarcity = SC.SPARSE
    b.save("cow-springsummer")

    b.altitude = AL.LOWLANDS
    b.seasons = [SE.AUTUMN, SE.WINTER]
    b.group = GR.TROUP
    b.scarcity = SC.UNUSUAL
    b.save("cow-autumnwinter")

    b.start(mobs["crabbersdelight:crab"])
    b.altitude = AL.DUNES
    b.biomeFilters = BF([WA.COAST, [HE.TROPICAL, HE.SUBTROPICAL]])
    b.seasons = SE.ALL
    b.group = GR.SOLO
    b.scarcity = SC.UNCOMMON
    b.save("crab-warm")

    b.biomeFilters = BF([WA.COAST, [HE.TEMPERATE, HE.BOREAL]])
    b.scarcity = SC.SPARSE
    b.save("crab-cool")

    b.start(mobs["minecraft:dolphin"])
    b.altitude = AL.span(AL.SURFACE, AL.DEEPS)
    b.biomeFilters = BF([WA.OCEAN, [HE.SUBTROPICAL, HE.TEMPERATE]])
    b.location = LO.WATER
    b.seasons = SE.SUMMER
    b.group = GR.FAMILY
    b.scarcity = SC.UNCOMMON
    b.save("dolphin-summer")

    b.seasons = SE.exclude(SE.SUMMER)
    b.scarcity = SC.SPARSE
    b.save("dolphin-normal")

    b.start(mobs["minecraft:donkey"])
    b.altitude = AL.span(AL.UPLANDS, AL.HILLS)
    b.biomeFilters = BF([HE.SUBTROPICAL, HU.DRY, FL.FIELD])
    b.seasons = [SE.SUMMER, SE.AUTUMN]
    b.group = GR.FAMILY
    b.scarcity = SC.SPARSE
    b.save("donkey-autumnsummer")

    b.altitude = AL.span(AL.LOWLANDS, AL.UPLANDS)
    b.seasons = [SE.WINTER, SE.SPRING]
    b.scarcity = SC.SPARSE
    b.save("donkey-springwinter")

    b.start(mobs["minecraft:fox"])
    b.altitude = AL.span(AL.LOWLANDS, AL.HILLS)
    b.biomeFilters = BF([HE.within(HE.TEMPERATE, HE.FROZEN), FL.FOREST])
    b.seasons = [SE.SPRING]
    b.group = GR.FAMILY
    b.scarcity = SC.UNCOMMON
    b.save("fox-spring")

    b.seasons = SE.exclude(SE.SPRING)
    b.group = GR.SOLO
    b.scarcity = SC.SPARSE
    b.save("fox-normal")

    b.start(mobs["minecraft:frog"])
    b.altitude = AL.span(AL.SURFACE, AL.DUNES)
    b.biomeFilters = BF([(HE.TROPICAL, HE.TEMPERATE), HU.WET, WA.SWAMP])
    b.group = GR.HERD
    b.scarcity = SC.COMMON
    b.seasons = SE.SUMMER
    b.save("frog-summer")

    b.seasons = SE.SPRING
    b.scarcity = SC.SPARSE
    b.save("frog-spring")

    b.seasons = SE.AUTUMN
    b.scarcity = SC.UNUSUAL
    b.save("frog-autumn")

    b.seasons = SE.WINTER
    b.scarcity = SC.ABSENT
    b.save("frog-winter")

    b.start(mobs["minecraft:glow_squid"])
    b.altitude = AL.ABYSS
    b.biomeFilters = BF([WA.OCEAN], [HE.FROZEN])
    b.group = GR.SOLO
    b.location = LO.WATER
    b.scarcity = SC.RARE
    b.seasons = SE.ALL
    b.save("glowsquid-normal")

    b.start(mobs["minecraft:goat"])
    b.altitude = AL.span(AL.HILLS, AL.CRAGS)
    b.biomeFilters = BF([(HE.BOREAL, HE.FROZEN), SO.ROCKY])
    b.group = GR.FAMILY
    b.scarcity = SC.UNCOMMON
    b.seasons = SE.ALL
    b.save("goat-normal")

    b.start(mobs["minecraft:horse"])
    b.altitude = AL.span(AL.DUNES, AL.LOWLANDS)
    b.biomeFilters = BF([FL.FIELD, (HE.SUBTROPICAL, HE.TEMPERATE), (SO.LOAMY, SO.PEATY, SO.SANDY)])
    b.group = GR.HERD
    b.scarcity = SC.UNUSUAL
    b.seasons = SE.ALL
    b.save("horse-normal")

    b.start(mobs["minecraft:llama"])
    b.altitude = AL.span(AL.ALPINE, AL.PEAKS)
    b.biomeFilters = BF([(HE.BOREAL, HE.FROZEN), SO.ROCKY])
    b.group = GR.HERD
    b.scarcity = SC.UNCOMMON
    b.seasons = SE.ALL
    b.save("llama-normal")

    b.start(mobs["minecraft:magma_cube"])
    b.altitude = AL.PLUTONIC
    b.location = LO.CAVE
    b.group = GR.SOLO
    b.scarcity = SC.UNCOMMON
    b.save("magmacube-normal")

    b.start(mobs["minecraft:mooshroom"])
    b.altitude = AL.span(AL.DUNES, AL.UPLANDS)
    b.biomeFilters = BF([SO.FUNGAL])
    b.group = GR.HERD
    b.scarcity = SC.UNCOMMON
    b.seasons = SE.ALL
    b.save("mooshroom-normal")

    b.start(mobs["minecraft:ocelot"])
    b.altitude = AL.span(AL.LOWLANDS, AL.HILLS)
    b.biomeFilters = BF([FL.CANOPY, HE.TROPICAL, HU.WET])
    b.group = GR.SOLO
    b.scarcity = SC.RARE
    b.seasons = SE.ALL
    b.save("ocelot-normal")

    b.start(mobs["minecraft:panda"])
    b.altitude = AL.span(AL.LOWLANDS, AL.UPLANDS)
    b.biomeFilters = BF([ResourceId.parse("bamboo_forest")])
    b.group = GR.SOLO
    b.scarcity = SC.UNUSUAL
    b.seasons = SE.exclude(SE.SPRING)
    b.save("panda-normal")

    b.group = GR.PAIR
    b.seasons = SE.SPRING
    b.save("panda-spring")

    b.start(mobs["minecraft:parrot"])
    b.altitude = AL.span(AL.DUNES, AL.HILLS)
    b.biomeFilters = BF([(FL.CANOPY, FL.FOREST), HE.TROPICAL, HU.WET])
    b.group = GR.PAIR
    b.scarcity = SC.COMMON
    b.seasons = SE.ALL
    b.save("parrot-canopyforest")

    b.biomeFilters = BF([FL.CLEARING, HE.TROPICAL, HU.WET], [SO.FUNGAL])
    b.scarcity = SC.UNCOMMON
    b.save("parrot-clearing")

    b.start(mobs["minecraft:pig"])
    b.altitude = AL.span(AL.LOWLANDS, AL.HILLS)
    b.biomeFilters = BF([
        FL.within(FL.CANOPY, FL.CLEARING),
        HE.within(HE.SUBTROPICAL, HE.TEMPERATE)
    ])
    b.group = GR.TROUP
    b.scarcity = SC.COMMON
    b.seasons = SE.SUMMER
    b.save("pig-summer")

    b.scarcity = SC.UNCOMMON
    b.seasons = SE.exclude(SE.SUMMER)
    b.save("pig-normal")

    b.start(mobs["minecraft:polar_bear"])
    b.altitude = AL.DUNES
    b.biomeFilters = BF([HE.FROZEN, (WA.COAST, WA.OCEAN)])
    b.group = GR.PAIR
    b.scarcity = SC.UNUSUAL
    b.seasons = [SE.SPRING, SE.WINTER]
    b.save("polarbear-springwinter")

    b.group = GR.SOLO
    b.seasons = [SE.SUMMER, SE.AUTUMN]
    b.scarcity = SC.RARE
    b.save("polarbear-autumnsummer")

    b.start(mobs["minecraft:pufferfish"])
    b.altitude = AL.SHALLOWS
    b.biomeFilters = BF([(HE.TEMPERATE, HE.TROPICAL), WA.OCEAN])
    b.group = GR.TROUP
    b.location = LO.WATER
    b.scarcity = SC.UNCOMMON
    b.seasons = SE.ALL
    b.save("pufferfish-normal")

    b.start(mobs["minecraft:rabbit"])
    b.altitude = AL.span(AL.DUNES, AL.ALPINE)
    b.biomeFilters = BF([
        FL.within(FL.CANOPY, FL.FIELD),
        HE.within(HE.SUBTROPICAL, HE.BOREAL),
        WA.INLAND,
    ])
    b.group = GR.FAMILY
    b.scarcity = SC.COMMON
    b.seasons = SE.SPRING
    b.save("rabbit-temperate-spring")

    b.scarcity = SC.SPARSE
    b.seasons = [SE.SUMMER, SE.AUTUMN]
    b.save("rabbit-temperate-autumnsummer")

    b.scarcity = SC.SPARSE
    b.seasons = SE.WINTER
    b.save("rabbit-temperate-winter")

    b.altitude = AL.span(AL.DUNES, AL.LOWLANDS)
    b.biomeFilters = BF([FL.BARREN, HE.TROPICAL, HU.DRY])
    b.group = GR.PAIR
    b.scarcity = SC.SPARSE
    b.seasons = SE.exclude(SE.SUMMER)
    b.save("rabbit-desert-normal")

    b.scarcity = SC.UNUSUAL
    b.seasons = SE.SUMMER
    b.save("rabbit-desert-summer")

    b.altitude = AL.span(AL.LOWLANDS, AL.UPLANDS)
    b.biomeFilters = BF([FL.within(FL.FOREST, FL.FIELD), HE.FROZEN])
    b.scarcity = SC.SPARSE
    b.seasons = SE.exclude(SE.WINTER)
    b.save("rabbit-frozen-normal")

    b.scarcity = SC.UNUSUAL
    b.seasons = SE.WINTER
    b.save("rabbit-frozen-winter")

    b.start(mobs["minecraft:salmon"])
    b.altitude = AL.span(AL.SURFACE, AL.SHALLOWS)
    b.biomeFilters = BF([WA.RIVER], [HE.FROZEN])
    b.group = GR.HERD
    b.scarcity = SC.COMMON
    b.seasons = SE.AUTUMN
    b.save("salmon-autumnrun")

    b.scarcity = SC.UNCOMMON
    b.seasons = [SE.SPRING]
    b.save("salmon-springrun")

    b.seasons = [SE.SUMMER, SE.WINTER]
    b.scarcity = SC.ABSENT
    b.save("salmon-notrunning")

    b.start(mobs["minecraft:sheep"])
    b.altitude = AL.span(AL.LOWLANDS, AL.UPLANDS)
    b.biomeFilters = BF([FL.within(FL.FOREST, FL.FIELD), HE.BOREAL])
    b.group = GR.HERD
    b.scarcity = SC.UNCOMMON
    b.seasons = SE.ALL
    b.save("sheep-normal")

    b.start(mobs["minecraft:slime"])
    b.altitude = AL.span(AL.SURFACE, AL.DUNES)
    b.biomeFilters = BF([HE.TEMPERATE, WA.SWAMP])
    b.group = GR.SOLO
    b.scarcity = SC.UNCOMMON
    b.seasons = [SE.SPRING]
    b.save("slime-spring")

    b.scarcity = SC.UNUSUAL
    b.seasons = SE.exclude(SE.SPRING)
    b.save("slime-normal")

    b.start(mobs["minecraft:spider"])
    b.altitude = AL.span(AL.LOWLANDS, AL.HILLS)
    b.biomeFilters = BF([FL.CANOPY, HE.TEMPERATE])
    b.group = GR.SOLO
    b.scarcity = SC.COMMON
    b.seasons = SE.SUMMER
    b.save("spider-summer")

    b.scarcity = SC.UNCOMMON
    b.seasons = [SE.SPRING, SE.AUTUMN]
    b.save("spider-springsummer")

    b.scarcity = SC.SPARSE
    b.seasons = SE.WINTER
    b.save("spider-winter")

    b.start(mobs["minecraft:squid"])
    b.altitude = AL.DEEPS
    b.biomeFilters = BF([WA.OCEAN], [HE.FROZEN])
    b.group = GR.SOLO
    b.location = LO.WATER
    b.scarcity = SC.SPARSE
    b.seasons = SE.ALL
    b.save("squid-normal")

    b.start(mobs["minecraft:tropical_fish"])
    b.altitude = AL.SHALLOWS
    b.biomeFilters = BF([HE.TROPICAL, WA.OCEAN])
    b.group = GR.HERD
    b.location = LO.WATER
    b.scarcity = SC.COMMON
    b.seasons = SE.ALL
    b.save("tropicalfish-normal")

    b.start(mobs["minecraft:turtle"])
    b.altitude = AL.span(AL.SURFACE, AL.SHALLOWS)
    b.biomeFilters = BF([HE.within(HE.TROPICAL, HE.SUBTROPICAL), WA.OCEAN])
    b.group = GR.SOLO
    b.scarcity = SC.SPARSE
    b.seasons = SE.ALL
    b.save("turtle-normal")

    b.altitude = AL.DUNES
    b.biomeFilters = BF([HE.within(HE.TROPICAL, HE.SUBTROPICAL), WA.COAST])
    b.group = GR.SOLO
    b.scarcity = SC.UNUSUAL
    b.save("turtle-spawning")

    b.start(mobs["minecraft:wolf"])
    b.altitude = AL.span(AL.LOWLANDS, AL.UPLANDS)
    b.biomeFilters = BF([FL.CANOPY, HE.TEMPERATE, WA.INLAND])
    b.group = GR.TROUP
    b.scarcity = SC.COMMON
    b.seasons = SE.ALL
    b.save("wolf-deepforest")

    b.biomeFilters = BF([FL.within(FL.FOREST, FL.FIELD), (HE.TEMPERATE, HE.BOREAL), WA.INLAND])
    b.scarcity = SC.UNCOMMON
    b.save("wolf-normal")

    b.biomeFilters = BF([FL.within(FL.FOREST, FL.FIELD), HE.FROZEN, WA.INLAND])
    b.scarcity = SC.UNUSUAL
    b.save("wolf-arctic")

    b.biomeFilters = BF([(FL.CLEARING, FL.FIELD), HE.SUBTROPICAL, WA.INLAND])
    b.scarcity = SC.SPARSE
    b.save("wolf-savanna")
