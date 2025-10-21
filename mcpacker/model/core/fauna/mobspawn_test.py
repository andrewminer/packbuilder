from mcpacker.model.core.ecology.biomefilter import BiomeFilter
from mcpacker.model.core.fauna.mob import Mob
from mcpacker.model.core.fauna.mobspawn import MobSpawn
from mcpacker.model.core.habitat import Habitat
from pytest import fixture

import mcpacker.model.core.fauna.active as AC
import mcpacker.model.core.ecology.flora as FL
import mcpacker.model.core.ecology.heat as HE


# Fixtures #########################################################################################

@fixture(name="cow")
def createCow():
    yield Mob("minecraft:cow", AC.DIURNAL)

@fixture(name="fields")
def createFieldsHabitat():
    yield Habitat(biomeFilter=BiomeFilter([FL.FIELD, HE.TEMPERATE]))

@fixture(name="spawn")
def createMobSpawn(cow, fields):
    yield MobSpawn(cow, fields)


# Tests ############################################################################################

def test_cowsInFields(spawn):
    assert repr(spawn) == (
        "Spawn(" +
            "habitats=[" +
                "Habitat(" +
                    "altitude=Altitude(name=anywhere, bottom=-64, top=320), " +
                    "biomeFilter=BiomeFilter(" +
                        "required=[Flora(name='field'), Heat(name='temperate')], " +
                        "prohibited=[]" +
                    "), " +
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
            "]" +
        ")"
    )

