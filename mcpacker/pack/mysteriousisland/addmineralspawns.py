from mcpacker.model.ecology.biomefilter import BiomeFilter as BF
from mcpacker.model.geology.mineralspawnbuilder import MineralSpawnBuilder
from mcpacker.model.modpack import ModPack

import mcpacker.model.altitude as AL
import mcpacker.model.ecology.flora as FL
import mcpacker.model.ecology.geology as GE
import mcpacker.model.ecology.heat as HE
import mcpacker.model.ecology.humidity as HU
import mcpacker.model.ecology.soil as SO
import mcpacker.model.ecology.water as WA
import mcpacker.model.geology.bulk as BU
import mcpacker.model.geology.deposittype as DE
import mcpacker.model.scarcity as SC

# Helper Functions #################################################################################

def addMineralSpawns(pack:ModPack):
    minerals = pack.world.minerals
    b = MineralSpawnBuilder(pack.world.mineralSpawns)

    # Aluminum Family ##########################################################

    b.start(minerals["basalt"])
    b.biomeFilters = BF([HE.TROPICAL, HU.SOAKED, WA.INLAND])
    b.save("aluminum-indicator")

    b.switch(minerals["aluminum"])
    b.altitude = AL.span(AL.SUBSTRATE, AL.OVERBURDEN)
    b.bulk = BU.HUGE
    b.depositType = DE.STRATA
    b.scarcity = SC.COMMON
    b.save("aluminum-primary-aluminum")

    b.switch(minerals["nickel"])
    b.altitude = AL.span(AL.OVERBURDEN, AL.CRUST)
    b.bulk = BU.SMALL
    b.scarcity = SC.UNCOMMON
    b.save("aluminum-secondary-nickel")

    b.switch(minerals["amethyst"])
    b.altitude = AL.CRUST
    b.bulk = BU.TINY
    b.scarcity = SC.RARE
    b.save("aluminum-tertiary-amethyst")

    # Coal Family ##############################################################

    b.start(minerals["tuff"])
    b.biomeFilters = BF([GE.SEDIMENTARY, HE.TEMPERATE, HU.SOAKED])
    b.save("coal-indicator")

    b.switch(minerals["coal"])
    b.altitude = AL.span(AL.SUBSTRATE, AL.OVERBURDEN)
    b.bulk = BU.LARGE
    b.depositType = DE.STRATA
    b.scarcity = SC.COMMON
    b.save("coal-primary-coal")

    b.switch(minerals["sulfur"])
    b.altitude = AL.CRUST
    b.bulk = BU.SMALL
    b.scarcity = SC.SPARSE
    b.save("coal-secondary-sulfur")

    b.switch(minerals["iron"])
    b.altitude = AL.span(AL.CRUST, AL.MANTLE)
    b.bulk = BU.SMALL
    b.scarcity = SC.UNUSUAL
    b.save("coal-tertiary-iron")

    # Copper Family ############################################################

    b.start(minerals["diorite"])
    b.biomeFilters = BF([GE.SEDIMENTARY, HE.SUBTROPICAL, HU.DRY])
    b.save("copper-indicator")

    b.switch(minerals["copper"])
    b.altitude = AL.CRUST
    b.bulk = BU.MEDIUM
    b.scarcity = SC.UNCOMMON
    b.save("copper-primary-copper")

    b.switch(minerals["redstone"])
    b.altitude = AL.MANTLE
    b.bulk = BU.SMALL
    b.scarcity = SC.UNUSUAL
    b.save("copper-secondary-redstone")

    b.switch(minerals["gold"])
    b.altitude = AL.span(AL.CRUST, AL.MANTLE)
    b.bulk = BU.TINY
    b.scarcity = SC.RARE
    b.save("copper-tertiary-gold")

    # Gold Family ##############################################################

    b.start(minerals["marble"])
    b.biomeFilters = BF([GE.METAMORPHIC, HE.BOREAL, HU.DRY])
    b.save("gold-indicator")

    b.start(minerals["quartz"])
    b.altitude = AL.span(AL.CRAGS, AL.PEAKS)
    b.bulk = BU.MEDIUM
    b.scarcity = SC.SPARSE
    b.save("gold-primary-quartz")

    b.switch(minerals["lapis"])
    b.altitude = AL.span(AL.CRUST, AL.MANTLE)
    b.bulk = BU.SMALL
    b.scarcity = SC.UNUSUAL
    b.save("gold-secondary-lapis")

    b.switch(minerals["gold"])
    b.altitude = AL.CRUST
    b.bulk = BU.TINY
    b.scarcity = SC.RARE
    b.save("gold-tertiary-gold")

    b.switch(minerals["emerald"])
    b.altitude = AL.MANTLE
    b.bulk = BU.TINY
    b.scarcity = SC.RARE
    b.save("gold-quarternary-emerald")

    # Iron Family ##############################################################

    b.start(minerals["andesite"])
    b.biomeFilters = BF([GE.SEDIMENTARY, HE.TEMPERATE, HU.WET])
    b.save("iron-indicator")

    b.start(minerals["iron"])
    b.altitude = AL.CRUST
    b.bulk = BU.MEDIUM
    b.scarcity = SC.COMMON
    b.save("iron-primary-iron")

    b.switch(minerals["quartz"])
    b.altitude = AL.CRUST
    b.bulk = BU.SMALL
    b.scarcity = SC.UNUSUAL
    b.save("iron-secondary-quartz")

    b.switch(minerals["uranium"])
    b.altitude = AL.MANTLE
    b.bulk = BU.TINY
    b.scarcity = SC.RARE
    b.save("iron-tertiary-uranium")

    # Lead Family ##############################################################

    b.start(minerals["dolostone"])
    b.biomeFilters = BF([GE.SEDIMENTARY, HE.TEMPERATE, HU.DAMP])
    b.save("lead-indicator")

    b.start(minerals["lead"])
    b.altitude = AL.CRUST
    b.bulk = BU.MEDIUM
    b.scarcity = SC.SPARSE
    b.save("lead-primary-lead")

    b.switch(minerals["zinc"])
    b.altitude = AL.CRUST
    b.bulk = BU.SMALL
    b.scarcity = SC.SPARSE
    b.save("lead-secondary-zinc")

    b.switch(minerals["silver"])
    b.altitude = AL.span(AL.CRUST, AL.MANTLE)
    b.bulk = BU.SMALL
    b.scarcity = SC.UNUSUAL
    b.save("lead-tertiary-silver")

    # Plutonic Family ##########################################################

    b.start(minerals["sulfur"])
    b.altitude = AL.PLUTONIC
    b.save("plutonic-special-sulfur")

    b.switch(minerals["glowstone"])
    b.save("plutonic-special-glowstone")

    b.switch(minerals["diamond"])
    b.save("plutonic-special-diamond")

    # Salt Family ##############################################################

    b.start(minerals["chalk"])
    b.biomeFilters = BF([GE.SEDIMENTARY, HE.TROPICAL, HU.ARID])
    b.save("salt-indicator")

    b.switch(minerals["salt"])
    b.altitude = AL.span(AL.CRUST, AL.MANTLE)
    b.bulk = BU.LARGE
    b.depositType = DE.STRATA
    b.scarcity = SC.UNCOMMON
    b.save("salt-primary-salt")

    b.switch(minerals["nitrate"])
    b.altitude = AL.EVAPORITES
    b.bulk = BU.SMALL
    b.depositType = DE.DISK
    b.scarcity = SC.UNCOMMON
    b.save("salt-secondary-nitrate")

    # Soil Family ##############################################################

    b.start(minerals["loam"])
    b.altitude = AL.SOIL
    b.bulk = BU.HUGE
    b.biomeFilters = BF([SO.LOAMY])
    b.scarcity = SC.CARPET
    b.save("soil-special-loam")

    b.start(minerals["peat"])
    b.altitude = AL.SOIL
    b.bulk = BU.LARGE
    b.biomeFilters = BF([SO.PEATY])
    b.scarcity = SC.COMMON
    b.save("soil-special-peat")

    # Tin Family ###############################################################

    b.start(minerals["granite"])
    b.biomeFilters = BF([GE.IGNEOUS, HE.BOREAL, HU.DRY])
    b.save("tin-indicator")

    b.switch(minerals["tin"])
    b.altitude = AL.CRUST
    b.bulk = BU.MEDIUM
    b.scarcity = SC.SPARSE
    b.save("tin-primary-tin")

    b.switch(minerals["copper"])
    b.altitude = AL.span(AL.CRUST, AL.MANTLE)
    b.bulk = BU.SMALL
    b.scarcity = SC.UNUSUAL
    b.save("tin-secondary-copper")

"""

        vein    strata
absent      0       0
rare        0.024   0.5
unusual     0.12    2.0
sparse      0.3     5.0
uncommon    0.61    10.0
common      1.83    25.0
carpet      3.66    60.0

"""
