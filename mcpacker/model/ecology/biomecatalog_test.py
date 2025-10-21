from mcpacker.model.ecology.biome import Biome
from mcpacker.model.ecology.biomecatalog import BiomeCatalog
from mcpacker.model.ecology.biomefilter import BiomeFilter
from pytest import fixture

import mcpacker.model.ecology.flora as F
import mcpacker.model.ecology.geology as G
import mcpacker.model.ecology.heat as E
import mcpacker.model.ecology.humidity as U
import mcpacker.model.ecology.soil as S
import mcpacker.model.ecology.water as W

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
        Biome("kansasname", "minecraft:plains",
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
    assert [b.name for b in catalog.filter(lambda b: jungles.accepts(b))] == ["singapore"]
