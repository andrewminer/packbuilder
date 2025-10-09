from mcpacker.model.core.ecology.biomefilter import BiomeFilter
from mcpacker.model.core.habitat import Habitat
from mcpacker.model.core.spawn import Spawn
from pytest import fixture

import mcpacker.model.core.ecology.flora as F
import mcpacker.model.core.ecology.heat as E


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

