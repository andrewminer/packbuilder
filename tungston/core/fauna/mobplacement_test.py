from pytest import fixture
from tungston.core.ecology.biomefilter import BiomeFilter
from tungston.core.fauna.mob import Mob
from tungston.core.fauna.mobplacement import MobPlacement
from tungston.core.habitat import Habitat

import tungston.core.ecology.flora as F
import tungston.core.ecology.heat as E


# Fixtures #########################################################################################

@fixture(name="cow")
def createCow():
    yield Mob("cow", "minecraft:cow")

@fixture(name="fields")
def createFieldsHabitat():
    yield Habitat(biomeFilter=BiomeFilter([F.FIELD, E.TEMPERATE]))

@fixture(name="placement")
def createMobPlacement(cow, fields):
    yield MobPlacement(cow, fields)


# Tests ############################################################################################

def test_cowsInFields(placement):
    assert str(placement) == (
        "Placement{" +
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

