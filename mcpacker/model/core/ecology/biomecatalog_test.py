from mcpacker.model.core.ecology.biome import Biome
from mcpacker.model.core.ecology.biomecatalog import BiomeCatalog
from mcpacker.model.core.ecology.biomefilter import BiomeFilter
from pytest import fixture

import mcpacker.model.core.ecology.flora as F
import mcpacker.model.core.ecology.geology as G
import mcpacker.model.core.ecology.heat as E
import mcpacker.model.core.ecology.humidity as U
import mcpacker.model.core.ecology.soil as S
import mcpacker.model.core.ecology.water as W

# Fixtures #########################################################################################

@fixture(name="jungles")
def createJungleFilter():
    yield BiomeFilter([U.WET, E.TROPICAL, F.within(F.CANOPY, F.CLEARING)])

@fixture(name="catalog")
def createCatalog():
    yield BiomeCatalog([
        Biome("dallas", "minecraft:savanna",
            F.FIELD, G.SEDIMENTARY, E.SUBTROPICAL, U.DRY, S.SANDY, W.INLAND
        ),
        Biome("kansascity", "minecraft:plains",
            F.FIELD, G.SEDIMENTARY, E.TEMPERATE, U.DAMP, S.LOAMY, W.INLAND
        ),
        Biome("mobile", "minecraft:swamp",
            F.CLEARING, G.SEDIMENTARY, E.TEMPERATE, U.WET, S.PEATY, W.SWAMP
        ),
        Biome("phoenix", "minecraft:desert",
            F.BARREN, G.SEDIMENTARY, E.TROPICAL, U.DRY, S.SANDY, W.INLAND
        ),
        Biome("portland", "minecraft:forest",
            F.FOREST, G.SEDIMENTARY, E.TEMPERATE, U.DAMP, S.LOAMY, W.INLAND
        ),
        Biome("singapore", "minecraft:jungle",
            F.CANOPY, G.SEDIMENTARY, E.TROPICAL, U.WET, S.ACIDIC, W.INLAND
        ),
    ])


# Tests ############################################################################################

def test_findJungles(catalog, jungles):
    assert [b.city for b in catalog.matching(jungles)] == ["singapore"]
