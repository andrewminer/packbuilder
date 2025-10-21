from mcpacker.model.ecology.biomefilter import BiomeFilter
from mcpacker.model.habitat import Habitat
from mcpacker.model.spawn import Spawn
from pytest import fixture

import mcpacker.model.ecology.flora as F
import mcpacker.model.ecology.heat as E


# Fixtures #########################################################################################

@fixture(name="fields")
def createFieldsHabitat():
    yield Habitat(biomeFilter=BiomeFilter([F.FIELD, E.TEMPERATE]))

@fixture(name="spawn")
def createSpawn(fields):
    yield Spawn([fields])


# Tests ############################################################################################

def test_repr(spawn):
    assert repr(spawn) == (
        "Spawn(habitats=[" +
            "Habitat(" +
                "altitude=Altitude(name=anywhere, bottom=-64, top=320), " +
                "biomeFilter=BiomeFilter(" +
                    "required=[Flora(name='field'), Heat(name='temperate')], " +
                    "prohibited=[]" +
                "), "
                "seasons=[" +
                    "Season(name='spring'), " +
                    "Season(name='summer'), " +
                    "Season(name='autumn'), " +
                    "Season(name='winter')" +
                "], " +
                "group=Group(name='solo', smallest=1, largest=1), " +
                "location=Location(name='outside'), " +
                "scarcity=Scarcity(name='sparse')" +
            ")" +
        "])"
    )

