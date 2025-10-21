from mcpacker.model.ecology.biome import Biome
from mcpacker.model.ecology.biomefilter import BiomeFilter as BF
from mcpacker.model.fauna.mob import Mob
from mcpacker.model.fauna.mobspawn import MobSpawn
from mcpacker.model.geology.mineral import Mineral
from mcpacker.model.geology.replacement import Replacement
from mcpacker.model.habitat import Habitat
from mcpacker.model.modpack import ModPack
from mcpacker.write.incontrol.spawnerwriter import SpawnerWriter
from pathlib import Path
from pytest import fixture

import mcpacker.json                        as json
import mcpacker.model.altitude         as AL
import mcpacker.model.ecology.flora    as FL
import mcpacker.model.ecology.geology  as GE
import mcpacker.model.ecology.heat     as HE
import mcpacker.model.ecology.humidity as HU
import mcpacker.model.ecology.soil     as SO
import mcpacker.model.ecology.water    as WA
import mcpacker.model.fauna.active     as AC
import mcpacker.model.fauna.group      as GR
import mcpacker.model.fauna.location   as LO
import mcpacker.model.scarcity         as SC
import mcpacker.model.season           as SE
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
    pack = ModPack("testModPack")
    pack.augment(addBiomes)
    pack.augment(addMobs)
    pack.augment(addMobSpawns)
    yield pack

@fixture(name="writer")
def createWriter(pack, tmp_path):
    writer = SpawnerWriter(pack, tmp_path)
    writer.write()
    yield writer


# Tests ############################################################################################

def test_write(writer:SpawnerWriter, tmp_path:Path):
    path = tmp_path / "testModPack" / "config" / "incontrol" / "spawner.json"
    text = path.read_text()
    data = json.loads(text)

    assert len(data) == 4

    rule = data[0]
    assert rule["mob"] == "minecraft:chicken"
    assert rule["amount"]["maximum"] == 6
    assert abs(rule["persecond"] - 0.2) < 0.001
    assert rule["conditions"]["and"]["biome"] == ["minecraft:jungle"]
    assert rule["conditions"]["and"]["summer"]

    rule = data[1]
    assert abs(rule["persecond"] - 0.066) < 0.001
    assert rule["conditions"]["and"]["spring"]


