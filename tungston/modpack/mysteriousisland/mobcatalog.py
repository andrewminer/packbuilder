from tungston.core.ecology.biomefilter import BiomeFilter as BF
from tungston.core.fauna.mob import Mob
from tungston.core.fauna.mobplacement import MobPlacement
from tungston.core.fauna.mobcatalog import MobCatalog

import tungston.core.active           as AC
import tungston.core.altitude         as AL
import tungston.core.ecology.flora    as FL
import tungston.core.ecology.geology  as GE
import tungston.core.ecology.heat     as HE
import tungston.core.ecology.humidity as HU
import tungston.core.ecology.soil     as SO
import tungston.core.ecology.water    as WA
import tungston.core.fauna.group      as GR
import tungston.core.fauna.location   as LO
import tungston.core.scarcity         as SC
import tungston.core.season           as SE


# Constants ########################################################################################

CATALOG = MobCatalog([
    MobPlacement(Mob("armadillo", "minecraft:armadillo", AC.NOCTURNAL),
        Habitat(
            altitude    = AL.LOWLANDS,
            biomeFilter = BF([HE.SUBTROPICAL, HU.DRY]),
            seasons     = SE.SUMMER,
            group       = GR.merge(GR.SOLO, GR.PAIR),
            scarcity    = SC.COMMON
        ).derive(
            altitude = AL.UPLANDS, scarcity = SC.SPARSE,
        ).derive(
            altitude = AL.LOWLANDS, SE.excluding(SE.SUMMER), scarcity = SC.UNCOMMON,
        ).derive(
            altitude = AL.UPLANDS, scarcity = SC.UNUSUAL,
        )
    ),
    MobPlacement(Mob("black_bear", "bearminimum:black_bear"),
        Habitat(
            altitudes = AL.span(AL.LOWLANDS, AL.ALPINE),
            biomeFilter = BF([HE.TEMPERATE, FL.FOREST]),
            seasons = SE.AUTUMN,
            group = GR.merge(GR.SOLO, GR.FAMILY),
            scarcity = SC.UNCOMMON,
        ).derive(
            seasons = [SE.SPRING, SE.SUMMER], scarcity = SC.SPARSE
        ).derive(
            seasons = SE.WINTER, scarcity = SC.UNUSUAL
        ).derive(
            biomeFilter = BF([HE.BOREAL, (HE.CANOPY, HE.FOREST)]),
            seasons = SE.AUTUMN,
            scarcity = SC.SPARSE
        ).derive(
            seasons = [SE.SPRING, SE.SUMMER], scarcity = SC.UNUSUAL
        ).derive(
            seasons = SE.WINTER, scarcity = SC.RARE
        )
    ),
    MobPlacement(Mob("blaze", "minecraft:blaze"),
        Habitat(
            altitudes = AL.PLUTONIC,
            location  = LO.CAVE,
            group     = GR.SOLO,
            scarcity  = SC.UNCOMMON
        )
    ),
    MobPlacement(Mob("bogged", "minecraft:bogged")),
    MobPlacement(Mob("brown_bear", "bearminimum:brown_bear")
        Habitat(
            altitudes   = AL.span(AL.LOWLANDS, AL.ALPINE),
            biomeFilter = BF([HE.BOREAL, (FL.CANOPY, FL.FOREST)]),
            seasons     = SE.AUTUMN,
            group       = GR.SOLO,
            scarcity    = SC.SPARSE
        ).derive(
            seasons = [SE.SPRING, SE.SUMMER], scarcity = SC.UNUSUAL
        ).derive(
            seasons = SE.WINTER, scarcity = SC.RARE
        )
    ),
    MobPlacement(Mob("bulwark", "immersiveengineering:bulwark")),
    MobPlacement(Mob("camel", "minecraft:camel", AC.CREPUSCULAR),
        Habitat(
            altitudes = AL.span(AL.DUNES, AL.LOWLANDS),
            biomeFilter = BF([HE.TROPICAL, HU.DRY, FL.BARREN, SO.SANDY]),
            seasons = SE.WET,
            group = GR.FAMILY,
            scarcity = SC.UNUSUAL,
        ).derive(
            seasons = SE.DRY, scarcity = SC.RARE
        )
    ),
    MobPlacement(Mob("cat", "minecraft:cat")),
    MobPlacement(Mob("cave_spider", "minecraft:cave_spider"),
        Habitat(
            altitudes = AL.SPAN(AL.OVERBURDEN, AL.HILLS),
            location  = LO.CAVE,
            group     = GR.SOLO,
            scarcity  = SC.UNCOMMON
        )
    ),
    MobPlacement(Mob("chameleon", "cold_sweat:chameleon"),
        Habitat(
            altitudes = AL.span(AL.DUNES, AL.UPLANDS),
            biomeFilters = BF([HE.TROPICAL, HU.WET, [FL.CANOPY, FL.FOREST]]),
            seasons = SE.WET,
            groups = GR.merge(GR.SOLO, GR.FAMILY),
            scarcity = SC.COMMON,
        ).derive(
            seasons = SE.DRY, scarcity = SC.UNCOMMON,
        ).derive(
            biomeFilters = BF([HE.TROPICAL, HU.WET, FL.CLEARING]),
            seasons = SE.WET,
            scarcity = SC.UNCOMMON
        ).derive(
            seasons = SE.DRY, scarcity = SC.SPARSE,
        )
    ),
    MobPlacement(Mob("chicken", "minecraft:chicken")
        Habitat(
            altitudes = AL.span(AL.LOWLANDS, AL.UPLANDS),
            biomeFilters = BF([HE.TROPICAL, HU.WET, FL.within(FL.CANOPY, FL.CLEARING)]),
            seasons = SE.SUMMER,
            groups = GR.TROUP,
            scarcity.COMMON,
        ).derive(
            seasons = SE.excluding(SE.SUMMER), scarcity = SC.UNCOMMON
        )
    ),
    MobPlacement(Mob("cod", "minecraft:cod")),
    MobPlacement(Mob("commando", "immersiveengineering:commando")),
    MobPlacement(Mob("cow", "minecraft:cow")),
    MobPlacement(Mob("crab", "crabbersdelight:crab")),
    MobPlacement(Mob("creeper", "minecraft:creeper")),
    MobPlacement(Mob("dolphin", "minecraft:dolphin")),
    MobPlacement(Mob("donkey", "minecraft:donkey")),
    MobPlacement(Mob("drowned", "minecraft:drowned")),
    MobPlacement(Mob("enderman", "minecraft:enderman")),
    MobPlacement(Mob("evoker", "minecraft:evoker")),
    MobPlacement(Mob("fox", "minecraft:fox")),
    MobPlacement(Mob("frog", "minecraft:frog")),
    MobPlacement(Mob("fusilier", "immersiveengineering:fusilier")),
    MobPlacement(Mob("glow_squid", "minecraft:glow_squid")),
    MobPlacement(Mob("goat", "minecraft:goat")),
    MobPlacement(Mob("hoglin", "minecraft:hoglin")),
    MobPlacement(Mob("horse", "minecraft:horse")),
    MobPlacement(Mob("husk", "minecraft:husk")),
    MobPlacement(Mob("llama", "minecraft:llama")),
    MobPlacement(Mob("magma_cube", "minecraft:magma_cube")),
    MobPlacement(Mob("mooshroom", "minecraft:mooshroom")),
    MobPlacement(Mob("mule", "minecraft:mule")),
    MobPlacement(Mob("ocelot", "minecraft:ocelot")),
    MobPlacement(Mob("panda", "minecraft:panda")),
    MobPlacement(Mob("parrot", "minecraft:parrot")),
    MobPlacement(Mob("pig", "minecraft:pig")),
    MobPlacement(Mob("pillager", "minecraft:pillager")),
    MobPlacement(Mob("polar_bear", "minecraft:polar_bear")),
    MobPlacement(Mob("pufferfish", "minecraft:pufferfish")),
    MobPlacement(Mob("rabbit", "minecraft:rabbit")),
    MobPlacement(Mob("raccoon", "animalplus:raccoon")),
    MobPlacement(Mob("ravager", "minecraft:ravager")),
    MobPlacement(Mob("red_panda", "animalplus:red_panda")),
    MobPlacement(Mob("salmon", "minecraft:salmon")),
    MobPlacement(Mob("sheep", "minecraft:sheep")),
    MobPlacement(Mob("skeleton", "minecraft:skeleton")),
    MobPlacement(Mob("slime", "minecraft:slime")),
    MobPlacement(Mob("spider", "minecraft:spider")),
    MobPlacement(Mob("squid", "minecraft:squid")),
    MobPlacement(Mob("tropical_fish", "minecraft:tropical_fish")),
    MobPlacement(Mob("turtle", "minecraft:turtle")),
    MobPlacement(Mob("vex", "minecraft:vex")),
    MobPlacement(Mob("villager", "minecraft:villager")),
    MobPlacement(Mob("vindicator", "minecraft:vindicator")),
    MobPlacement(Mob("wandering_trader", "minecraft:wandering_trader")),
    MobPlacement(Mob("warden", "minecraft:warden")),
    MobPlacement(Mob("witch", "minecraft:witch")),
    MobPlacement(Mob("wither_skeleton", "minecraft:wither_skeleton")),
    MobPlacement(Mob("wither", "minecraft:wither")),
    MobPlacement(Mob("wolf", "minecraft:wolf")),
    MobPlacement(Mob("zoglin", "minecraft:zoglin")),
    MobPlacement(Mob("zombie_villager", "minecraft:zombie_villager")),
    MobPlacement(Mob("zombie", "minecraft:zombie")),
])
