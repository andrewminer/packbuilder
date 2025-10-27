from collections.abc import Iterable
from mcpacker.format.json import JsonBlob
from mcpacker.model.ecology.biome import Biome
from mcpacker.model.ecology.biomefilter import BiomeFilter
from mcpacker.model.fauna.active import Active
from mcpacker.model.fauna.mobspawn import MobSpawn
from mcpacker.model.scarcity import Scarcity
from mcpacker.model.season import Season
from mcpacker.write.writer import Writer
from typing import cast

import mcpacker.format.json as FJ
import mcpacker.write.json as WJ
import mcpacker.model.dimension as DI
import mcpacker.model.fauna.location as LO
import mcpacker.model.scarcity as SC
import mcpacker.model.time as TI


# Class ############################################################################################

class SpawnerWriter(Writer):

    def doWrite(self):
        path = self.locator.inc_config()/"spawner.json"
        self.resetOutputFile(path)
        path.write_text(WJ.dumps(self._makeAllRules()))


    # Private Functions ########################################################

    def _computeBiomeNames(self, biomeFilters:Iterable[BiomeFilter]) -> JsonBlob:
        accepted:set[Biome] = set()
        for biome in self.pack.world.biomes:
            for biomeFilter in biomeFilters:
                if not biomeFilter.accepts(biome): continue
                accepted.add(biome)

        return cast(JsonBlob, sorted(str(b.gameId) for b in accepted))

    def _computeSpawnRate(self, scarcity:Scarcity) -> float:
        base = {
            SC.ABSENT:   24 * TI.HOUR,
            SC.RARE:     10 * TI.MIN,
            SC.UNUSUAL:   5 * TI.MIN,
            SC.SPARSE:    1 * TI.MIN,
            SC.UNCOMMON: 15 * TI.SEC,
            SC.COMMON:    5 * TI.SEC,
            SC.CARPET:    1 * TI.SEC,
        }[scarcity]

        return 1.0 / (base / 20)

    def _computeWeight(self, scarcity:Scarcity) -> int:
        return {
            SC.ABSENT: 0,
            SC.RARE: 1,
            SC.UNUSUAL: 2,
            SC.SPARSE: 4,
            SC.UNCOMMON: 8,
            SC.COMMON: 16,
            SC.CARPET: 32,
        }[scarcity]

    def _makeAndCondition(self, spawn:MobSpawn, season:Season, active:Active) -> JsonBlob:
        return {
            "biome": self._computeBiomeNames(spawn.habitat.biomeFilters),
            season.name: True,
            "seesky": True if LO.OUTSIDE == spawn.ecotype.location else None,
            "cave": True if LO.CAVE == spawn.ecotype.location else None,
            "mintime": active.start,
            "maxtime": active.end,
        }

    def _makeAllRules(self) -> JsonBlob:
        result:list[JsonBlob] = []

        for spawn in self.pack.world.mobSpawns:
            for season in spawn.habitat.seasons:
                for active in spawn.mob.active:
                    result.append(self._makeRule(spawn, season, active))

        return FJ.removeEmptyObjects(FJ.removeNoneValues(result))

    def _makeCondition(self, spawn:MobSpawn, season:Season, active:Active) -> JsonBlob:
        return {
            "dimension": DI.OVERWORLD.name,
            "minheight": spawn.habitat.altitude.bottom,
            "maxheight": spawn.habitat.altitude.top,
            "maxthis": spawn.ecotype.group.largest * 2,
            "inwater": LO.WATER == spawn.ecotype.location,
            "and": self._makeAndCondition(spawn, season, active),
        }

    def _makeRule(self, spawn:MobSpawn, season:Season, active:Active) -> JsonBlob:
        return {
            "mob": str(spawn.mob.gameId),
            "amount": {
                "minimum": spawn.ecotype.group.smallest,
                "maximum": spawn.ecotype.group.largest,
                "groupdistance": 4,
            },
            "persecond": self._computeSpawnRate(spawn.ecotype.scarcity),
            "attempts": spawn.ecotype.group.largest * 4,
            "weights": [ self._computeWeight(spawn.ecotype.scarcity) ],
            "conditions": self._makeCondition(spawn, season, active),
        }
