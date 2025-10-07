from mcpacker.model.core.ecology.biome import Biome
from mcpacker.model.core.ecology.biomecatalog import BiomeCatalog
from mcpacker.model.core.ecology.biomefilter import BiomeFilter

import mcpacker.model.core.ecology.flora    as FL
import mcpacker.model.core.ecology.geology  as GE
import mcpacker.model.core.ecology.heat     as HE
import mcpacker.model.core.ecology.humidity as HU
import mcpacker.model.core.ecology.soil     as SO
import mcpacker.model.core.ecology.water    as WA

# Constants ########################################################################################

CATALOG = BiomeCatalog([
    Biome("aberdeen", "minecraft:windswept_gravelly_hills",
        FL.BARREN, GE.METAMORPHIC, HE.BOREAL, HU.DAMP, SO.ROCKY, WA.INLAND
    ),
    Biome("archangel", "minecraft:frozen_ocean",
        FL.BARREN, GE.SEDIMENTARY, HE.FROZEN, HU.WET, SO.SANDY, WA.OCEAN
    ),
    Biome("aspen", "minecraft:frozen_peaks",
        FL.BARREN, GE.IGNEOUS, HE.FROZEN, HU.WET, SO.ROCKY, WA.INLAND
    ),
    Biome("bombay", "minecraft:lukewarm_ocean",
        FL.BARREN, GE.SEDIMENTARY, HE.SUBTROPICAL, HU.WET, SO.SANDY, WA.OCEAN
    ),
    Biome("boston", "minecraft:cold_ocean",
        FL.BARREN, GE.SEDIMENTARY, HE.BOREAL, HU.WET, SO.CLAYEY, WA.OCEAN
    ),
    Biome("bryce", "minecraft:eroded_badlands",
        FL.BARREN, GE.SEDIMENTARY, HE.SUBTROPICAL, HU.DRY, SO.CLAYEY, WA.INLAND
    ),
    Biome("calcutta", "minecraft:mangrove_swamp",
        FL.FOREST, GE.SEDIMENTARY, HE.SUBTROPICAL, HU.WET, SO.CLAYEY, WA.INLAND
    ),
    Biome("cornwall", "minecraft:windswept_hills",
        FL.BARREN, GE.METAMORPHIC, HE.BOREAL, HU.DAMP, SO.ROCKY, WA.INLAND
    ),
    Biome("dallas", "minecraft:savanna",
        FL.FIELD, GE.SEDIMENTARY, HE.SUBTROPICAL, HU.DRY, SO.SANDY, WA.INLAND
    ),
    Biome("duluth", "minecraft:frozen_river",
        FL.BARREN, GE.SEDIMENTARY, HE.FROZEN, HU.WET, SO.SANDY, WA.RIVER
    ),
    Biome("durango", "minecraft:savanna_plateau",
        FL.FIELD, GE.IGNEOUS, HE.SUBTROPICAL, HU.DRY, SO.SANDY, WA.INLAND
    ),
    Biome("freiburg", "minecraft:dark_forest",
        FL.CANOPY, GE.SEDIMENTARY, HE.TEMPERATE, HU.WET, SO.CLAYEY, WA.INLAND
    ),
    Biome("glasgow", "minecraft:windswept_forest",
        FL.CLEARING, GE.METAMORPHIC, HE.BOREAL, HU.DAMP, SO.ACIDIC, WA.INLAND
    ),
    Biome("haarlem", "minecraft:flower_forest",
        FL.CLEARING, GE.SEDIMENTARY, HE.TEMPERATE, HU.DAMP, SO.LOAMY, WA.INLAND
    ),
    Biome("halifax", "minecraft:deep_cold_ocean",
        FL.BARREN, GE.SEDIMENTARY, HE.BOREAL, HU.WET, SO.SANDY, WA.OCEAN
    ),
    Biome("hammerfest", "minecraft:ice_spikes",
        FL.BARREN, GE.METAMORPHIC, HE.FROZEN, HU.WET, SO.ROCKY, WA.INLAND
    ),
    Biome("havana", "minecraft:deep_lukewarm_ocean",
        FL.BARREN, GE.SEDIMENTARY, HE.SUBTROPICAL, HU.WET, SO.SANDY, WA.OCEAN
    ),
    Biome("hilo", "minecraft:mushroom_fields",
        FL.CLEARING, GE.IGNEOUS, HE.SUBTROPICAL, HU.WET, SO.FUNGAL, WA.INLAND
    ),
    Biome("honolulu", "minecraft:deep_ocean",
        FL.BARREN, GE.SEDIMENTARY, HE.TEMPERATE, HU.WET, SO.SANDY, WA.OCEAN
    ),
    Biome("innnesbruk", "minecraft:meadow",
        FL.FIELD, GE.SEDIMENTARY, HE.BOREAL, HU.DAMP, SO.PEATY, WA.INLAND
    ),
    Biome("irkutsk", "minecraft:taiga",
        FL.FOREST, GE.METAMORPHIC, HE.BOREAL, HU.DAMP, SO.ACIDIC, WA.INLAND
    ),
    Biome("jackson", "minecraft:jagged_peaks",
        FL.BARREN, GE.METAMORPHIC, HE.BOREAL, HU.DRY, SO.ROCKY, WA.INLAND
    ),
    Biome("juneau", "minecraft:old_growth_spruce_taiga",
        FL.FOREST, GE.METAMORPHIC, HE.BOREAL, HU.DAMP, SO.PEATY, WA.INLAND
    ),
    Biome("kansascity", "minecraft:plains",
        FL.FIELD, GE.SEDIMENTARY, HE.TEMPERATE, HU.DAMP, SO.LOAMY, WA.INLAND
    ),
    Biome("kola", "minecraft:snowy_taiga",
        FL.BARREN, GE.METAMORPHIC, HE.FROZEN, HU.DAMP, SO.ACIDIC, WA.INLAND
    ),
    Biome("kyoto", "minecraft:cherry_grove",
        FL.CLEARING, GE.SEDIMENTARY, HE.TEMPERATE, HU.DAMP, SO.ROCKY, WA.INLAND
    ),
    Biome("madras", "minecraft:sparse_jungle",
        FL.CLEARING, GE.SEDIMENTARY, HE.TROPICAL, HU.WET, SO.ACIDIC, WA.INLAND
    ),
    Biome("memphis", "minecraft:river",
        FL.CLEARING, GE.SEDIMENTARY, HE.TEMPERATE, HU.WET, SO.SANDY, WA.RIVER
    ),
    Biome("minsk", "minecraft:old_growth_birch_forest",
        FL.FOREST, GE.SEDIMENTARY, HE.TEMPERATE, HU.DAMP, SO.ACIDIC, WA.INLAND
    ),
    Biome("moab", "minecraft:windswept_savanna",
        FL.FIELD, GE.IGNEOUS, HE.SUBTROPICAL, HU.DRY, SO.ROCKY, WA.INLAND
    ),
    Biome("mobile", "minecraft:swamp",
        FL.CLEARING, GE.SEDIMENTARY, HE.TEMPERATE, HU.WET, SO.PEATY, WA.SWAMP
    ),
    Biome("moscow", "minecraft:snowy_plains",
        FL.FIELD, GE.SEDIMENTARY, HE.FROZEN, HU.DAMP, SO.LOAMY, WA.INLAND
    ),
    Biome("nassau", "minecraft:warm_ocean",
        FL.BARREN, GE.SEDIMENTARY, HE.TROPICAL, HU.WET, SO.SANDY, WA.COAST
    ),
    Biome("nice", "minecraft:beach",
        FL.BARREN, GE.SEDIMENTARY, HE.SUBTROPICAL, HU.DAMP, SO.SANDY, WA.COAST
    ),
    Biome("nuuk", "minecraft:beach",
        FL.BARREN, GE.SEDIMENTARY, HE.FROZEN, HU.DAMP, SO.SANDY, WA.COAST
    ),
    Biome("perm", "minecraft:old_growth_pine_taiga",
        FL.FOREST, GE.METAMORPHIC, HE.BOREAL, HU.DAMP, SO.ACIDIC, WA.INLAND
    ),
    Biome("phoenix", "minecraft:desert",
        FL.BARREN, GE.SEDIMENTARY, HE.TROPICAL, HU.DRY, SO.SANDY, WA.INLAND
    ),
    Biome("plymouth", "minecraft:stony_shore",
        FL.BARREN, GE.METAMORPHIC, HE.TEMPERATE, HU.DAMP, SO.ROCKY, WA.COAST
    ),
    Biome("portland", "minecraft:forest",
        FL.FOREST, GE.SEDIMENTARY, HE.TEMPERATE, HU.DAMP, SO.LOAMY, WA.INLAND
    ),
    Biome("quito", "minecraft:stony_peaks",
        FL.BARREN, GE.IGNEOUS, HE.BOREAL, HU.DRY, SO.ROCKY, WA.INLAND
    ),
    Biome("rangoon", "minecraft:bamboo_jungle",
        FL.BARREN, GE.SEDIMENTARY, HE.SUBTROPICAL, HU.DRY, SO.LOAMY, WA.INLAND
    ),
    Biome("sanfrancisco", "minecraft:ocean",
        FL.BARREN, GE.SEDIMENTARY, HE.TEMPERATE, HU.WET, SO.SANDY, WA.OCEAN
    ),
    Biome("santafe", "minecraft:wooded_badlands",
        FL.CLEARING, GE.SEDIMENTARY, HE.SUBTROPICAL, HU.DRY, SO.CLAYEY, WA.INLAND
    ),
    Biome("singapore", "minecraft:jungle",
        FL.CANOPY, GE.SEDIMENTARY, HE.TROPICAL, HU.WET, SO.ACIDIC, WA.INLAND
    ),
    Biome("tombstone", "minecraft:badlands",
        FL.BARREN, GE.SEDIMENTARY, HE.SUBTROPICAL, HU.DRY, SO.CLAYEY, WA.INLAND
    ),
    Biome("topeka", "minecraft:sunflower_plains",
        FL.FIELD, GE.SEDIMENTARY, HE.TEMPERATE, HU.DAMP, SO.LOAMY, WA.INLAND
    ),
    Biome("tromso", "minecraft:deep_frozen_ocean",
        FL.BARREN, GE.SEDIMENTARY, HE.FROZEN, HU.WET, SO.SANDY, WA.OCEAN
    ),
    Biome("umea", "minecraft:grove",
        FL.CLEARING, GE.METAMORPHIC, HE.FROZEN, HU.DAMP, SO.ACIDIC, WA.INLAND
    ),
    Biome("warsaw", "minecraft:birch_forest",
        FL.FOREST, GE.SEDIMENTARY, HE.TEMPERATE, HU.DAMP, SO.ACIDIC, WA.INLAND
    ),
    Biome("zurich", "minecraft:snowy_slopes",
        FL.BARREN, GE.METAMORPHIC, HE.FROZEN, HU.DAMP, SO.ROCKY, WA.INLAND
    ),
])
