from mcpacker.model.core.ecology.biome       import Biome
from mcpacker.model.core.ecology.biomefilter import BiomeFilter
from mcpacker.model.modpack                  import ModPack

import mcpacker.model.core.ecology.flora    as FL
import mcpacker.model.core.ecology.geology  as GE
import mcpacker.model.core.ecology.heat     as HE
import mcpacker.model.core.ecology.humidity as HU
import mcpacker.model.core.ecology.soil     as SO
import mcpacker.model.core.ecology.water    as WA


# Functions ########################################################################################

def addBiomes(pack:ModPack):
    pack.world.biomes.add(
        Biome("aberdeen", "minecraft:windswept_gravelly_hills",
            FL.BARREN, GE.METAMORPHIC, HE.BOREAL, HU.DAMP, SO.ROCKY, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("archangel", "minecraft:frozen_ocean",
            FL.BARREN, GE.SEDIMENTARY, HE.FROZEN, HU.WET, SO.SANDY, WA.OCEAN
        )
    )

    pack.world.biomes.add(
        Biome("aspen", "minecraft:frozen_peaks",
            FL.BARREN, GE.IGNEOUS, HE.FROZEN, HU.WET, SO.ROCKY, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("bombay", "minecraft:lukewarm_ocean",
            FL.BARREN, GE.SEDIMENTARY, HE.SUBTROPICAL, HU.WET, SO.SANDY, WA.OCEAN
        )
    )

    pack.world.biomes.add(
        Biome("boston", "minecraft:cold_ocean",
            FL.BARREN, GE.SEDIMENTARY, HE.BOREAL, HU.WET, SO.CLAYEY, WA.OCEAN
        )
    )

    pack.world.biomes.add(
        Biome("bryce", "minecraft:eroded_badlands",
            FL.BARREN, GE.SEDIMENTARY, HE.SUBTROPICAL, HU.DRY, SO.CLAYEY, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("calcutta", "minecraft:mangrove_swamp",
            FL.FOREST, GE.SEDIMENTARY, HE.SUBTROPICAL, HU.WET, SO.CLAYEY, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("cornwall", "minecraft:windswept_hills",
            FL.BARREN, GE.METAMORPHIC, HE.BOREAL, HU.DAMP, SO.ROCKY, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("dallas", "minecraft:savanna",
            FL.FIELD, GE.SEDIMENTARY, HE.SUBTROPICAL, HU.DRY, SO.SANDY, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("duluth", "minecraft:frozen_river",
            FL.BARREN, GE.SEDIMENTARY, HE.FROZEN, HU.WET, SO.SANDY, WA.RIVER
        )
    )

    pack.world.biomes.add(
        Biome("durango", "minecraft:savanna_plateau",
            FL.FIELD, GE.IGNEOUS, HE.SUBTROPICAL, HU.DRY, SO.SANDY, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("freiburg", "minecraft:dark_forest",
            FL.CANOPY, GE.SEDIMENTARY, HE.TEMPERATE, HU.WET, SO.CLAYEY, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("glasgow", "minecraft:windswept_forest",
            FL.CLEARING, GE.METAMORPHIC, HE.BOREAL, HU.DAMP, SO.ACIDIC, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("haarlem", "minecraft:flower_forest",
            FL.CLEARING, GE.SEDIMENTARY, HE.TEMPERATE, HU.DAMP, SO.LOAMY, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("halifax", "minecraft:deep_cold_ocean",
            FL.BARREN, GE.SEDIMENTARY, HE.BOREAL, HU.WET, SO.SANDY, WA.OCEAN
        )
    )

    pack.world.biomes.add(
        Biome("hammerfest", "minecraft:ice_spikes",
            FL.BARREN, GE.METAMORPHIC, HE.FROZEN, HU.WET, SO.ROCKY, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("havana", "minecraft:deep_lukewarm_ocean",
            FL.BARREN, GE.SEDIMENTARY, HE.SUBTROPICAL, HU.WET, SO.SANDY, WA.OCEAN
        )
    )

    pack.world.biomes.add(
        Biome("hilo", "minecraft:mushroom_fields",
            FL.CLEARING, GE.IGNEOUS, HE.SUBTROPICAL, HU.WET, SO.FUNGAL, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("honolulu", "minecraft:deep_ocean",
            FL.BARREN, GE.SEDIMENTARY, HE.TEMPERATE, HU.WET, SO.SANDY, WA.OCEAN
        )
    )

    pack.world.biomes.add(
        Biome("innnesbruk", "minecraft:meadow",
            FL.FIELD, GE.SEDIMENTARY, HE.BOREAL, HU.DAMP, SO.PEATY, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("irkutsk", "minecraft:taiga",
            FL.FOREST, GE.METAMORPHIC, HE.BOREAL, HU.DAMP, SO.ACIDIC, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("jackson", "minecraft:jagged_peaks",
            FL.BARREN, GE.METAMORPHIC, HE.BOREAL, HU.DRY, SO.ROCKY, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("juneau", "minecraft:old_growth_spruce_taiga",
            FL.FOREST, GE.METAMORPHIC, HE.BOREAL, HU.DAMP, SO.PEATY, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("kansascity", "minecraft:plains",
            FL.FIELD, GE.SEDIMENTARY, HE.TEMPERATE, HU.DAMP, SO.LOAMY, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("kola", "minecraft:snowy_taiga",
            FL.BARREN, GE.METAMORPHIC, HE.FROZEN, HU.DAMP, SO.ACIDIC, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("kyoto", "minecraft:cherry_grove",
            FL.CLEARING, GE.SEDIMENTARY, HE.TEMPERATE, HU.DAMP, SO.ROCKY, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("madras", "minecraft:sparse_jungle",
            FL.CLEARING, GE.SEDIMENTARY, HE.TROPICAL, HU.WET, SO.ACIDIC, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("memphis", "minecraft:river",
            FL.CLEARING, GE.SEDIMENTARY, HE.TEMPERATE, HU.WET, SO.SANDY, WA.RIVER
        )
    )

    pack.world.biomes.add(
        Biome("minsk", "minecraft:old_growth_birch_forest",
            FL.FOREST, GE.SEDIMENTARY, HE.TEMPERATE, HU.DAMP, SO.ACIDIC, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("moab", "minecraft:windswept_savanna",
            FL.FIELD, GE.IGNEOUS, HE.SUBTROPICAL, HU.DRY, SO.ROCKY, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("mobile", "minecraft:swamp",
            FL.CLEARING, GE.SEDIMENTARY, HE.TEMPERATE, HU.WET, SO.PEATY, WA.SWAMP
        )
    )

    pack.world.biomes.add(
        Biome("moscow", "minecraft:snowy_plains",
            FL.FIELD, GE.SEDIMENTARY, HE.FROZEN, HU.DAMP, SO.LOAMY, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("nassau", "minecraft:warm_ocean",
            FL.BARREN, GE.SEDIMENTARY, HE.TROPICAL, HU.WET, SO.SANDY, WA.COAST
        )
    )

    pack.world.biomes.add(
        Biome("nice", "minecraft:beach",
            FL.BARREN, GE.SEDIMENTARY, HE.SUBTROPICAL, HU.DAMP, SO.SANDY, WA.COAST
        )
    )

    pack.world.biomes.add(
        Biome("nuuk", "minecraft:snowy_beach",
            FL.BARREN, GE.SEDIMENTARY, HE.FROZEN, HU.DAMP, SO.SANDY, WA.COAST
        )
    )

    pack.world.biomes.add(
        Biome("perm", "minecraft:old_growth_pine_taiga",
            FL.FOREST, GE.METAMORPHIC, HE.BOREAL, HU.DAMP, SO.ACIDIC, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("phoenix", "minecraft:desert",
            FL.BARREN, GE.SEDIMENTARY, HE.TROPICAL, HU.DRY, SO.SANDY, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("plymouth", "minecraft:stony_shore",
            FL.BARREN, GE.METAMORPHIC, HE.TEMPERATE, HU.DAMP, SO.ROCKY, WA.COAST
        )
    )

    pack.world.biomes.add(
        Biome("portland", "minecraft:forest",
            FL.FOREST, GE.SEDIMENTARY, HE.TEMPERATE, HU.DAMP, SO.LOAMY, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("quito", "minecraft:stony_peaks",
            FL.BARREN, GE.IGNEOUS, HE.BOREAL, HU.DRY, SO.ROCKY, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("rangoon", "minecraft:bamboo_jungle",
            FL.BARREN, GE.SEDIMENTARY, HE.SUBTROPICAL, HU.DRY, SO.LOAMY, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("sanfrancisco", "minecraft:ocean",
            FL.BARREN, GE.SEDIMENTARY, HE.TEMPERATE, HU.WET, SO.SANDY, WA.OCEAN
        )
    )

    pack.world.biomes.add(
        Biome("santafe", "minecraft:wooded_badlands",
            FL.CLEARING, GE.SEDIMENTARY, HE.SUBTROPICAL, HU.DRY, SO.CLAYEY, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("singapore", "minecraft:jungle",
            FL.CANOPY, GE.SEDIMENTARY, HE.TROPICAL, HU.WET, SO.ACIDIC, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("tombstone", "minecraft:badlands",
            FL.BARREN, GE.SEDIMENTARY, HE.SUBTROPICAL, HU.DRY, SO.CLAYEY, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("topeka", "minecraft:sunflower_plains",
            FL.FIELD, GE.SEDIMENTARY, HE.TEMPERATE, HU.DAMP, SO.LOAMY, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("tromso", "minecraft:deep_frozen_ocean",
            FL.BARREN, GE.SEDIMENTARY, HE.FROZEN, HU.WET, SO.SANDY, WA.OCEAN
        )
    )

    pack.world.biomes.add(
        Biome("umea", "minecraft:grove",
            FL.CLEARING, GE.METAMORPHIC, HE.FROZEN, HU.DAMP, SO.ACIDIC, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("warsaw", "minecraft:birch_forest",
            FL.FOREST, GE.SEDIMENTARY, HE.TEMPERATE, HU.DAMP, SO.ACIDIC, WA.INLAND
        )
    )

    pack.world.biomes.add(
        Biome("zurich", "minecraft:snowy_slopes",
            FL.BARREN, GE.METAMORPHIC, HE.FROZEN, HU.DAMP, SO.ROCKY, WA.INLAND
        )
    )
