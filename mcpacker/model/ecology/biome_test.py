from mcpacker.model.ecology.biome import Biome
from pytest import fixture

import mcpacker.model.ecology.flora as F
import mcpacker.model.ecology.geology as G
import mcpacker.model.ecology.heat as E
import mcpacker.model.ecology.humidity as U
import mcpacker.model.ecology.soil as S
import mcpacker.model.ecology.water as W


# Fixtures #########################################################################################

@fixture(name="desert")
def createDesert():
    return Biome(
        "phoenix", "minecraft:desert",
        F.BARREN, G.SEDIMENTARY, E.TROPICAL, U.DRY, S.SANDY, W.INLAND
    )

# Tests ############################################################################################

def test_createBiome(desert):
    assert desert.name == "phoenix"
    assert desert.soil == S.SANDY
