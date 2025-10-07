from pytest import fixture
from tungston.core.ecology.biome import Biome
from tungston.core.ecology.biomecatalog import BiomeCatalog
from tungston.core.world import World
from tungston.generator.markdown.biomereport import BiomeReport

import tungston.core.ecology.flora as F
import tungston.core.ecology.geology as G
import tungston.core.ecology.heat as E
import tungston.core.ecology.humidity as U
import tungston.core.ecology.soil as S
import tungston.core.ecology.water as W

import textwrap


# Fixtures #########################################################################################

@fixture(name="biomes")
def createCatalog():
    yield BiomeCatalog([
        Biome("dallas", "minecraft:savanna",
            F.FIELD, G.SEDIMENTARY, E.SUBTROPICAL, U.DRY, S.SANDY, W.INLAND
        ),
        Biome("kansascity", "minecraft:plains",
            F.FIELD, G.SEDIMENTARY, E.TEMPERATE, U.DAMP, S.LOAMY, W.INLAND
        ),
    ])

@fixture(name="world")
def createWorld(biomes):
    yield World(biomes, None, None, None)

@fixture(name="report")
def createReport(world):
    report = BiomeReport(world)
    report.build()
    yield report

# Tests ############################################################################################

def test_report(report):
    assert str(report) == textwrap.dedent("""
        # Biome: dallas <minecraft:savanna>

          * Flora: field
          * Geology: sedimentary
          * Heat: subtropical
          * Humidity: dry
          * Soil: sandy
          * Water: inland

        # Biome: kansascity <minecraft:plains>

          * Flora: field
          * Geology: sedimentary
          * Heat: temperate
          * Humidity: damp
          * Soil: loamy
          * Water: inland
    """).strip()
