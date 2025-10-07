from mcpacker.model.core.ecology.biome import Biome
from pytest import fixture

import mcpacker.model.core.ecology.flora as F
import mcpacker.model.core.ecology.geology as G
import mcpacker.model.core.ecology.heat as E
import mcpacker.model.core.ecology.humidity as U
import mcpacker.model.core.ecology.soil as S
import mcpacker.model.core.ecology.water as W


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
