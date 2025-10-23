from mcpacker.model.ecology.biomefilter import BiomeFilter
from mcpacker.model.ecotype import Ecotype
from mcpacker.model.habitat import Habitat
from mcpacker.model.spawn import Spawn
from mcpacker.model.spawnable import Spawnable
from pytest import fixture

import mcpacker.model.ecology.flora as F
import mcpacker.model.ecology.heat as E


# Helper Classes ###################################################################################

class SampleSpawnable(Spawnable):
    pass


# Fixtures #########################################################################################

@fixture(name="spawn")
def createSpawn():
    yield Spawn(
        "spawn",
        Habitat(biomeFilters=BiomeFilter([F.FIELD, E.TEMPERATE])),
        SampleSpawnable("spawnable"),
        Ecotype()
    )


# Tests ############################################################################################

def test_repr(spawn):
    assert repr(spawn) == (
        "Spawn("
            "ecotype=Ecotype(scarcity=Scarcity(name='sparse')), "
            "habitat=Habitat("
                "altitude=Altitude(name=anywhere, bottom=-64, top=320), "
                "biomeFilters=[BiomeFilter("
                    "required=[Flora(name='field'), Heat(name='temperate')], "
                    "prohibited=[]"
                ")], "
                "seasons=["
                    "Season(name='spring'), "
                    "Season(name='summer'), "
                    "Season(name='autumn'), "
                    "Season(name='winter')"
                "]"
            "), "
            "name='spawn', "
            "spawnable=Spawnable(name='spawnable')"
        ")"
    )

