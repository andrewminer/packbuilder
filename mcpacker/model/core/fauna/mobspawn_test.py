from mcpacker.model.core.ecology.biomefilter import BiomeFilter
from mcpacker.model.core.fauna.mob import Mob
from mcpacker.model.core.fauna.mobspawn import MobSpawn
from mcpacker.model.core.habitat import Habitat
from pytest import fixture

import mcpacker.model.core.ecology.flora as F
import mcpacker.model.core.ecology.heat as E


# Fixtures #########################################################################################

@fixture(name="cow")
def createCow():
    yield Mob("cow", "minecraft:cow")

@fixture(name="fields")
def createFieldsHabitat():
    yield Habitat(biomeFilter=BiomeFilter([F.FIELD, E.TEMPERATE]))

@fixture(name="spawn")
def createMobSpawn(cow, fields):
    yield MobSpawn(cow, fields)


# Tests ############################################################################################

def test_cowsInFields(spawn):
    assert str(spawn) == (
        "Spawn{" +
            "habitats: [" +
                "Habitat{" +
                    "altitude: anywhere <-64 to 320>, " +
                    "biomeFilter: BiomeFilter([[Flora<field>, Heat<temperate>]], [[]]), " +
                    "seasons: [Season<spring>, Season<summer>, Season<autumn>, Season<winter>], " +
                    "group: solo<1 to 1>, " +
                    "location: Location<outside>, " +
                    "scarcity: Scarcity<sparse>" +
                "}" +
            "]" +
        "}"
    )

