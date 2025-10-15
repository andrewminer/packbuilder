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
        "Habitat(" +
            "altitude=Altitude(name=anywhere, bottom=-64, top=320), " +
            "biomeFilter=BiomeFilter(" +
                "required=[Flora(name='field'), Heat(name='temperate')], " +
                "prohibited=[]"
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
        ")"
    )
