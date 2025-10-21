from mcpacker.format.report.biomereport import BiomeReport
from mcpacker.model.core.ecology.biome import Biome
from mcpacker.model.modpack import AugmentFunc
from mcpacker.model.modpack import ModPack
from pytest import fixture
from typing import Callable

import mcpacker.model.core.ecology.flora as F
import mcpacker.model.core.ecology.geology as G
import mcpacker.model.core.ecology.heat as E
import mcpacker.model.core.ecology.humidity as U
import mcpacker.model.core.ecology.soil as S
import mcpacker.model.core.ecology.water as W
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
def createPack(addBiomes:AugmentFunc):
    pack = ModPack("testModPack")
    pack.augment(addBiomes)
    yield pack

@fixture(name="report")
def createReport(pack:ModPack):
    yield BiomeReport(pack).compose()


# Tests ############################################################################################

def test_report(report):
 assert str(report).strip() == textwrap.dedent("""
        Biome: minecraft:savanna (dallas)

            Traits: field, sedimentary, subtropical, dry, sandy, inland

            Geology:
                <no deposits>

            Flora:
                <no flora>

            Fauna:
                <no fauna>

        Biome: minecraft:plains (kansascity)

            Traits: field, sedimentary, temperate, damp, loamy, inland

            Geology:
                <no deposits>

            Flora:
                <no flora>

            Fauna:
                <no fauna>
    """).strip()
