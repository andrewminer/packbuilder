from mcpacker.model.core.ecology.biomefilter import BiomeFilter as BF
from mcpacker.model.core.fauna.mob import Mob
from mcpacker.model.core.fauna.mobcatalog import MobCatalog
from mcpacker.model.core.fauna.mobspawn import MobSpawn
from mcpacker.model.core.habitat import Habitat
from mcpacker.model.core.resourceid import ResourceId
from mcpacker.model.modpack import ModPack

import mcpacker.model.core.altitude as AL
import mcpacker.model.core.ecology.flora as FL
import mcpacker.model.core.ecology.geology as GE
import mcpacker.model.core.ecology.heat as HE
import mcpacker.model.core.ecology.humidity as HU
import mcpacker.model.core.ecology.soil as SO
import mcpacker.model.core.ecology.water as WA
import mcpacker.model.core.fauna.active as AC
import mcpacker.model.core.fauna.group as GR
import mcpacker.model.core.fauna.location as LO
import mcpacker.model.core.scarcity as SC
import mcpacker.model.core.season as SE


# Constants ########################################################################################

def addMobSpawns(pack:ModPack):
    mobs = pack.world.mobs
    spawns = pack.world.mobSpawns

    spawns.add(
        MobSpawn(mobs["animalplus:raccoon"],
            Habitat(
                altitude = AL.span(AL.LOWLANDS, AL.HILLS),
                biomeFilter = BF([(FL.CANOPY, FL.FOREST), HE.within(HE.TEMPERATE, HE.BOREAL)]),
                seasons = SE.exclude(SE.WINTER),
                group = GR.merge(GR.SOLO, GR.PAIR),
                scarcity = SC.UNCOMMON,
            ).derive(
                seasons = SE.WINTER,
                scarcity = SC.SPARSE,
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["animalplus:red_panda"],
            Habitat(
                altitude = AL.span(AL.UPLANDS, AL.HILLS),
                biomeFilter = BF([ResourceId.parse("bamboo_forest")]),
                seasons = SE.ALL,
                group = GR.merge(GR.SOLO, GR.PAIR),
                scarcity = SC.SPARSE,
            )
        )
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
                altitude = AL.LOWLANDS,
                biomeFilter = BF([HE.SUBTROPICAL, HU.DRY, SO.CLAYEY]),
                seasons = SE.SUMMER,
                group = GR.merge(GR.SOLO, GR.PAIR),
                scarcity = SC.COMMON
            ).derive(
                altitude = AL.UPLANDS,
                scarcity = SC.SPARSE,
            ).derive(
                altitude = AL.LOWLANDS,
                scarcity = SC.UNCOMMON,
                seasons = SE.exclude(SE.SUMMER),
            ).derive(
                altitude = AL.UPLANDS,
                scarcity = SC.UNUSUAL,
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["minecraft:blaze"],
            Habitat(
                altitude = AL.PLUTONIC,
                location = LO.CAVE,
                group = GR.SOLO,
                scarcity = SC.UNCOMMON
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["bearminimum:brown_bear"],
            Habitat(
                altitude = AL.span(AL.LOWLANDS, AL.ALPINE),
                biomeFilter = BF([HE.BOREAL, (FL.CANOPY, FL.FOREST)]),
                seasons = SE.AUTUMN,
                group = GR.SOLO,
                scarcity = SC.SPARSE
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
                location = LO.CAVE,
                group = GR.SOLO,
                scarcity = SC.UNCOMMON
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["cold_sweat:chameleon"],
            Habitat(
                altitude = AL.span(AL.DUNES, AL.UPLANDS),
                biomeFilter = BF([(FL.CANOPY, FL.FOREST), HE.TROPICAL, HU.WET, WA.INLAND]),
                seasons = SE.WET,
                group = GR.merge(GR.SOLO, GR.FAMILY),
                scarcity = SC.COMMON,
            ).derive(
                seasons = SE.DRY,
                scarcity = SC.UNCOMMON,
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["minecraft:chicken"],
            Habitat(
                altitude = AL.span(AL.LOWLANDS, AL.UPLANDS),
                biomeFilter = BF([FL.CLEARING, HE.TROPICAL, HU.WET], [SO.FUNGAL]),
                seasons = SE.SUMMER,
                group = GR.TROUP,
                scarcity = SC.COMMON,
            ).derive(
                seasons = SE.exclude(SE.SUMMER),
                scarcity = SC.UNCOMMON
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["minecraft:cod"],
            Habitat(
                altitude = AL.span(AL.SHALLOWS, AL.DEEPS),
                biomeFilter = BF([HE.BOREAL, WA.OCEAN]),
                seasons = SE.ALL,
                group = GR.HERD,
                scarcity = SC.COMMON,
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
                scarcity = SC.SPARSE,
            ).derive(
                altitude = AL.LOWLANDS,
                seasons = [SE.AUTUMN, SE.WINTER],
                group = GR.TROUP,
                scarcity = SC.UNUSUAL,
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
                scarcity = SC.UNCOMMON,
            ).derive(
                biomeFilter = BF([WA.COAST, [HE.TEMPERATE, HE.BOREAL]]),
                scarcity = SC.SPARSE,
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
            scarcity = SC.SPARSE,
        ).derive(
            altitude = AL.span(AL.LOWLANDS, AL.UPLANDS),
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
        MobSpawn(mobs["minecraft:frog"],
            Habitat(
                altitude = AL.span(AL.SURFACE, AL.DUNES),
                biomeFilter = BF([(HE.TROPICAL, HE.TEMPERATE), HU.WET, WA.SWAMP]),
                group = GR.HERD,
                scarcity = SC.COMMON,
                seasons = [SE.SUMMER],
            ).derive(
                seasons = [SE.SPRING],
                scarcity = SC.SPARSE,
            ).derive(
                seasons = [SE.AUTUMN],
                scarcity = SC.UNUSUAL,
            ).derive(
                seasons = [SE.WINTER],
                scarcity = SC.ABSENT,
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["minecraft:glow_squid"],
            Habitat(
                altitude = AL.ABYSS,
                biomeFilter = BF([WA.OCEAN], [HE.FROZEN]),
                group = GR.SOLO,
                location = LO.WATER,
                scarcity = SC.RARE,
                seasons = SE.ALL,
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["minecraft:goat"],
            Habitat(
                altitude = AL.span(AL.HILLS, AL.CRAGS),
                biomeFilter = BF([(HE.BOREAL, HE.FROZEN), SO.ROCKY]),
                group = GR.FAMILY,
                scarcity = SC.UNCOMMON,
                seasons = SE.ALL,
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["minecraft:horse"],
            Habitat(
                altitude = AL.span(AL.DUNES, AL.LOWLANDS),
                biomeFilter = BF(
                    [FL.FIELD, (HE.SUBTROPICAL, HE.TEMPERATE), (SO.LOAMY, SO.PEATY, SO.SANDY)]
                ),
                group = GR.HERD,
                scarcity = SC.UNUSUAL,
                seasons = SE.ALL,
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["minecraft:llama"],
            Habitat(
                altitude = AL.span(AL.ALPINE, AL.PEAKS),
                biomeFilter = BF([(HE.BOREAL, HE.FROZEN), SO.ROCKY]),
                group = GR.HERD,
                scarcity = SC.UNCOMMON,
                seasons = SE.ALL,
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["minecraft:magma_cube"],
            Habitat(
                altitude = AL.PLUTONIC,
                location = LO.CAVE,
                group = GR.SOLO,
                scarcity = SC.UNCOMMON
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["minecraft:mooshroom"],
            Habitat(
                altitude = AL.span(AL.DUNES, AL.UPLANDS),
                biomeFilter = BF([SO.FUNGAL]),
                group = GR.HERD,
                scarcity = SC.UNCOMMON,
                seasons = SE.ALL,
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["minecraft:ocelot"],
            Habitat(
                altitude = AL.span(AL.LOWLANDS, AL.HILLS),
                biomeFilter = BF([FL.CANOPY, HE.TROPICAL, HU.WET]),
                group = GR.SOLO,
                scarcity = SC.RARE,
                seasons = SE.ALL,
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["minecraft:panda"],
            Habitat(
                altitude = AL.span(AL.LOWLANDS, AL.UPLANDS),
                biomeFilter = BF([ResourceId.parse("bamboo_forest")]),
                group = GR.SOLO,
                scarcity = SC.UNUSUAL,
                seasons = SE.exclude(SE.SPRING),
            ).derive(
                group = GR.PAIR,
                seasons = SE.SPRING,
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["minecraft:parrot"],
            Habitat(
                altitude = AL.span(AL.DUNES, AL.HILLS),
                biomeFilter = BF([(FL.CANOPY, FL.FOREST), HE.TROPICAL, HU.WET]),
                group = GR.PAIR,
                scarcity = SC.COMMON,
                seasons = SE.ALL,
            ).derive(
                biomeFilter = BF([FL.CLEARING, HE.TROPICAL, HU.WET], [SO.FUNGAL]),
                scarcity = SC.UNCOMMON,
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["minecraft:pig"],
            Habitat(
                altitude = AL.span(AL.LOWLANDS, AL.HILLS),
                biomeFilter = BF([
                    FL.within(FL.CANOPY, FL.CLEARING),
                    HE.within(HE.SUBTROPICAL, HE.TEMPERATE)
                ]),
                group = GR.TROUP,
                scarcity = SC.COMMON,
                seasons = [SE.SUMMER],
            ).derive(
                scarcity = SC.UNCOMMON,
                seasons = SE.exclude(SE.SUMMER),
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["minecraft:polar_bear"],
            Habitat(
                altitude = AL.DUNES,
                biomeFilter = BF([HE.FROZEN, (WA.COAST, WA.OCEAN)]),
                group = GR.PAIR,
                scarcity = SC.UNUSUAL,
                seasons = [SE.SPRING, SE.WINTER]
            ).derive(
                group = GR.SOLO,
                seasons = [SE.SUMMER, SE.AUTUMN],
                scarcity = SC.RARE,
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["minecraft:pufferfish"],
            Habitat(
                altitude = AL.SHALLOWS,
                biomeFilter = BF([(HE.TEMPERATE, HE.TROPICAL), WA.OCEAN]),
                group = GR.TROUP,
                location = LO.WATER,
                scarcity = SC.UNCOMMON,
                seasons = SE.ALL,
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["minecraft:rabbit"],
            Habitat(
                altitude = AL.span(AL.DUNES, AL.ALPINE),
                biomeFilter = BF([
                    FL.within(FL.CANOPY, FL.FIELD),
                    HE.within(HE.SUBTROPICAL, HE.BOREAL),
                    WA.INLAND,
                ]),
                group = GR.FAMILY,
                scarcity = SC.COMMON,
                seasons = [SE.SPRING],
            ).derive(
                scarcity = SC.SPARSE,
                seasons = [SE.SUMMER, SE.AUTUMN],
            ).derive(
                scarcity = SC.SPARSE,
                seasons = [SE.WINTER],
            ).derive(
                altitude = AL.span(AL.DUNES, AL.LOWLANDS),
                biomeFilter = BF([FL.BARREN, HE.TROPICAL, HU.DRY]),
                group = GR.PAIR,
                scarcity = SC.SPARSE,
                seasons = SE.exclude(SE.SUMMER),
            ).derive(
                scarcity = SC.UNUSUAL,
                seasons = [SE.SUMMER],
            ).derive(
                altitude = AL.span(AL.LOWLANDS, AL.UPLANDS),
                biomeFilter = BF([FL.within(FL.FOREST, FL.FIELD), HE.FROZEN]),
                scarcity = SC.SPARSE,
                seasons = SE.exclude(SE.WINTER),
            ).derive(
                scarcity = SC.UNUSUAL,
                seasons = [SE.WINTER],
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["minecraft:salmon"],
            Habitat(
                altitude = AL.span(AL.SURFACE, AL.SHALLOWS),
                biomeFilter = BF([WA.RIVER], [HE.FROZEN]),
                group = GR.HERD,
                scarcity = SC.COMMON,
                seasons = [SE.AUTUMN],
            ).derive(
                scarcity = SC.UNCOMMON,
                seasons = [SE.SPRING],
            ).derive(
                seasons = [SE.SUMMER, SE.WINTER],
                scarcity = SC.ABSENT,
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["minecraft:sheep"],
            Habitat(
                altitude = AL.span(AL.LOWLANDS, AL.UPLANDS),
                biomeFilter = BF([FL.within(FL.FOREST, FL.FIELD), HE.BOREAL]),
                group = GR.HERD,
                scarcity = SC.UNCOMMON,
                seasons = SE.ALL,
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["minecraft:slime"],
            Habitat(
                altitude = AL.span(AL.SURFACE, AL.DUNES),
                biomeFilter = BF([HE.TEMPERATE, WA.SWAMP]),
                group = GR.SOLO,
                scarcity = SC.UNCOMMON,
                seasons = [SE.SPRING],
            ).derive(
                scarcity = SC.UNUSUAL,
                seasons = SE.exclude(SE.SPRING),
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["minecraft:spider"],
            Habitat(
                altitude = AL.span(AL.LOWLANDS, AL.HILLS),
                biomeFilter = BF([FL.CANOPY, HE.TEMPERATE]),
                group = GR.SOLO,
                scarcity = SC.COMMON,
                seasons = [SE.SUMMER],
            ).derive(
                scarcity = SC.UNCOMMON,
                seasons = [SE.SPRING, SE.AUTUMN],
            ).derive(
                scarcity = SC.SPARSE,
                seasons = [SE.WINTER],
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["minecraft:squid"],
            Habitat(
                altitude = AL.DEEPS,
                biomeFilter = BF([WA.OCEAN], [HE.FROZEN]),
                group = GR.SOLO,
                location = LO.WATER,
                scarcity = SC.SPARSE,
                seasons = SE.ALL,
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["minecraft:tropical_fish"],
            Habitat(
                altitude = AL.SHALLOWS,
                biomeFilter = BF([HE.TROPICAL, WA.OCEAN]),
                group = GR.HERD,
                location = LO.WATER,
                scarcity = SC.COMMON,
                seasons = SE.ALL,
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["minecraft:turtle"],
            Habitat(
                altitude = AL.span(AL.SURFACE, AL.SHALLOWS),
                biomeFilter = BF([HE.within(HE.TROPICAL, HE.SUBTROPICAL), WA.OCEAN]),
                group = GR.SOLO,
                scarcity = SC.SPARSE,
                seasons = SE.ALL,
            ).derive(
                altitude = AL.DUNES,
                biomeFilter = BF([HE.within(HE.TROPICAL, HE.SUBTROPICAL), WA.COAST]),
                group = GR.SOLO,
                scarcity = SC.UNUSUAL,
            )
        )
    )

    spawns.add(
        MobSpawn(mobs["minecraft:wolf"],
            Habitat(
                altitude = AL.span(AL.LOWLANDS, AL.UPLANDS),
                biomeFilter = BF([FL.CANOPY, HE.TEMPERATE, WA.INLAND]),
                group = GR.TROUP,
                scarcity = SC.COMMON,
                seasons = SE.ALL,
            ).derive(
                biomeFilter = BF([
                    FL.within(FL.FOREST, FL.FIELD), (HE.TEMPERATE, HE.BOREAL), WA.INLAND,
                ]),
                scarcity = SC.UNCOMMON,
            ).derive(
                biomeFilter = BF([FL.within(FL.FOREST, FL.FIELD), HE.FROZEN, WA.INLAND]),
                scarcity = SC.UNUSUAL,
            ).derive(
                biomeFilter = BF([(FL.CLEARING, FL.FIELD), HE.SUBTROPICAL, WA.INLAND]),
                scarcity = SC.SPARSE,
            )
        )
    )
