from pytest import fixture
from tungston.core.ecology.biomefilter import BiomeFilter
from tungston.core.habitat import Habitat
from tungston.core.placement import Placement

import tungston.core.ecology.flora as F
import tungston.core.ecology.heat as E


# Fixtures #########################################################################################

@fixture(name="fields")
def createFieldsHabitat():
    yield Habitat(biomeFilter=BiomeFilter([F.FIELD, E.TEMPERATE]))

@fixture(name="placement")
def createPlacement(fields):
    yield Placement([fields])


# Tests ############################################################################################

def test_repr(placement):
    assert repr(placement) == (
        "Placement{" +
            "habitats: [" +
                "Habitat{" +
                    "altitude: [anywhere <-64 to 320>], " +
                    "biomeFilter: BiomeFilter([[Flora<field>, Heat<temperate>]], [[]]), " +
                    "seasons: [Season<spring>, Season<summer>, Season<autumn>, Season<winter>], " +
                    "group: solo<1 to 1>, " +
                    "location: Location<outside>, " +
                    "scarcity: Scarcity<sparse>" +
                "}" +
            "]" +
        "}"
    )

