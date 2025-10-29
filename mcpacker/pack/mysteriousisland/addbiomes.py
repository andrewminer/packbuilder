from mcpacker.model.ecology.biome import Biome
from mcpacker.model.modpack import ModPack

import mcpacker.model.ecology.flora as FL
import mcpacker.model.ecology.geology as GE
import mcpacker.model.ecology.heat as HE
import mcpacker.model.ecology.humidity as HU
import mcpacker.model.ecology.soil as SO
import mcpacker.model.ecology.water as WA


# Functions ########################################################################################

def addBiomes(pack:ModPack):
    biomes = pack.world.biomes

    biomes.add(Biome("tombstone", "minecraft:badlands",
        FL.BARREN, GE.SEDIMENTARY, HE.SUBTROPICAL, HU.ARID, SO.CLAYEY, WA.INLAND
    ))

    biomes.add(Biome("rangoon", "minecraft:bamboo_jungle",
        FL.FOREST, GE.SEDIMENTARY, HE.TROPICAL, HU.WET, SO.ACIDIC, WA.INLAND
    ))

    biomes.add(Biome("nice", "minecraft:beach",
        FL.BARREN, GE.SEDIMENTARY, HE.SUBTROPICAL, HU.DAMP, SO.SANDY, WA.COAST
    ))

    biomes.add(Biome("helsinki", "minecraft:birch_forest",
        FL.FOREST, GE.SEDIMENTARY, HE.TEMPERATE, HU.DAMP, SO.ACIDIC, WA.INLAND
    ))

    biomes.add(Biome("tokyo", "minecraft:cherry_grove",
        FL.CLEARING, GE.SEDIMENTARY, HE.TEMPERATE, HU.DAMP, SO.ROCKY, WA.INLAND
    ))

    biomes.add(Biome("boston", "minecraft:cold_ocean",
        FL.BARREN, GE.SEDIMENTARY, HE.BOREAL, HU.WET, SO.CLAYEY, WA.OCEAN
    ))

    biomes.add(Biome("freiburg", "minecraft:dark_forest",
        FL.CANOPY, GE.METAMORPHIC, HE.TEMPERATE, HU.SOAKED, SO.CLAYEY, WA.INLAND
    ))

    biomes.add(Biome("halifax", "minecraft:deep_cold_ocean",
        FL.BARREN, GE.METAMORPHIC, HE.BOREAL, HU.WET, SO.CLAYEY, WA.OCEAN
    ))

    biomes.add(Biome("tromso", "minecraft:deep_frozen_ocean",
        FL.BARREN, GE.METAMORPHIC, HE.FROZEN, HU.DAMP, SO.CLAYEY, WA.OCEAN
    ))

    biomes.add(Biome("havana", "minecraft:deep_lukewarm_ocean",
        FL.BARREN, GE.SEDIMENTARY, HE.SUBTROPICAL, HU.WET, SO.CLAYEY, WA.OCEAN
    ))

    biomes.add(Biome("auckland", "minecraft:deep_ocean",
        FL.BARREN, GE.IGNEOUS, HE.TEMPERATE, HU.DAMP, SO.CLAYEY, WA.OCEAN
    ))

    biomes.add(Biome("timbuktu", "minecraft:desert",
        FL.BARREN, GE.SEDIMENTARY, HE.TROPICAL, HU.ARID, SO.SANDY, WA.INLAND
    ))

    biomes.add(Biome("canoncity", "minecraft:eroded_badlands",
        FL.BARREN, GE.IGNEOUS, HE.SUBTROPICAL, HU.ARID, SO.ROCKY, WA.INLAND
    ))

    biomes.add(Biome("haarlem", "minecraft:flower_forest",
        FL.CLEARING, GE.SEDIMENTARY, HE.TEMPERATE, HU.WET, SO.LOAMY, WA.INLAND
    ))

    biomes.add(Biome("sherwood", "minecraft:forest",
        FL.FOREST, GE.SEDIMENTARY, HE.TEMPERATE, HU.WET, SO.LOAMY, WA.INLAND
    ))

    biomes.add(Biome("archangel", "minecraft:frozen_ocean",
        FL.BARREN, GE.IGNEOUS, HE.FROZEN, HU.DAMP, SO.SANDY, WA.OCEAN
    ))

    biomes.add(Biome("chamonix", "minecraft:frozen_peaks",
        FL.BARREN, GE.IGNEOUS, HE.FROZEN, HU.DAMP, SO.ROCKY, WA.INLAND
    ))

    biomes.add(Biome("winnipeg", "minecraft:frozen_river",
        FL.BARREN, GE.IGNEOUS, HE.FROZEN, HU.DAMP, SO.SANDY, WA.RIVER
    ))

    biomes.add(Biome("umea", "minecraft:grove",
        FL.CLEARING, GE.METAMORPHIC, HE.FROZEN, HU.DAMP, SO.ACIDIC, WA.INLAND
    ))

    biomes.add(Biome("hammerfest", "minecraft:ice_spikes",
        FL.BARREN, GE.METAMORPHIC, HE.FROZEN, HU.WET, SO.ROCKY, WA.INLAND
    ))

    biomes.add(Biome("jackson", "minecraft:jagged_peaks",
        FL.BARREN, GE.METAMORPHIC, HE.BOREAL, HU.DRY, SO.ROCKY, WA.INLAND
    ))

    biomes.add(Biome("singapore", "minecraft:jungle",
        FL.CANOPY, GE.IGNEOUS, HE.TROPICAL, HU.SOAKED, SO.ACIDIC, WA.INLAND
    ))

    biomes.add(Biome("bombay", "minecraft:lukewarm_ocean",
        FL.BARREN, GE.IGNEOUS, HE.SUBTROPICAL, HU.WET, SO.SANDY, WA.OCEAN
    ))

    biomes.add(Biome("calcutta", "minecraft:mangrove_swamp",
        FL.FOREST, GE.SEDIMENTARY, HE.TROPICAL, HU.SOAKED, SO.CLAYEY, WA.SWAMP
    ))

    biomes.add(Biome("innsbruck", "minecraft:meadow",
        FL.FIELD, GE.METAMORPHIC, HE.BOREAL, HU.DAMP, SO.LOAMY, WA.INLAND
    ))

    biomes.add(Biome("krakatoa", "minecraft:mushroom_fields",
        FL.CLEARING, GE.IGNEOUS, HE.TROPICAL, HU.WET, SO.FUNGAL, WA.INLAND
    ))

    biomes.add(Biome("sanfrancisco", "minecraft:ocean",
        FL.BARREN, GE.IGNEOUS, HE.TEMPERATE, HU.WET, SO.SANDY, WA.OCEAN
    ))

    biomes.add(Biome("minsk", "minecraft:old_growth_birch_forest",
        FL.FOREST, GE.SEDIMENTARY, HE.TEMPERATE, HU.DAMP, SO.ACIDIC, WA.INLAND
    ))

    biomes.add(Biome("stpetersburg", "minecraft:old_growth_pine_taiga",
        FL.FOREST, GE.METAMORPHIC, HE.BOREAL, HU.DAMP, SO.ACIDIC, WA.INLAND
    ))

    biomes.add(Biome("juneau", "minecraft:old_growth_spruce_taiga",
        FL.FOREST, GE.METAMORPHIC, HE.BOREAL, HU.DAMP, SO.PEATY, WA.INLAND
    ))

    biomes.add(Biome("kansascity", "minecraft:plains",
        FL.FIELD, GE.SEDIMENTARY, HE.TEMPERATE, HU.DAMP, SO.LOAMY, WA.INLAND
    ))

    biomes.add(Biome("memphis", "minecraft:river",
        FL.BARREN, GE.SEDIMENTARY, HE.TEMPERATE, HU.WET, SO.SANDY, WA.RIVER
    ))

    biomes.add(Biome("katanga", "minecraft:savanna",
        FL.FIELD, GE.SEDIMENTARY, HE.SUBTROPICAL, HU.DRY, SO.SANDY, WA.INLAND
    ))

    biomes.add(Biome("khartoum", "minecraft:savanna_plateau",
        FL.FIELD, GE.SEDIMENTARY, HE.SUBTROPICAL, HU.DRY, SO.SANDY, WA.INLAND
    ))

    biomes.add(Biome("nuuk", "minecraft:snowy_beach",
        FL.BARREN, GE.METAMORPHIC, HE.FROZEN, HU.DAMP, SO.SANDY, WA.COAST
    ))

    biomes.add(Biome("rovaniemi", "minecraft:snowy_plains",
        FL.FIELD, GE.SEDIMENTARY, HE.FROZEN, HU.DAMP, SO.PEATY, WA.INLAND
    ))

    biomes.add(Biome("zurich", "minecraft:snowy_slopes",
        FL.BARREN, GE.METAMORPHIC, HE.FROZEN, HU.DAMP, SO.ROCKY, WA.INLAND
    ))

    biomes.add(Biome("kola", "minecraft:snowy_taiga",
        FL.FOREST, GE.METAMORPHIC, HE.FROZEN, HU.DAMP, SO.ACIDIC, WA.INLAND
    ))

    biomes.add(Biome("madras", "minecraft:sparse_jungle",
        FL.CLEARING, GE.METAMORPHIC, HE.TROPICAL, HU.SOAKED, SO.ACIDIC, WA.INLAND
    ))

    biomes.add(Biome("quito", "minecraft:stony_peaks",
        FL.BARREN, GE.IGNEOUS, HE.BOREAL, HU.DRY, SO.ROCKY, WA.INLAND
    ))

    biomes.add(Biome("plymouth", "minecraft:stony_shore",
        FL.BARREN, GE.METAMORPHIC, HE.TEMPERATE, HU.DAMP, SO.ROCKY, WA.COAST
    ))

    biomes.add(Biome("stlouis", "minecraft:sunflower_plains",
        FL.FIELD, GE.SEDIMENTARY, HE.TEMPERATE, HU.DAMP, SO.SANDY, WA.INLAND
    ))

    biomes.add(Biome("neworleans", "minecraft:swamp",
        FL.CLEARING, GE.SEDIMENTARY, HE.TEMPERATE, HU.SOAKED, SO.PEATY, WA.SWAMP
    ))

    biomes.add(Biome("irkutsk", "minecraft:taiga",
        FL.FOREST, GE.METAMORPHIC, HE.BOREAL, HU.DAMP, SO.ACIDIC, WA.INLAND
    ))

    biomes.add(Biome("nassau", "minecraft:warm_ocean",
        FL.BARREN, GE.SEDIMENTARY, HE.TROPICAL, HU.SOAKED, SO.SANDY, WA.OCEAN
    ))

    biomes.add(Biome("stirling", "minecraft:windswept_forest",
        FL.CLEARING, GE.SEDIMENTARY, HE.BOREAL, HU.DAMP, SO.ACIDIC, WA.INLAND
    ))

    biomes.add(Biome("inverness", "minecraft:windswept_gravelly_hills",
        FL.BARREN, GE.METAMORPHIC, HE.BOREAL, HU.DRY, SO.ROCKY, WA.INLAND
    ))

    biomes.add(Biome("cornwall", "minecraft:windswept_hills",
        FL.BARREN, GE.IGNEOUS, HE.BOREAL, HU.DRY, SO.ROCKY, WA.INLAND
    ))

    biomes.add(Biome("moab", "minecraft:windswept_savanna",
        FL.FIELD, GE.SEDIMENTARY, HE.SUBTROPICAL, HU.DRY, SO.ROCKY, WA.INLAND
    ))

    biomes.add(Biome("santafe", "minecraft:wooded_badlands",
        FL.CLEARING, GE.SEDIMENTARY, HE.SUBTROPICAL, HU.DRY, SO.CLAYEY, WA.INLAND
    ))
