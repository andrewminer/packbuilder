from mcpacker.model.core.ecology.biomefilter import BiomeFilter
from mcpacker.model.core.habitat import Habitat
from pytest import fixture

import mcpacker.model.core.ecology.flora as FL
import mcpacker.model.core.ecology.heat as HE
import mcpacker.model.core.season as SE
import mcpacker.model.core.scarcity as SC


# Fixtures #########################################################################################

@fixture(name="fields")
def createFieldsFilter():
    yield BiomeFilter([FL.FIELD, HE.TEMPERATE])

@fixture(name="derivedHabitats")
def createDerivedHabitat(fields):
    yield (
        Habitat(biomeFilter=fields, seasons=SE.SUMMER, scarcity=SC.COMMON)
        .derive(seasons=SE.AUTUMN, scarcity=SC.UNCOMMON)
        .derive(seasons=SE.WINTER, scarcity=SC.ABSENT)
        .collect()
    )

@fixture(name="fields")
def createFieldsHabitat(fields):
    yield Habitat(biomeFilter=fields)

# Tests ############################################################################################

def test_derive(derivedHabitats):
    assert [h.scarcity for h in derivedHabitats] == [SC.COMMON, SC.UNCOMMON, SC.ABSENT]

def test_repr(fields):
    assert repr(fields) == (
        "Habitat{" +
            "altitude: anywhere <-64 to 320>, " +
            "biomeFilter: BiomeFilter([[Flora<field>, Heat<temperate>]], [[]]), " +
            "seasons: [Season<spring>, Season<summer>, Season<autumn>, Season<winter>], " +
            "group: solo<1 to 1>, " +
            "location: Location<outside>, " +
            "scarcity: Scarcity<sparse>" +
        "}"
    )
