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
    b.biomeFilters = BF([HE.TROPICAL, (HU.WET, HU.SOAKED)], [SO.FUNGAL, WA.OCEAN])
    b.save("aluminum-indicator-basalt")

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
    b.save("coal-indicator-tuff")

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

    # Copper (oxidizedcap) Family ##############################################

    b.start(minerals["sandstone"])
    b.biomeFilters = BF([GE.SEDIMENTARY, HE.SUBTROPICAL, (HU.ARID, HU.DRY)])
    b.save("copper-oxidizedcap-indicator-sandstone")

    b.switch(minerals["copper"])
    b.altitude = AL.CRUST
    b.bulk = BU.MEDIUM
    b.scarcity = SC.UNCOMMON
    b.save("copper-oxidizedcap-primary-copper")

    b.switch(minerals["iron"])
    b.altitude = AL.CRUST
    b.bulk = BU.SMALL
    b.scarcity = SC.UNUSUAL
    b.save("copper-oxidizedcap-secondary-iron")

    b.switch(minerals["sulfur"])
    b.altitude = AL.CRUST
    b.bulk = BU.TINY
    b.scarcity = SC.RARE
    b.save("copper-oxidizedcap-tertiary-sulfur")

    # Copper (porphyry) Family ##################################################

    b.start(minerals["diorite"])
    b.biomeFilters = BF([GE.IGNEOUS, (HE.SUBTROPICAL, HE.FROZEN), SO.ROCKY])
    b.save("copper-porphyry-indicator-diorite")

    b.switch(minerals["copper"])
    b.altitude = AL.CRUST
    b.bulk = BU.MEDIUM
    b.scarcity = SC.UNCOMMON
    b.save("copper-porphyry-primary-copper")

    b.switch(minerals["redstone"])
    b.altitude = AL.MANTLE
    b.bulk = BU.SMALL
    b.scarcity = SC.UNUSUAL
    b.save("copper-porphyry-secondary-redstone")

    b.switch(minerals["gold"])
    b.altitude = AL.span(AL.CRUST, AL.MANTLE)
    b.bulk = BU.TINY
    b.scarcity = SC.RARE
    b.save("copper-porphyry-tertiary-gold")

    # Gold Family ##############################################################

    b.start(minerals["marble"])
    b.biomeFilters = BF([GE.METAMORPHIC, (HE.BOREAL, HE.FROZEN), SO.ROCKY])
    b.save("gold-indicator-marble")

    b.switch(minerals["quartz"])
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

    # Iron (banded) Family ##############################################################

    b.start(minerals["diorite"])
    b.biomeFilters = BF(
        [FL.within(FL.CANOPY, FL.CLEARING), GE.METAMORPHIC, (HE.BOREAL, HE.FROZEN)]
    )
    b.save("iron-banded-indicator-diorite")

    b.switch(minerals["iron"])
    b.altitude = AL.span(AL.OVERBURDEN, AL.CRUST)
    b.bulk = BU.LARGE
    b.scarcity = SC.UNCOMMON
    b.save("iron-banded-primary-iron")

    b.switch(minerals["quartz"])
    b.altitude = AL.span(AL.OVERBURDEN, AL.CRUST)
    b.bulk = BU.MEDIUM
    b.scarcity = SC.UNUSUAL
    b.save("iron-banded-secondary-quartz")

    b.switch(minerals["uranium"])
    b.altitude = AL.CRUST
    b.bulk = BU.SMALL
    b.scarcity = SC.UNCOMMON
    b.save("iron-banded-tertiary-uranium")

    # Iron (bog) Family ##############################################################

    b.start(minerals["andesite"])
    b.biomeFilters = BF([FL.FOREST, GE.SEDIMENTARY, HE.TEMPERATE], [WA.SWAMP])
    b.save("iron-bog-indicator-andesite")

    b.switch(minerals["coal"])
    b.altitude = AL.SOIL
    b.bulk = BU.SMALL
    b.depositType = DE.DISK
    b.scarcity = SC.UNCOMMON
    b.save("iron-bog-primary-coal")

    b.switch(minerals["iron"])
    b.altitude = AL.span(AL.SOIL, AL.DUNES)
    b.bulk = BU.MEDIUM
    b.depositType = DE.DISK
    b.scarcity = SC.UNCOMMON
    b.save("iron-bog-secondary-iron")

    b.switch(minerals["uranium"])
    b.altitude = AL.SOIL
    b.bulk = BU.SMALL
    b.scarcity = SC.RARE
    b.save("iron-bog-tertiary-uranium")

    # Lead Family ##############################################################

    b.start(minerals["dolostone"])
    b.biomeFilters = BF([FL.FIELD, GE.SEDIMENTARY, HE.TEMPERATE, HU.DAMP])
    b.save("lead-indicator-dolostone")

    b.switch(minerals["lead"])
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

    # Ocean (igneous) Family ###################################################

    b.start(minerals["basalt"])
    b.biomeFilters = BF([GE.IGNEOUS, WA.OCEAN])
    b.save("ocean-igneous-indicator-basalt")

    b.switch(minerals["tin"])
    b.altitude = AL.CRUST
    b.bulk = BU.MEDIUM
    b.depositType = DE.VEIN
    b.scarcity = SC.UNCOMMON
    b.save("ocean-igneous-primary-tin")

    b.switch(minerals["copper"])
    b.altitude = AL.CRUST
    b.bulk = BU.SMALL
    b.depositType = DE.VEIN
    b.scarcity = SC.SPARSE
    b.save("ocean-igneous-secondary-copper")

    b.switch(minerals["diamond"])
    b.altitude = AL.MANTLE
    b.bulk = BU.TINY
    b.depositType = DE.VEIN
    b.scarcity = SC.RARE
    b.save("ocean-igneous-tertiary-diamond")

    # Ocean (metamorphic) Family ###############################################

    b.start(minerals["marble"])
    b.biomeFilters = BF([GE.METAMORPHIC, WA.OCEAN])
    b.save("ocean-metamorphic-indicator-marble")

    b.switch(minerals["quartz"])
    b.altitude = AL.CRUST
    b.bulk = BU.LARGE
    b.depositType = DE.STRATA
    b.scarcity = SC.COMMON
    b.save("ocean-metamorphic-primary-quartz")

    b.switch(minerals["gold"])
    b.altitude = AL.CRUST
    b.bulk = BU.SMALL
    b.depositType = DE.VEIN
    b.scarcity = SC.UNUSUAL
    b.save("ocean-metamorphic-secondary-gold")

    b.switch(minerals["emerald"])
    b.altitude = AL.MANTLE
    b.bulk = BU.TINY
    b.depositType = DE.VEIN
    b.scarcity = SC.RARE
    b.save("ocean-metamorphic-tertiary-emerald")

    # Ocean (sedimentary) Family ###############################################

    b.start(minerals["sandstone"])
    b.biomeFilters = BF([GE.SEDIMENTARY, WA.OCEAN])
    b.save("ocean-sedimentary-indicator-sandstone")

    b.switch(minerals["iron"])
    b.altitude = AL.CRUST
    b.bulk = BU.MEDIUM
    b.depositType = DE.STRATA
    b.scarcity = SC.UNCOMMON
    b.save("ocean-sedimentary-primary-iron")

    b.switch(minerals["nickel"])
    b.altitude = AL.CRUST
    b.bulk = BU.SMALL
    b.depositType = DE.DISK
    b.scarcity = SC.SPARSE
    b.save("ocean-sedimentary-secondary-nickel")

    b.switch(minerals["lapis"])
    b.altitude = AL.CRUST
    b.bulk = BU.LARGE
    b.depositType = DE.VEIN
    b.scarcity = SC.SPARSE
    b.save("ocean-sedimentary-tertiary-lapis")

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
    b.save("salt-indicator-chalk")

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

    # Silver Family ###############################################################

    b.start(minerals["diorite"])
    b.biomeFilters = BF([GE.METAMORPHIC, HE.TEMPERATE, HU.SOAKED])
    b.save("silver-indicator-diorite")

    b.switch(minerals["quartz"])
    b.altitude = AL.span(AL.CRUST, AL.LOWLANDS)
    b.bulk = BU.MEDIUM
    b.scarcity = SC.UNCOMMON
    b.save("silver-primary-quartz")

    b.switch(minerals["lead"])
    b.altitude = AL.span(AL.SOIL, AL.OVERBURDEN)
    b.bulk = BU.MEDIUM
    b.scarcity = SC.SPARSE
    b.save("silver-secondary-lead")

    b.switch(minerals["silver"])
    b.altitude = AL.CRUST
    b.bulk = BU.SMALL
    b.scarcity = SC.SPARSE
    b.save("silver-tertiary-silver")

    # Tin Family ###############################################################

    b.start(minerals["granite"])
    b.biomeFilters = BF([GE.IGNEOUS, HE.BOREAL, SO.ROCKY])
    b.save("tin-indicator-granite")

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

    # Volcanic Family ##########################################################

    b.start(minerals["basalt"])
    b.biomeFilters = BF([GE.IGNEOUS, SO.FUNGAL])
    b.save("volcanic-indicator-basalt")

    b.switch(minerals["sulfur"])
    b.altitude = AL.span(AL.LOWLANDS, AL.CRUST)
    b.bulk = BU.MEDIUM
    b.scarcity = SC.UNCOMMON
    b.save("volcanic-primary-sulfur")

    b.switch(minerals["magma"])
    b.altitude = AL.span(AL.SOIL, AL.CRUST)
    b.bulk = BU.MEDIUM
    b.scarcity = SC.SPARSE
    b.save("volcanic-secondary-magma")

    b.switch(minerals["diamond"])
    b.altitude = AL.span(AL.CRUST, AL.MANTLE)
    b.bulk = BU.TINY
    b.depositType = DE.VEIN
    b.scarcity = SC.UNUSUAL
    b.save("volcanic-tertiary-diamond")

# TODO: All the Taiga biomes are missing mineral deposits
# TODO: Mushroom Fields doesn't have any minerals

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
