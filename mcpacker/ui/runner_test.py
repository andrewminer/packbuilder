from mcpacker.model.core.ecology.biome       import Biome
from mcpacker.model.core.ecology.biomefilter import BiomeFilter as BF
from mcpacker.model.core.fauna.mob           import Mob
from mcpacker.model.core.fauna.mobspawn      import MobSpawn
from mcpacker.model.core.geology.mineral     import Mineral
from mcpacker.model.core.geology.replacement import Replacement
from mcpacker.model.core.habitat             import Habitat
from mcpacker.model.modpack                  import ModPack
from mcpacker.ui.runner                      import Runner
from mcpacker.write.incontrol.spawnerwriter  import SpawnerWriter
from pathlib                                 import Path
from pytest                                  import fixture

import mcpacker.json                        as json
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

@fixture(name="addBiomes")
def defineAddBiomes():
    def addBiomes(pack:ModPack):
        pack.world.biomes.add(Biome("singapore", "minecraft:jungle",
            FL.CANOPY, GE.SEDIMENTARY, HE.TROPICAL, HU.WET, SO.ACIDIC, WA.INLAND
        ))

    yield addBiomes

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
def createPack(addBiomes, addMobs, addMobSpawns):
    pack = ModPack("testpack")
    pack.augment(addBiomes)
    pack.augment(addMobs)
    pack.augment(addMobSpawns)
    yield pack

@fixture(name="modPackRunner")
def createModPackRunner(tmp_path:Path, pack:ModPack):
    runner = Runner(pack, tmp_path)
    runner._command_writeModPack()
    yield runner

@fixture(name="reportRunner")
def createReportRunner(tmp_path:Path, pack:ModPack):
    runner = Runner(pack, tmp_path)
    runner._command_writeReports()
    yield runner

# Tests ############################################################################################

def test_writeModPack(tmp_path:Path, modPackRunner:Runner):
    assert (tmp_path/"testpack"/"config"/"incontrol"/"spawner.json").exists()
    assert (tmp_path/"testpack"/"test.md").exists()

def test_writeReports(tmp_path:Path, reportRunner:Runner):
    assert (tmp_path/"testpack"/"reports"/"biomes.md").exists()
    assert (tmp_path/"testpack"/"reports"/"minerals.md").exists()
    assert (tmp_path/"testpack"/"reports"/"mobspawns.md").exists()
