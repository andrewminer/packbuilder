from tungston.core.ecology.biome import Biome
from tungston.core.ecology.biomecatalog import BiomeCatalog
from tungston.core.ecology.biomefilter import BiomeFilter

import tungston.core.ecology.flora as F
import tungston.core.ecology.geology as G
import tungston.core.ecology.heat as E
import tungston.core.ecology.humidity as U
import tungston.core.ecology.soil as S
import tungston.core.ecology.water as W

# Constants ########################################################################################

CATALOG = BiomeCatalog([
    Biome("aberdeen", "minecraft:windswept_gravelly_hills",
        F.BARREN, G.METAMORPHIC, E.BOREAL, U.DAMP, S.ROCKY, W.INLAND
    ),
    Biome("archangel", "minecraft:frozen_ocean",
        F.BARREN, G.SEDIMENTARY, E.FROZEN, U.WET, S.SANDY, W.OCEAN
    ),
    Biome("aspen", "minecraft:frozen_peaks",
        F.BARREN, G.IGNEOUS, E.FROZEN, U.WET, S.ROCKY, W.INLAND
    ),
    Biome("bombay", "minecraft:lukewarm_ocean",
        F.BARREN, G.SEDIMENTARY, E.SUBTROPICAL, U.WET, S.SANDY, W.OCEAN
    ),
    Biome("boston", "minecraft:cold_ocean",
        F.BARREN, G.SEDIMENTARY, E.BOREAL, U.WET, S.CLAYEY, W.OCEAN
    ),
    Biome("bryce", "minecraft:eroded_badlands",
        F.BARREN, G.SEDIMENTARY, E.SUBTROPICAL, U.DRY, S.CLAYEY, W.INLAND
    ),
    Biome("calcutta", "minecraft:mangrove_swamp",
        F.FOREST, G.SEDIMENTARY, E.SUBTROPICAL, U.WET, S.CLAYEY, W.INLAND
    ),
    Biome("cornwall", "minecraft:windswept_hills",
        F.BARREN, G.METAMORPHIC, E.BOREAL, U.DAMP, S.ROCKY, W.INLAND
    ),
    Biome("dallas", "minecraft:savanna",
        F.FIELD, G.SEDIMENTARY, E.SUBTROPICAL, U.DRY, S.SANDY, W.INLAND
    ),
    Biome("duluth", "minecraft:frozen_river",
        F.BARREN, G.SEDIMENTARY, E.FROZEN, U.WET, S.SANDY, W.RIVER
    ),
    Biome("durango", "minecraft:savanna_plateau",
        F.FIELD, G.IGNEOUS, E.SUBTROPICAL, U.DRY, S.SANDY, W.INLAND
    ),
    Biome("freiburg", "minecraft:dark_forest",
        F.CANOPY, G.SEDIMENTARY, E.TEMPERATE, U.WET, S.CLAYEY, W.INLAND
    ),
    Biome("glasgow", "minecraft:windswept_forest",
        F.CLEARING, G.METAMORPHIC, E.BOREAL, U.DAMP, S.ACIDIC, W.INLAND
    ),
    Biome("haarlem", "minecraft:flower_forest",
        F.CLEARING, G.SEDIMENTARY, E.TEMPERATE, U.DAMP, S.LOAMY, W.INLAND
    ),
    Biome("halifax", "minecraft:deep_cold_ocean",
        F.BARREN, G.SEDIMENTARY, E.BOREAL, U.WET, S.SANDY, W.OCEAN
    ),
    Biome("hammerfest", "minecraft:ice_spikes",
        F.BARREN, G.METAMORPHIC, E.FROZEN, U.WET, S.ROCKY, W.INLAND
    ),
    Biome("havana", "minecraft:deep_lukewarm_ocean",
        F.BARREN, G.SEDIMENTARY, E.SUBTROPICAL, U.WET, S.SANDY, W.OCEAN
    ),
    Biome("hilo", "minecraft:mushroom_fields",
        F.CLEARING, G.IGNEOUS, E.SUBTROPICAL, U.WET, S.FUNGAL, W.INLAND
    ),
    Biome("honolulu", "minecraft:deep_ocean",
        F.BARREN, G.SEDIMENTARY, E.TEMPERATE, U.WET, S.SANDY, W.OCEAN
    ),
    Biome("innnesbruk", "minecraft:meadow",
        F.FIELD, G.SEDIMENTARY, E.BOREAL, U.DAMP, S.PEATY, W.INLAND
    ),
    Biome("irkutsk", "minecraft:taiga",
        F.FOREST, G.METAMORPHIC, E.BOREAL, U.DAMP, S.ACIDIC, W.INLAND
    ),
    Biome("jackson", "minecraft:jagged_peaks",
        F.BARREN, G.METAMORPHIC, E.BOREAL, U.DRY, S.ROCKY, W.INLAND
    ),
    Biome("juneau", "minecraft:old_growth_spruce_taiga",
        F.FOREST, G.METAMORPHIC, E.BOREAL, U.DAMP, S.PEATY, W.INLAND
    ),
    Biome("kansascity", "minecraft:plains",
        F.FIELD, G.SEDIMENTARY, E.TEMPERATE, U.DAMP, S.LOAMY, W.INLAND
    ),
    Biome("kola", "minecraft:snowy_taiga",
        F.BARREN, G.METAMORPHIC, E.FROZEN, U.DAMP, S.ACIDIC, W.INLAND
    ),
    Biome("kyoto", "minecraft:cherry_grove",
        F.CLEARING, G.SEDIMENTARY, E.TEMPERATE, U.DAMP, S.ROCKY, W.INLAND
    ),
    Biome("madras", "minecraft:sparse_jungle",
        F.CLEARING, G.SEDIMENTARY, E.TROPICAL, U.WET, S.ACIDIC, W.INLAND
    ),
    Biome("memphis", "minecraft:river",
        F.CLEARING, G.SEDIMENTARY, E.TEMPERATE, U.WET, S.SANDY, W.RIVER
    ),
    Biome("minsk", "minecraft:old_growth_birch_forest",
        F.FOREST, G.SEDIMENTARY, E.TEMPERATE, U.DAMP, S.ACIDIC, W.INLAND
    ),
    Biome("moab", "minecraft:windswept_savanna",
        F.FIELD, G.IGNEOUS, E.SUBTROPICAL, U.DRY, S.ROCKY, W.INLAND
    ),
    Biome("mobile", "minecraft:swamp",
        F.CLEARING, G.SEDIMENTARY, E.TEMPERATE, U.WET, S.PEATY, W.SWAMP
    ),
    Biome("moscow", "minecraft:snowy_plains",
        F.FIELD, G.SEDIMENTARY, E.FROZEN, U.DAMP, S.LOAMY, W.INLAND
    ),
    Biome("nassau", "minecraft:warm_ocean",
        F.BARREN, G.SEDIMENTARY, E.TROPICAL, U.WET, S.SANDY, W.COAST
    ),
    Biome("nice", "minecraft:beach",
        F.BARREN, G.SEDIMENTARY, E.SUBTROPICAL, U.DAMP, S.SANDY, W.COAST
    ),
    Biome("nuuk", "minecraft:beach",
        F.BARREN, G.SEDIMENTARY, E.FROZEN, U.DAMP, S.SANDY, W.COAST
    ),
    Biome("perm", "minecraft:old_growth_pine_taiga",
        F.FOREST, G.METAMORPHIC, E.BOREAL, U.DAMP, S.ACIDIC, W.INLAND
    ),
    Biome("phoenix", "minecraft:desert",
        F.BARREN, G.SEDIMENTARY, E.TROPICAL, U.DRY, S.SANDY, W.INLAND
    ),
    Biome("plymouth", "minecraft:stony_shore",
        F.BARREN, G.METAMORPHIC, E.TEMPERATE, U.DAMP, S.ROCKY, W.COAST
    ),
    Biome("portland", "minecraft:forest",
        F.FOREST, G.SEDIMENTARY, E.TEMPERATE, U.DAMP, S.LOAMY, W.INLAND
    ),
    Biome("quito", "minecraft:stony_peaks",
        F.BARREN, G.IGNEOUS, E.BOREAL, U.DRY, S.ROCKY, W.INLAND
    ),
    Biome("rangoon", "minecraft:bamboo_jungle",
        F.BARREN, G.SEDIMENTARY, E.SUBTROPICAL, U.DRY, S.LOAMY, W.INLAND
    ),
    Biome("sanfrancisco", "minecraft:ocean",
        F.BARREN, G.SEDIMENTARY, E.TEMPERATE, U.WET, S.SANDY, W.OCEAN
    ),
    Biome("santafe", "minecraft:wooded_badlands",
        F.CLEARING, G.SEDIMENTARY, E.SUBTROPICAL, U.DRY, S.CLAYEY, W.INLAND
    ),
    Biome("singapore", "minecraft:jungle",
        F.CANOPY, G.SEDIMENTARY, E.TROPICAL, U.WET, S.ACIDIC, W.INLAND
    ),
    Biome("tombstone", "minecraft:badlands",
        F.BARREN, G.SEDIMENTARY, E.SUBTROPICAL, U.DRY, S.CLAYEY, W.INLAND
    ),
    Biome("topeka", "minecraft:sunflower_plains",
        F.FIELD, G.SEDIMENTARY, E.TEMPERATE, U.DAMP, S.LOAMY, W.INLAND
    ),
    Biome("tromso", "minecraft:deep_frozen_ocean",
        F.BARREN, G.SEDIMENTARY, E.FROZEN, U.WET, S.SANDY, W.OCEAN
    ),
    Biome("umea", "minecraft:grove",
        F.CLEARING, G.METAMORPHIC, E.FROZEN, U.DAMP, S.ACIDIC, W.INLAND
    ),
    Biome("warsaw", "minecraft:birch_forest",
        F.FOREST, G.SEDIMENTARY, E.TEMPERATE, U.DAMP, S.ACIDIC, W.INLAND
    ),
    Biome("zurich", "minecraft:snowy_slopes",
        F.BARREN, G.METAMORPHIC, E.FROZEN, U.DAMP, S.ROCKY, W.INLAND
    ),
])
