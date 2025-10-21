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

    biomes.add(Biome("aberdeen", "minecraft:windswept_gravelly_hills",
        FL.BARREN, GE.METAMORPHIC, HE.BOREAL, HU.DAMP, SO.ROCKY, WA.INLAND
    ))

    biomes.add(Biome("archangel", "minecraft:frozen_ocean",
        FL.BARREN, GE.SEDIMENTARY, HE.FROZEN, HU.WET, SO.SANDY, WA.OCEAN
    ))

    biomes.add(Biome("aspen", "minecraft:frozen_peaks",
        FL.BARREN, GE.IGNEOUS, HE.FROZEN, HU.WET, SO.ROCKY, WA.INLAND
    ))

    biomes.add(Biome("bombay", "minecraft:lukewarm_ocean",
        FL.BARREN, GE.SEDIMENTARY, HE.SUBTROPICAL, HU.WET, SO.SANDY, WA.OCEAN
    ))

    biomes.add(Biome("boston", "minecraft:cold_ocean",
        FL.BARREN, GE.SEDIMENTARY, HE.BOREAL, HU.WET, SO.CLAYEY, WA.OCEAN
    ))

    biomes.add(Biome("bryce", "minecraft:eroded_badlands",
        FL.BARREN, GE.SEDIMENTARY, HE.SUBTROPICAL, HU.DRY, SO.CLAYEY, WA.INLAND
    ))

    biomes.add(Biome("calcutta", "minecraft:mangrove_swamp",
        FL.FOREST, GE.SEDIMENTARY, HE.TROPICAL, HU.WET, SO.CLAYEY, WA.SWAMP
    ))

    biomes.add(Biome("cornwall", "minecraft:windswept_hills",
        FL.BARREN, GE.METAMORPHIC, HE.BOREAL, HU.DAMP, SO.ROCKY, WA.INLAND
    ))

    biomes.add(Biome("dakar", "minecraft:savanna",
        FL.FIELD, GE.SEDIMENTARY, HE.SUBTROPICAL, HU.DRY, SO.SANDY, WA.INLAND
    ))

    biomes.add(Biome("duluth", "minecraft:frozen_river",
        FL.BARREN, GE.SEDIMENTARY, HE.FROZEN, HU.WET, SO.SANDY, WA.RIVER
    ))

    biomes.add(Biome("khartoum", "minecraft:savanna_plateau",
        FL.FIELD, GE.IGNEOUS, HE.SUBTROPICAL, HU.DRY, SO.SANDY, WA.INLAND
    ))

    biomes.add(Biome("freiburg", "minecraft:dark_forest",
        FL.CANOPY, GE.SEDIMENTARY, HE.TEMPERATE, HU.WET, SO.CLAYEY, WA.INLAND
    ))

    biomes.add(Biome("glasgow", "minecraft:windswept_forest",
        FL.CLEARING, GE.METAMORPHIC, HE.BOREAL, HU.DAMP, SO.ACIDIC, WA.INLAND
    ))

    biomes.add(Biome("haarlem", "minecraft:flower_forest",
        FL.CLEARING, GE.SEDIMENTARY, HE.TEMPERATE, HU.DAMP, SO.LOAMY, WA.INLAND
    ))

    biomes.add(Biome("halifax", "minecraft:deep_cold_ocean",
        FL.BARREN, GE.SEDIMENTARY, HE.BOREAL, HU.WET, SO.SANDY, WA.OCEAN
    ))

    biomes.add(Biome("hammerfest", "minecraft:ice_spikes",
        FL.BARREN, GE.METAMORPHIC, HE.FROZEN, HU.WET, SO.ROCKY, WA.INLAND
    ))

    biomes.add(Biome("havana", "minecraft:deep_lukewarm_ocean",
        FL.BARREN, GE.SEDIMENTARY, HE.SUBTROPICAL, HU.WET, SO.SANDY, WA.OCEAN
    ))

    biomes.add(Biome("tahiti", "minecraft:mushroom_fields",
        FL.CLEARING, GE.IGNEOUS, HE.TROPICAL, HU.WET, SO.FUNGAL, WA.INLAND
    ))

    biomes.add(Biome("honolulu", "minecraft:deep_ocean",
        FL.BARREN, GE.IGNEOUS, HE.TEMPERATE, HU.WET, SO.SANDY, WA.OCEAN
    ))

    biomes.add(Biome("innsbruck", "minecraft:meadow",
        FL.FIELD, GE.IGNEOUS, HE.BOREAL, HU.DAMP, SO.LOAMY, WA.INLAND
    ))

    biomes.add(Biome("irkutsk", "minecraft:taiga",
        FL.FOREST, GE.METAMORPHIC, HE.BOREAL, HU.DAMP, SO.ACIDIC, WA.INLAND
    ))

    biomes.add(Biome("jackson", "minecraft:jagged_peaks",
        FL.BARREN, GE.METAMORPHIC, HE.BOREAL, HU.DRY, SO.ROCKY, WA.INLAND
    ))

    biomes.add(Biome("juneau", "minecraft:old_growth_spruce_taiga",
        FL.FOREST, GE.METAMORPHIC, HE.BOREAL, HU.DAMP, SO.PEATY, WA.INLAND
    ))

    biomes.add(Biome("kansascity", "minecraft:plains",
        FL.FIELD, GE.SEDIMENTARY, HE.TEMPERATE, HU.DAMP, SO.LOAMY, WA.INLAND
    ))

    biomes.add(Biome("kola", "minecraft:snowy_taiga",
        FL.FOREST, GE.METAMORPHIC, HE.FROZEN, HU.DAMP, SO.ACIDIC, WA.INLAND
    ))

    biomes.add(Biome("kyoto", "minecraft:cherry_grove",
        FL.CLEARING, GE.SEDIMENTARY, HE.TEMPERATE, HU.DAMP, SO.ROCKY, WA.INLAND
    ))

    biomes.add(Biome("madras", "minecraft:sparse_jungle",
        FL.CLEARING, GE.SEDIMENTARY, HE.TROPICAL, HU.WET, SO.ACIDIC, WA.INLAND
    ))

    biomes.add(Biome("memphis", "minecraft:river",
        FL.BARREN, GE.SEDIMENTARY, HE.TEMPERATE, HU.WET, SO.SANDY, WA.RIVER
    ))

    biomes.add(Biome("minsk", "minecraft:old_growth_birch_forest",
        FL.FOREST, GE.SEDIMENTARY, HE.TEMPERATE, HU.DAMP, SO.ACIDIC, WA.INLAND
    ))

    biomes.add(Biome("moab", "minecraft:windswept_savanna",
        FL.FIELD, GE.IGNEOUS, HE.SUBTROPICAL, HU.DRY, SO.ROCKY, WA.INLAND
    ))

    biomes.add(Biome("mobile", "minecraft:swamp",
        FL.CLEARING, GE.SEDIMENTARY, HE.TEMPERATE, HU.WET, SO.PEATY, WA.SWAMP
    ))

    biomes.add(Biome("moscow", "minecraft:snowy_plains",
        FL.FIELD, GE.SEDIMENTARY, HE.FROZEN, HU.DAMP, SO.PEATY, WA.INLAND
    ))

    biomes.add(Biome("nassau", "minecraft:warm_ocean",
        FL.BARREN, GE.SEDIMENTARY, HE.TROPICAL, HU.WET, SO.SANDY, WA.COAST
    ))

    biomes.add(Biome("nice", "minecraft:beach",
        FL.BARREN, GE.SEDIMENTARY, HE.SUBTROPICAL, HU.DAMP, SO.SANDY, WA.COAST
    ))

    biomes.add(Biome("nuuk", "minecraft:snowy_beach",
        FL.BARREN, GE.SEDIMENTARY, HE.FROZEN, HU.DAMP, SO.SANDY, WA.COAST
    ))

    biomes.add(Biome("perm", "minecraft:old_growth_pine_taiga",
        FL.FOREST, GE.METAMORPHIC, HE.BOREAL, HU.DAMP, SO.ACIDIC, WA.INLAND
    ))

    biomes.add(Biome("timbuktu", "minecraft:desert",
        FL.BARREN, GE.SEDIMENTARY, HE.TROPICAL, HU.DRY, SO.SANDY, WA.INLAND
    ))

    biomes.add(Biome("plymouth", "minecraft:stony_shore",
        FL.BARREN, GE.METAMORPHIC, HE.TEMPERATE, HU.DAMP, SO.ROCKY, WA.COAST
    ))

    biomes.add(Biome("sherwood", "minecraft:forest",
        FL.FOREST, GE.SEDIMENTARY, HE.TEMPERATE, HU.DAMP, SO.LOAMY, WA.INLAND
    ))

    biomes.add(Biome("quito", "minecraft:stony_peaks",
        FL.BARREN, GE.IGNEOUS, HE.BOREAL, HU.DRY, SO.ROCKY, WA.INLAND
    ))

    biomes.add(Biome("rangoon", "minecraft:bamboo_jungle",
        FL.FOREST, GE.SEDIMENTARY, HE.TROPICAL, HU.WET, SO.ACIDIC, WA.INLAND
    ))

    biomes.add(Biome("sanfrancisco", "minecraft:ocean",
        FL.BARREN, GE.SEDIMENTARY, HE.TEMPERATE, HU.WET, SO.SANDY, WA.OCEAN
    ))

    biomes.add(Biome("santafe", "minecraft:wooded_badlands",
        FL.CLEARING, GE.SEDIMENTARY, HE.SUBTROPICAL, HU.DRY, SO.CLAYEY, WA.INLAND
    ))

    biomes.add(Biome("singapore", "minecraft:jungle",
        FL.CANOPY, GE.SEDIMENTARY, HE.TROPICAL, HU.WET, SO.ACIDIC, WA.INLAND
    ))

    biomes.add(Biome("tombstone", "minecraft:badlands",
        FL.BARREN, GE.SEDIMENTARY, HE.SUBTROPICAL, HU.DRY, SO.CLAYEY, WA.INLAND
    ))

    biomes.add(Biome("stlouis", "minecraft:sunflower_plains",
        FL.FIELD, GE.SEDIMENTARY, HE.TEMPERATE, HU.DAMP, SO.LOAMY, WA.INLAND
    ))

    biomes.add(Biome("tromso", "minecraft:deep_frozen_ocean",
        FL.BARREN, GE.SEDIMENTARY, HE.FROZEN, HU.WET, SO.SANDY, WA.OCEAN
    ))

    biomes.add(Biome("umea", "minecraft:grove",
        FL.CLEARING, GE.METAMORPHIC, HE.FROZEN, HU.DAMP, SO.ACIDIC, WA.INLAND
    ))

    biomes.add(Biome("warsaw", "minecraft:birch_forest",
        FL.FOREST, GE.SEDIMENTARY, HE.TEMPERATE, HU.DAMP, SO.ACIDIC, WA.INLAND
    ))

    biomes.add(Biome("zurich", "minecraft:snowy_slopes",
        FL.BARREN, GE.METAMORPHIC, HE.FROZEN, HU.DAMP, SO.ROCKY, WA.INLAND
    ))
