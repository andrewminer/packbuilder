from pytest import fixture
from tungston.core.ecology.biome import Biome

import tungston.core.ecology.flora as F
import tungston.core.ecology.geology as G
import tungston.core.ecology.heat as E
import tungston.core.ecology.humidity as U
import tungston.core.ecology.soil as S
import tungston.core.ecology.water as W


# Fixtures #########################################################################################

@fixture(name="desert")
def createDesert():
    return Biome(
        "phoenix", "minecraft:desert",
        F.BARREN, G.SEDIMENTARY, E.TROPICAL, U.DRY, S.SANDY, W.INLAND
    )

# Tests ############################################################################################

def test_createBiome(desert):
    assert desert.city == "phoenix"
    assert desert.soil == S.SANDY
