from mcpacker.model.core.ecology.biomefilter import BiomeFilter as BF
from mcpacker.model.core.geology.deposit.geodedeposit import GeodeDeposit
from mcpacker.model.core.geology.deposit.mineraldeposit import MineralDeposit
from mcpacker.model.core.geology.inclusion import Inclusion as I
from mcpacker.model.modpack import ModPack

import mcpacker.model.core.altitude as AL
import mcpacker.model.core.ecology.flora as FL
import mcpacker.model.core.ecology.geology as GE
import mcpacker.model.core.ecology.heat as HE
import mcpacker.model.core.ecology.humidity as HU
import mcpacker.model.core.ecology.soil as SO
import mcpacker.model.core.ecology.water as WA
import mcpacker.model.core.geology.bulk as BU
import mcpacker.model.core.geology.proportion as PR
import mcpacker.model.core.scarcity as SC


# Catalog ##########################################################################################

def addDeposits(pack:ModPack):
    minerals = pack.world.minerals
    deposits = pack.world.deposits

    # Geode Deposits ###########################################################

    deposits.add(GeodeDeposit(
        name = "geode_amethyst",
        altitude = AL.span(AL.MANTLE, AL.CRUST),
        # TODO: these filter exclude all biomes
        biomeFilters = BF([GE.IGNEOUS, HE.TEMPERATE, HU.DAMP]),
        scarcity = SC.UNCOMMON,
    ))

    deposits.add(GeodeDeposit(
        name = "geode_kimberlite",
        altitude = AL.span(AL.MANTLE, AL.CRUST),
        biomeFilters = BF([GE.IGNEOUS]),
        scarcity = SC.SPARSE,
    ))

    deposits.add(MineralDeposit(
        name = "hydrothermal_emerald",
        altitude = AL.span(AL.CRUST, AL.SUBSTRATE),
        biomeFilters = BF([HE.FROZEN, GE.METAMORPHIC, SO.ROCKY]),
        scarcity = SC.UNCOMMON,
    ))

    # Metal Deposits ###########################################################

    deposits.add(MineralDeposit(
        name = "bif_iron",
        altitude = AL.span(AL.CRUST, AL.SUBSTRATE),
        biomeFilters = BF([FL.FIELD, HE.SUBTROPICAL, HU.DRY]),
        bulk = BU.LARGE,
        inclusions = [
            I(minerals["iron"], 50),
            I(minerals["quartz"], 45),
            I(minerals["uranium"], 5)
        ],
        proportion = PR.BED,
        scarcity = SC.UNCOMMON,
    ))

    deposits.add(MineralDeposit(
        name = "epithermal_silver",
        altitude = AL.span(AL.OVERBURDEN, AL.SUBSTRATE),
        biomeFilters = BF([(HE.BOREAL, HE.FROZEN), SO.ROCKY, GE.IGNEOUS]),
        bulk = BU.SMALL,
        inclusions = [I(minerals["silver"], 75), I(minerals["gold"], 25)],
        proportion = PR.PIPE,
        scarcity = SC.RARE,
    ))

    deposits.add(MineralDeposit(
        name = "greisen_tin",
        altitude = AL.span(AL.OVERBURDEN, AL.SUBSTRATE),
        biomeFilters = BF([HE.BOREAL, SO.ROCKY, GE.METAMORPHIC]),
        bulk = BU.MEDIUM,
        inclusions = [I(minerals["tin"], 100)],
        proportion = PR.STOCK,
        scarcity = SC.COMMON,
    ))

    deposits.add(MineralDeposit(
        name = "laterite_aluminum",
        altitude = AL.span(AL.DUNES, AL.UPLANDS),
        biomeFilters = BF([FL.within(FL.CANOPY, FL.CLEARING), HU.WET, HE.TROPICAL, GE.SEDIMENTARY]),
        bulk = BU.MEDIUM,
        inclusions = [I(minerals["aluminum"], 70), I(minerals["nickel"], 30)],
        proportion = PR.LENS,
        scarcity = SC.UNCOMMON,
    ))

    deposits.add(MineralDeposit(
        name = "mvt_lead",
        altitude = AL.span(AL.CRUST, AL.SUBSTRATE),
        biomeFilters = [
            BF([FL.FIELD, GE.SEDIMENTARY, HE.TEMPERATE, HU.DAMP]),
            BF([GE.SEDIMENTARY, HE.TEMPERATE, SO.CLAYEY]),
        ],
        bulk = BU.MEDIUM,
        inclusions = [
            I(minerals["lead"], 45),
            I(minerals["zinc"], 40),
            I(minerals["silver"], 15),
        ],
        proportion = PR.LODE,
        scarcity = SC.SPARSE,
    ))

    deposits.add(MineralDeposit(
        name = "porphyry_copper",
        altitude = AL.span(AL.MANTLE, AL.OVERBURDEN),
        biomeFilters = BF([GE.SEDIMENTARY, HE.SUBTROPICAL, HU.DRY, SO.CLAYEY]),
        bulk = BU.LARGE,
        inclusions = [
            I(minerals["copper"], 55),
            I(minerals["redstone"], 25),
            I(minerals["gold"], 20),
        ],
        proportion = PR.PIPE,
        scarcity = SC.UNUSUAL,
    ))

    deposits.add(MineralDeposit(
        name = "sedimentary_iron",
        altitude = AL.span(AL.OVERBURDEN, AL.SOIL),
        biomeFilters = BF([
            FL.within(FL.CANOPY, FL.CLEARING),
            (HE.TEMPERATE, HE.BOREAL)
        ]),
        bulk = BU.LARGE,
        inclusions = [I(minerals["iron"], 100)],
        proportion = PR.LODE,
        scarcity = SC.COMMON,
    ))

    deposits.add(MineralDeposit(
        name = "serpentine_nickel",
        altitude = AL.span(AL.UPLANDS, AL.HILLS),
        biomeFilters = BF([GE.METAMORPHIC, (HU.DAMP, HU.WET), (SO.ACIDIC, SO.ROCKY)]),
        bulk = BU.SMALL,
        inclusions = [I(minerals["nickel"], 70), I(minerals["iron"], 30)],
        proportion = PR.LENS,
        scarcity = SC.UNCOMMON,
    ))

    # Mineral Deposits #########################################################

    deposits.add(MineralDeposit(
        name = "evaporite_salt",
        altitude = AL.EVAPORITES,
        biomeFilters = BF([HE.TROPICAL, HU.DRY, SO.SANDY]),
        bulk = BU.TINY,
        inclusions = [I(minerals["salt"], 100)],
        proportion = PR.BED,
        scarcity = SC.SPARSE,
    ))

    deposits.add(MineralDeposit(
        name = "evaporite_nitrate",
        altitude = AL.EVAPORITES,
        biomeFilters = BF([FL.BARREN, HE.SUBTROPICAL, HU.DRY, SO.CLAYEY]),
        bulk = BU.TINY,
        inclusions = [I(minerals["nitrate"], 100)],
        proportion = PR.BED,
        scarcity = SC.SPARSE,
    ))

    deposits.add(MineralDeposit(
        name = "fumarole_sulfur",
        altitude = AL.CRUST,
        biomeFilters = BF([GE.IGNEOUS]),
        bulk = BU.MEDIUM,
        inclusions = [I(minerals["sulfur"], 100)],
        proportion = PR.VENT,
        scarcity = SC.UNUSUAL,
    ))

    deposits.add(MineralDeposit(
        name = "sedimentary_redbed",
        altitude = AL.span(AL.SOIL, AL.HILLS),
        biomeFilters = BF([GE.SEDIMENTARY, HE.SUBTROPICAL, HU.DRY, SO.CLAYEY]),
        bulk = BU.SMALL,
        inclusions = [I(minerals["redstone"], 80), I(minerals["iron"], 20)],
        proportion = PR.BED,
        scarcity = SC.UNCOMMON,
    ))

    deposits.add(MineralDeposit(
        name = "skarn_lapis",
        altitude = AL.CRUST,
        biomeFilters = BF([GE.METAMORPHIC, HE.BOREAL, SO.ROCKY]),
        bulk = BU.LARGE,
        inclusions = [
            I(minerals["greywacke"], 50),
            I(minerals["lapis"], 25),
            I(minerals["diorite"], 10),
            I(minerals["quartz"], 10),
            I(minerals["iron"], 5),
        ],
        proportion = PR.LENS,
        scarcity = SC.SPARSE,
    ))

    deposits.add(MineralDeposit(
        name = "vein_quartz",
        altitude = AL.span(AL.SUBSTRATE, AL.OVERBURDEN),
        biomeFilters = BF([HE.TROPICAL, HU.DRY, SO.SANDY]),
        bulk = BU.MEDIUM,
        inclusions = [I(minerals["quartz"], 95), I(minerals["gold"], 5)],
        proportion = PR.LODE,
        scarcity = SC.UNUSUAL,
    ))

    # Organic Deposits #########################################################

    deposits.add(MineralDeposit(
        name = "bed_loam",
        altitude = AL.span(AL.SOIL),
        biomeFilters = BF([HE.TEMPERATE, HU.DAMP, SO.LOAMY]),
        bulk = BU.TINY,
        inclusions = [I(minerals["loam"], 100)],
        proportion = PR.BED,
        scarcity = SC.COMMON,
    ))

    deposits.add(MineralDeposit(
        name = "seam_bituminouscoal",
        altitude = AL.span(AL.CRUST, AL.OVERBURDEN),
        biomeFilters = [
            BF([FL.FOREST, GE.SEDIMENTARY, HE.TEMPERATE]),
            BF([HE.BOREAL, GE.METAMORPHIC, (SO.ACIDIC, SO.ROCKY)]),
        ],
        bulk = BU.HUGE,
        inclusions = [I(minerals["coal"], 100)],
        proportion = PR.BED,
        scarcity = SC.COMMON,
    ))

    deposits.add(MineralDeposit(
        name = "seam_peatcoal",
        altitude = AL.span(AL.SOIL),
        biomeFilters = BF([SO.PEATY]),
        bulk = BU.LARGE,
        inclusions = [I(minerals["peat"], 100)],
        proportion = PR.BED,
        scarcity = SC.COMMON,
    ))
