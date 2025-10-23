from mcpacker.model.ecology.biomefilter import BiomeFilter
from mcpacker.model.fauna.mob import Mob
from mcpacker.model.fauna.mobecotype import MobEcotype
from mcpacker.model.fauna.mobspawn import MobSpawn
from mcpacker.model.habitat import Habitat
from pytest import fixture

import mcpacker.model.fauna.active as AC
import mcpacker.model.ecology.flora as FL
import mcpacker.model.ecology.heat as HE


# Fixtures #########################################################################################

@fixture(name="spawn")
def createMobSpawn():
    yield MobSpawn(
        "cow-in-field",
        Habitat(biomeFilters=BiomeFilter([FL.FIELD, HE.TEMPERATE])),
        Mob("minecraft:cow", AC.DIURNAL),
        MobEcotype()
    )


# Tests ############################################################################################

def test_cowsInFields(spawn):
    assert repr(spawn) == (
        "MobSpawn("
            "ecotype=MobEcotype("
                "group=Group(name='solo', smallest=1, largest=1), "
                "location=Location(name='outside'), "
                "scarcity=Scarcity(name='sparse')"
            "), "
            "habitat=Habitat("
                "altitude=Altitude(name=anywhere, bottom=-64, top=320), "
                "biomeFilters=[BiomeFilter("
                    "required=[Flora(name='field'), Heat(name='temperate')], "
                    "prohibited=[])"
                "], "
                "seasons=["
                    "Season(name='spring'), "
                    "Season(name='summer'), "
                    "Season(name='autumn'), "
                    "Season(name='winter')"
                "]"
            "), "
            "name='cow-in-field', "
            "spawnable=Mob("
                "gameId=ResourceId(isTag=False, mod='minecraft', name='cow'), "
                "active=[Active<day>{start:0, end:12000}]"
            ")"
        ")"
    )

