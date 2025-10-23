from mcpacker.model.ecology.biomefilter import BiomeFilter
from mcpacker.model.habitat import Habitat
from pytest import fixture

import mcpacker.model.altitude as AL
import mcpacker.model.ecology.flora as FL
import mcpacker.model.ecology.heat as HE
import mcpacker.model.season as SE


# Fixtures #########################################################################################

@fixture(name="fields")
def createFieldsFilter():
    yield BiomeFilter([FL.FIELD, HE.TEMPERATE])

@fixture(name="fields")
def createFieldsHabitat(fields):
    yield Habitat(AL.LOWLANDS, BiomeFilter([FL.FIELD, HE.TEMPERATE]), SE.HOT)

# Tests ############################################################################################

def test_repr(fields):
    assert repr(fields) == (
        "Habitat("
            "altitude=Altitude(name=lowlands, bottom=70, top=92), "
            "biomeFilters=[BiomeFilter("
                "required=[Flora(name='field'), Heat(name='temperate')], "
                "prohibited=[]"
            ")], "
            "seasons=[Season(name='summer')]"
        ")"
    )
