from mcpacker.model.core.ecology.biomefilter import BiomeFilter as BF
from mcpacker.model.core.fauna.mob           import Mob
from mcpacker.model.core.fauna.mobcatalog    import MobCatalog
from mcpacker.model.core.fauna.mobspawn      import MobSpawn
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
    spawns = pack.world.mobSpawns

    spawns.add(
        MobSpawn(mobs["animalplus:raccoon"])
    )

    spawns.add(
        MobSpawn(mobs["animalplus:red_panda"])
    )

    spawns.add(
        MobSpawn(mobs["bearminimum:black_bear"],
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

    spawns.add(
        MobSpawn(mobs["minecraft:armadillo"],
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

    spawns.add(
        MobSpawn(mobs["minecraft:blaze"],
            Habitat(
                altitude = AL.PLUTONIC,
                location  = LO.CAVE,
                group     = GR.SOLO,
                scarcity  = SC.UNCOMMON
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["minecraft:bogged"])
    )

    spawns.add(
        MobSpawn(mobs["bearminimum:brown_bear"],
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

    spawns.add(
        MobSpawn(mobs["minecraft:camel"],
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

    spawns.add(
        MobSpawn(mobs["minecraft:cave_spider"],
            Habitat(
                altitude = AL.span(AL.OVERBURDEN, AL.HILLS),
                location  = LO.CAVE,
                group     = GR.SOLO,
                scarcity  = SC.UNCOMMON
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["cold_sweat:chameleon"],
            Habitat(
                altitude    = AL.span(AL.DUNES, AL.UPLANDS),
                biomeFilter = BF([HE.TROPICAL, HU.WET, [FL.CANOPY, FL.FOREST]]),
                seasons     = SE.WET,
                group       = GR.merge(GR.SOLO, GR.FAMILY),
                scarcity    = SC.COMMON,
            ).derive(
                seasons     = SE.DRY,
                scarcity    = SC.UNCOMMON,
            ).derive(
                biomeFilter = BF([HE.TROPICAL, HU.WET, FL.CLEARING]),
                seasons     = SE.WET,
                scarcity    = SC.UNCOMMON
            ).derive(
                seasons     = SE.DRY,
                scarcity    = SC.SPARSE,
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["minecraft:chicken"],
            Habitat(
                altitude    = AL.span(AL.LOWLANDS, AL.UPLANDS),
                biomeFilter = BF([HE.TROPICAL, HU.WET, FL.within(FL.CANOPY, FL.CLEARING)]),
                seasons     = SE.SUMMER,
                group       = GR.TROUP,
                scarcity    = SC.COMMON,
            ).derive(
                seasons     = SE.exclude(SE.SUMMER),
                scarcity    = SC.UNCOMMON
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["minecraft:cod"],
            Habitat(
                altitude    = AL.span(AL.SHALLOWS, AL.DEEPS),
                biomeFilter = BF([WA.OCEAN, [HE.TEMPERATE, HE.BOREAL]]),
                seasons     = SE.ALL,
                group       = GR.HERD,
                scarcity    = SC.COMMON,
            ).derive(
                biomeFilter = BF([WA.OCEAN, HE.FROZEN]),
                scarcity    = SC.SPARSE,
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["minecraft:cow"],
            Habitat(
                altitude = AL.span(AL.LOWLANDS, AL.UPLANDS),
                biomeFilter = BF(
                    [
                        HE.within(HE.SUBTROPICAL, HE.BOREAL),
                        [HU.DAMP, HU.DRY],
                        FL.FIELD,
                    ], [
                        SO.FUNGAL
                    ]
                ),
                seasons = [SE.SPRING, SE.SUMMER],
                group = GR.HERD,
                scarcity = SC.COMMON,
            ).derive(
                altitude = AL.LOWLANDS,
                seasons = [SE.AUTUMN, SE.WINTER],
                groups = GR.TROUP,
                scarcity = SC.SPARSE,
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["crabbersdelight:crab"],
            Habitat(
                altitude = AL.DUNES,
                biomeFilter = BF([WA.COAST, [HE.TROPICAL, HE.SUBTROPICAL]]),
                seasons = SE.ALL,
                group = GR.SOLO,
                scarcity = SC.COMMON,
            ).derive(
                biomeFilter = BF([WA.COAST, [HE.TEMPERATE, HE.BOREAL]]),
                scarcity = SC.UNCOMMON,
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["minecraft:dolphin"],
            Habitat(
                altitude = AL.span(AL.SURFACE, AL.DEEPS),
                biomeFilter = BF([WA.OCEAN, [HE.SUBTROPICAL, HE.TEMPERATE]]),
                location = LO.WATER,
                seasons = SE.SUMMER,
                group = GR.FAMILY,
                scarcity = SC.UNCOMMON,
            ).derive(
                seasons = SE.exclude(SE.SUMMER),
                scarcity = SC.SPARSE,
            )
        )
    )

    spawns.add(MobSpawn(mobs["minecraft:donkey"],
        Habitat(
            altitude = AL.span(AL.UPLANDS, AL.HILLS),
            biomeFilter = BF([HE.SUBTROPICAL, HU.DRY, FL.FIELD]),
            seasons = [SE.SUMMER, SE.AUTUMN],
            group = GR.FAMILY,
            scarcity = SC.UNCOMMON,
        ).derive(
            seasons = [SE.WINTER, SE.SPRING],
            scarcity = SC.SPARSE,
        )
    ))

    spawns.add(MobSpawn(mobs["minecraft:fox"],
        Habitat(
            altitude = AL.span(AL.LOWLANDS, AL.HILLS),
            biomeFilter = BF([HE.within(HE.TEMPERATE, HE.FROZEN), FL.FOREST]),
            seasons = [SE.SPRING],
            group = GR.FAMILY,
            scarcity = SC.UNCOMMON,
        ).derive(
            seasons = SE.exclude(SE.SPRING),
            group = GR.SOLO,
            scarcity = SC.SPARSE,
        )
     ))

    spawns.add(
        MobSpawn(mobs["minecraft:frog"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:glow_squid"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:goat"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:horse"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:husk"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:llama"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:magma_cube"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:mooshroom"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:mule"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:ocelot"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:panda"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:parrot"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:pig"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:polar_bear"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:pufferfish"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:rabbit"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:salmon"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:sheep"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:skeleton"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:slime"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:spider"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:squid"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:tropical_fish"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:turtle"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:vex"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:villager"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:vindicator"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:wandering_trader"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:warden"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:witch"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:wither_skeleton"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:wither"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:wolf"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:zoglin"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:zombie_villager"])
    )

    spawns.add(
        MobSpawn(mobs["minecraft:zombie"])
    )
