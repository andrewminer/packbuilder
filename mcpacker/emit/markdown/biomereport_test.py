from mcpacker.emit.markdown.biomereport import BiomeReport
from mcpacker.model.core.ecology.biome  import Biome
from mcpacker.model.modpack             import ModPack
from pytest                             import fixture

import mcpacker.model.core.ecology.flora    as F
import mcpacker.model.core.ecology.geology  as G
import mcpacker.model.core.ecology.heat     as E
import mcpacker.model.core.ecology.humidity as U
import mcpacker.model.core.ecology.soil     as S
import mcpacker.model.core.ecology.water    as W

import textwrap


# Fixtures #########################################################################################

@fixture(name="addBiomes")
def defineAddBiomes():
    def addBiomes(pack:ModPack):
        pack.world.biomes.add(
            Biome("dallas", "minecraft:savanna",
                F.FIELD, G.SEDIMENTARY, E.SUBTROPICAL, U.DRY, S.SANDY, W.INLAND
            )
        )
        pack.world.biomes.add(
            Biome("kansascity", "minecraft:plains",
                F.FIELD, G.SEDIMENTARY, E.TEMPERATE, U.DAMP, S.LOAMY, W.INLAND
            )
        )

    return addBiomes

@fixture(name="pack")
def createPack(addBiomes):
    pack = ModPack("test")
    pack.augment(addBiomes)
    yield pack

@fixture(name="report")
def createReport(pack):
    report = BiomeReport(pack)
    report.build()
    yield report

# Tests ############################################################################################

def test_report(report):
    assert str(report) == textwrap.dedent("""
        # Biome: minecraft:plains (kansascity)

          * Flora: field
          * Geology: sedimentary
          * Heat: temperate
          * Humidity: damp
          * Soil: loamy
          * Water: inland

        # Biome: minecraft:savanna (dallas)

          * Flora: field
          * Geology: sedimentary
          * Heat: subtropical
          * Humidity: dry
          * Soil: sandy
          * Water: inland
    """).strip()
