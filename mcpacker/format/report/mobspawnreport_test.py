from mcpacker.format.report.mobspawnreport import MobSpawnReport
from mcpacker.model.ecology.biomefilter import BiomeFilter as BF
from mcpacker.model.fauna.mob import Mob
from mcpacker.model.fauna.mobspawn import MobSpawn
from mcpacker.model.geology.mineral import Mineral
from mcpacker.model.geology.replacement import Replacement
from mcpacker.model.habitat import Habitat
from mcpacker.model.modpack import AugmentFunc
from mcpacker.model.modpack import ModPack
from pytest import fixture

import mcpacker.model.altitude as AL
import mcpacker.model.ecology.flora as FL
import mcpacker.model.ecology.geology as GE
import mcpacker.model.ecology.heat as HE
import mcpacker.model.ecology.humidity as HU
import mcpacker.model.ecology.soil as SO
import mcpacker.model.ecology.water as WA
import mcpacker.model.fauna.active as AC
import mcpacker.model.fauna.group as GR
import mcpacker.model.fauna.location as LO
import mcpacker.model.scarcity as SC
import mcpacker.model.season as SE
import textwrap


# Fixtures #########################################################################################

@fixture(name="addMobs")
def defineAddMobs():
    def addMobs(pack:ModPack):
        pack.world.mobs.add(Mob("minecraft:chicken", AC.DIURNAL))

    yield addMobs

@fixture(name="addMobSpawns")
def defineAddMobSpawnss():
    def addMobSpawns(pack:ModPack):
        mobs = pack.world.mobs
        spawns = pack.world.mobSpawns

        pack.world.mobSpawns.add(
            MobSpawn(mobs["minecraft:chicken"],
                Habitat(
                    altitude    = AL.span(AL.LOWLANDS, AL.UPLANDS),
                    biomeFilter = BF([HE.TROPICAL, HU.WET, FL.within(FL.CANOPY, FL.CLEARING)]),
                    seasons     = SE.SUMMER,
                    group       = GR.TROUP,
                    scarcity    = SC.COMMON,
                ).derive(
                    seasons     = SE.exclude(SE.SUMMER),
                    scarcity    = SC.UNCOMMON
                )
            )
        )

    yield addMobSpawns

@fixture(name="pack")
def createPack(addMobs:AugmentFunc, addMobSpawns:AugmentFunc):
    yield ModPack("testModPack").augment(addMobs).augment(addMobSpawns)

@fixture(name="report")
def createReport(pack:ModPack):
    yield MobSpawnReport(pack).compose()


# Tests ############################################################################################

def test_write(report:MobSpawnReport):
    assert str(report).strip() == textwrap.dedent("""
        Mob: minecraft:chicken

            Habitat 1
                altitude: lowlands to uplands (70 to 124)
                biomeFilter: tropical and wet and (canopy or forest or clearing)
                seasons: summer
                group: troup (3 to 6)
                location: outside
                scarcity: common

            Habitat 2
                altitude: lowlands to uplands (70 to 124)
                biomeFilter: tropical and wet and (canopy or forest or clearing)
                seasons: spring, autumn, winter
                group: troup (3 to 6)
                location: outside
                scarcity: uncommon
    """).strip()
