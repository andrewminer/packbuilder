from mcpacker.model.core.ecology.biomefilter import BiomeFilter as BF
from mcpacker.model.core.fauna.mob           import Mob
from mcpacker.model.core.fauna.mobspawn      import MobSpawn
from mcpacker.model.core.geology.mineral     import Mineral
from mcpacker.model.core.geology.replacement import Replacement
from mcpacker.model.core.habitat             import Habitat
from mcpacker.model.modpack                  import ModPack
from mcpacker.write.markdown.mobspawnreport  import MobSpawnReport
from pytest                                  import fixture

import mcpacker.model.core.altitude         as AL
import mcpacker.model.core.ecology.flora    as FL
import mcpacker.model.core.ecology.geology  as GE
import mcpacker.model.core.ecology.heat     as HE
import mcpacker.model.core.ecology.humidity as HU
import mcpacker.model.core.ecology.soil     as SO
import mcpacker.model.core.ecology.water    as WA
import mcpacker.model.core.fauna.active     as AC
import mcpacker.model.core.fauna.group      as GR
import mcpacker.model.core.fauna.location   as LO
import mcpacker.model.core.scarcity         as SC
import mcpacker.model.core.season           as SE
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
def createPack(addMobs, addMobSpawns):
    pack = ModPack("testModPack")
    pack.augment(addMobs)
    pack.augment(addMobSpawns)
    yield pack

@fixture(name="report")
def createReport(pack, tmp_path):
    report = MobSpawnReport(pack, tmp_path)
    report.write()
    yield report

# Tests ############################################################################################

def test_write(report, tmp_path):
    path = tmp_path / "testModPack" / "reports" / "mobspawns.md"
    assert path.read_text() == textwrap.dedent("""
        # Mob: minecraft:chicken

          * habitat 1
            * altitude: lowlands-uplands
            * biomeFilter:
              * Heat: tropical
              * Humidity: wet
              * Flora: any of: canopy, forest, clearing
            * seasons: summer
            * group: troup
            * location: outside
            * scarcity: common
          * habitat 2
            * altitude: lowlands-uplands
            * biomeFilter:
              * Heat: tropical
              * Humidity: wet
              * Flora: any of: canopy, forest, clearing
            * seasons: spring, autumn, winter
            * group: troup
            * location: outside
            * scarcity: uncommon

    """).lstrip()
