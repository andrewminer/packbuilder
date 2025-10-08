from mcpacker.model.core.ecology.biomefilter import BiomeFilter as BF
from mcpacker.model.core.fauna.mob           import Mob
from mcpacker.model.core.fauna.mobcatalog    import MobCatalog
from mcpacker.model.core.fauna.mobplacement  import MobPlacement
from mcpacker.model.core.habitat             import Habitat
from mcpacker.model.modpack                  import ModPack

import mcpacker.model.core.altitude         as AL
import mcpacker.model.core.ecology.flora    as FL
import mcpacker.model.core.ecology.geology  as GE
import mcpacker.model.core.ecology.heat     as HE
import mcpacker.model.core.ecology.humidity as HU
import mcpacker.model.core.ecology.soil     as SO
import mcpacker.model.core.ecology.water    as WA
import mcpacker.model.core.fauna.active     as AC
import mcpacker.model.core.fauna.group      as GR
import mcpacker.model.core.fauna.location   as LO
import mcpacker.model.core.scarcity         as SC
import mcpacker.model.core.season           as SE


# Constants ########################################################################################

def addMobs(pack:ModPack):
    mobs = pack.world.mobs

    mobs.add(
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
                altitude = AL.LOWLANDS, seasons = SE.exclude(SE.SUMMER), scarcity = SC.UNCOMMON,
            ).derive(
                altitude = AL.UPLANDS, scarcity = SC.UNUSUAL,
            )
        )
    )

    mobs.add(
        MobPlacement(Mob("black_bear", "bearminimum:black_bear"),
            Habitat(
                altitude = AL.span(AL.LOWLANDS, AL.ALPINE),
                biomeFilter = BF([HE.TEMPERATE, FL.FOREST]),
                seasons = SE.AUTUMN,
                group = GR.merge(GR.SOLO, GR.FAMILY),
                scarcity = SC.UNCOMMON,
            ).derive(
                seasons = [SE.SPRING, SE.SUMMER], scarcity = SC.SPARSE
            ).derive(
                seasons = SE.WINTER, scarcity = SC.UNUSUAL
            ).derive(
                biomeFilter = BF([HE.BOREAL, (FL.CANOPY, FL.FOREST)]),
                seasons = SE.AUTUMN,
                scarcity = SC.SPARSE
            ).derive(
                seasons = [SE.SPRING, SE.SUMMER], scarcity = SC.UNUSUAL
            ).derive(
                seasons = SE.WINTER, scarcity = SC.RARE
            )
        )
    )

    mobs.add(
        MobPlacement(Mob("blaze", "minecraft:blaze"),
            Habitat(
                altitude = AL.PLUTONIC,
                location  = LO.CAVE,
                group     = GR.SOLO,
                scarcity  = SC.UNCOMMON
            )
        )
    )

    mobs.add(
        MobPlacement(Mob("bogged", "minecraft:bogged"))
    )

    mobs.add(
        MobPlacement(Mob("brown_bear", "bearminimum:brown_bear"),
            Habitat(
                altitude   = AL.span(AL.LOWLANDS, AL.ALPINE),
                biomeFilter = BF([HE.BOREAL, (FL.CANOPY, FL.FOREST)]),
                seasons     = SE.AUTUMN,
                group       = GR.SOLO,
                scarcity    = SC.SPARSE
            ).derive(
                seasons = [SE.SPRING, SE.SUMMER], scarcity = SC.UNUSUAL
            ).derive(
                seasons = SE.WINTER, scarcity = SC.RARE
            )
        )
    )

    mobs.add(
        MobPlacement(Mob("bulwark", "immersiveengineering:bulwark"))
    )

    mobs.add(
        MobPlacement(Mob("camel", "minecraft:camel", AC.CREPUSCULAR),
            Habitat(
                altitude = AL.span(AL.DUNES, AL.LOWLANDS),
                biomeFilter = BF([HE.TROPICAL, HU.DRY, FL.BARREN, SO.SANDY]),
                seasons = SE.DRY,
                group = GR.FAMILY,
                scarcity = SC.UNUSUAL,
            ).derive(
                seasons = SE.WET, scarcity = SC.RARE
            )
        )
    )

    mobs.add(
        MobPlacement(Mob("cat", "minecraft:cat"))
    )

    mobs.add(
        MobPlacement(Mob("cave_spider", "minecraft:cave_spider"),
            Habitat(
                altitude = AL.span(AL.OVERBURDEN, AL.HILLS),
                location  = LO.CAVE,
                group     = GR.SOLO,
                scarcity  = SC.UNCOMMON
            )
        )
    )

    mobs.add(
        MobPlacement(Mob("chameleon", "cold_sweat:chameleon"),
            Habitat(
                altitude = AL.span(AL.DUNES, AL.UPLANDS),
                biomeFilter = BF([HE.TROPICAL, HU.WET, [FL.CANOPY, FL.FOREST]]),
                seasons = SE.WET,
                group = GR.merge(GR.SOLO, GR.FAMILY),
                scarcity = SC.COMMON,
            ).derive(
                seasons = SE.DRY, scarcity = SC.UNCOMMON,
            ).derive(
                biomeFilter = BF([HE.TROPICAL, HU.WET, FL.CLEARING]),
                seasons = SE.WET,
                scarcity = SC.UNCOMMON
            ).derive(
                seasons = SE.DRY, scarcity = SC.SPARSE,
            )
        )
    )

    mobs.add(
        MobPlacement(Mob("chicken", "minecraft:chicken"),
            Habitat(
                altitude = AL.span(AL.LOWLANDS, AL.UPLANDS),
                biomeFilter = BF([HE.TROPICAL, HU.WET, FL.within(FL.CANOPY, FL.CLEARING)]),
                seasons = SE.SUMMER,
                group = GR.TROUP,
                scarcity = SC.COMMON,
            ).derive(
                seasons = SE.exclude(SE.SUMMER), scarcity = SC.UNCOMMON
            )
        )
    )

    mobs.add(
        MobPlacement(Mob("cod", "minecraft:cod"))
    )

    mobs.add(
        MobPlacement(Mob("commando", "immersiveengineering:commando"))
    )

    mobs.add(
        MobPlacement(Mob("cow", "minecraft:cow"))
    )

    mobs.add(
        MobPlacement(Mob("crab", "crabbersdelight:crab"))
    )

    mobs.add(
        MobPlacement(Mob("creeper", "minecraft:creeper"))
    )

    mobs.add(
        MobPlacement(Mob("dolphin", "minecraft:dolphin"))
    )

    mobs.add(
        MobPlacement(Mob("donkey", "minecraft:donkey"))
    )

    mobs.add(
        MobPlacement(Mob("drowned", "minecraft:drowned"))
    )

    mobs.add(
        MobPlacement(Mob("enderman", "minecraft:enderman"))
    )

    mobs.add(
        MobPlacement(Mob("evoker", "minecraft:evoker"))
    )

    mobs.add(
        MobPlacement(Mob("fox", "minecraft:fox"))
    )

    mobs.add(
        MobPlacement(Mob("frog", "minecraft:frog"))
    )

    mobs.add(
        MobPlacement(Mob("fusilier", "immersiveengineering:fusilier"))
    )

    mobs.add(
        MobPlacement(Mob("glow_squid", "minecraft:glow_squid"))
    )

    mobs.add(
        MobPlacement(Mob("goat", "minecraft:goat"))
    )

    mobs.add(
        MobPlacement(Mob("hoglin", "minecraft:hoglin"))
    )

    mobs.add(
        MobPlacement(Mob("horse", "minecraft:horse"))
    )

    mobs.add(
        MobPlacement(Mob("husk", "minecraft:husk"))
    )

    mobs.add(
        MobPlacement(Mob("llama", "minecraft:llama"))
    )

    mobs.add(
        MobPlacement(Mob("magma_cube", "minecraft:magma_cube"))
    )

    mobs.add(
        MobPlacement(Mob("mooshroom", "minecraft:mooshroom"))
    )

    mobs.add(
        MobPlacement(Mob("mule", "minecraft:mule"))
    )

    mobs.add(
        MobPlacement(Mob("ocelot", "minecraft:ocelot"))
    )

    mobs.add(
        MobPlacement(Mob("panda", "minecraft:panda"))
    )

    mobs.add(
        MobPlacement(Mob("parrot", "minecraft:parrot"))
    )

    mobs.add(
        MobPlacement(Mob("pig", "minecraft:pig"))
    )

    mobs.add(
        MobPlacement(Mob("pillager", "minecraft:pillager"))
    )

    mobs.add(
        MobPlacement(Mob("polar_bear", "minecraft:polar_bear"))
    )

    mobs.add(
        MobPlacement(Mob("pufferfish", "minecraft:pufferfish"))
    )

    mobs.add(
        MobPlacement(Mob("rabbit", "minecraft:rabbit"))
    )

    mobs.add(
        MobPlacement(Mob("raccoon", "animalplus:raccoon"))
    )

    mobs.add(
        MobPlacement(Mob("ravager", "minecraft:ravager"))
    )

    mobs.add(
        MobPlacement(Mob("red_panda", "animalplus:red_panda"))
    )

    mobs.add(
        MobPlacement(Mob("salmon", "minecraft:salmon"))
    )

    mobs.add(
        MobPlacement(Mob("sheep", "minecraft:sheep"))
    )

    mobs.add(
        MobPlacement(Mob("skeleton", "minecraft:skeleton"))
    )

    mobs.add(
        MobPlacement(Mob("slime", "minecraft:slime"))
    )

    mobs.add(
        MobPlacement(Mob("spider", "minecraft:spider"))
    )

    mobs.add(
        MobPlacement(Mob("squid", "minecraft:squid"))
    )

    mobs.add(
        MobPlacement(Mob("tropical_fish", "minecraft:tropical_fish"))
    )

    mobs.add(
        MobPlacement(Mob("turtle", "minecraft:turtle"))
    )

    mobs.add(
        MobPlacement(Mob("vex", "minecraft:vex"))
    )

    mobs.add(
        MobPlacement(Mob("villager", "minecraft:villager"))
    )

    mobs.add(
        MobPlacement(Mob("vindicator", "minecraft:vindicator"))
    )

    mobs.add(
        MobPlacement(Mob("wandering_trader", "minecraft:wandering_trader"))
    )

    mobs.add(
        MobPlacement(Mob("warden", "minecraft:warden"))
    )

    mobs.add(
        MobPlacement(Mob("witch", "minecraft:witch"))
    )

    mobs.add(
        MobPlacement(Mob("wither_skeleton", "minecraft:wither_skeleton"))
    )

    mobs.add(
        MobPlacement(Mob("wither", "minecraft:wither"))
    )

    mobs.add(
        MobPlacement(Mob("wolf", "minecraft:wolf"))
    )

    mobs.add(
        MobPlacement(Mob("zoglin", "minecraft:zoglin"))
    )

    mobs.add(
        MobPlacement(Mob("zombie_villager", "minecraft:zombie_villager"))
    )

    mobs.add(
        MobPlacement(Mob("zombie", "minecraft:zombie"))
    )
