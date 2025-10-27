from mcpacker.model.ecology.biome import Biome
from mcpacker.model.ecology.biomefilter import BiomeFilter as BF
from mcpacker.model.fauna.mob import Mob
from mcpacker.model.fauna.mobspawn import MobSpawn
from mcpacker.model.fauna.mobspawnbuilder import MobSpawnBuilder
from mcpacker.model.geology.mineral import Mineral
from mcpacker.model.geology.replacement import Replacement
from mcpacker.model.habitat import Habitat
from mcpacker.model.modpack import ModPack
from mcpacker.ui.runner import Runner
from mcpacker.write.incontrol.spawnerwriter import SpawnerWriter
from pathlib import Path
from pytest import fixture
from zipfile import ZipFile

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
        b = MobSpawnBuilder(pack.world.mobSpawns)

        b.start(mobs["minecraft:chicken"])
        b.altitude = AL.span(AL.LOWLANDS, AL.UPLANDS)
        b.biomeFilters = BF([HE.TROPICAL, HU.WET, FL.within(FL.CANOPY, FL.CLEARING)])
        b.seasons = SE.SUMMER
        b.group = GR.TROUP
        b.scarcity = SC.COMMON
        b.save("chicken-summer")

        b.seasons = SE.exclude(SE.SUMMER)
        b.scarcity = SC.UNCOMMON
        b.save("chicken-normal")

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

    with ZipFile(tmp_path/"testpack"/"datapacks"/"testpack.jar") as archive:
        nameList = archive.namelist()
        assert "testpack/pack.mcmeta" in nameList

def test_writeReports(tmp_path:Path, reportRunner:Runner):
    assert (tmp_path/"testpack"/"reports"/"biomes.txt").exists()
    assert (tmp_path/"testpack"/"reports"/"deposits.txt").exists()
    assert (tmp_path/"testpack"/"reports"/"minerals.txt").exists()
    assert (tmp_path/"testpack"/"reports"/"mobspawns.txt").exists()
