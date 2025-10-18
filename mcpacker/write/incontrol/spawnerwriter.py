from mcpacker.json                           import JsonBlob
from mcpacker.model.core.ecology.biomefilter import BiomeFilter
from mcpacker.model.core.fauna.active        import Active
from mcpacker.model.core.fauna.mobspawn      import MobSpawn
from mcpacker.model.core.habitat             import Habitat
from mcpacker.model.core.scarcity            import Scarcity
from mcpacker.model.core.season              import Season
from mcpacker.model.modpack                  import ModPack
from mcpacker.write.incontrol                import INCONTROL_CONFIG_DIR
from mcpacker.write.writer                   import Writer
from pathlib                                 import Path

import mcpacker.json                      as json
import mcpacker.model.core.dimension      as DI
import mcpacker.model.core.fauna.location as LO
import mcpacker.model.core.scarcity       as SC
import mcpacker.model.time                as TI
import os


# Class ############################################################################################

class SpawnerWriter(Writer):

    def doWrite(self):
        path = self.locator.inc_config()/"spawner.json"
        self.resetOutputFile(path)
        path.write_text(json.dumps(self._makeAllRules(), indent=json.INDENT))

    # Private Functions ########################################################

    def _computeBiomeNames(self, biomeFilter:BiomeFilter) -> JsonBlob:
        return list(
            str(b.gameId) for b in self.pack.world.biomes.filter(
                lambda b: biomeFilter.accepts(b)
            )
        )

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

    def _makeAndCondition(self, habitat:Habitat, season:Season, active:Active) -> JsonBlob:
        return {
            "biome": self._computeBiomeNames(habitat.biomeFilter),
            season.name: True,
            "seesky": True if LO.OUTSIDE == habitat.location else None,
            "cave": True if LO.CAVE == habitat.location else None,
            "mintime": active.start,
            "maxtime": active.end,
        }

    def _makeAllRules(self) -> JsonBlob:
        result:list[JsonBlob] = []

        for spawn in self.pack.world.mobSpawns:
            for habitat in spawn.habitats:
                for season in habitat.seasons:
                    for active in spawn.mob.active:
                        result.append(self._makeRule(spawn, habitat, season, active))

        return json.removeEmptyObjects(json.removeNoneValues(result))

    def _makeCondition(self, habitat:Habitat, season:Season, active:Active) -> JsonBlob:
        return {
            "dimension": DI.OVERWORLD.name,
            "minheight": habitat.altitude.bottom,
            "maxheight": habitat.altitude.top,
            "maxthis": habitat.group.largest * 2,
            "inwater": LO.WATER == habitat.location,
            "and": self._makeAndCondition(habitat, season, active),
        }

    def _makeRule(self, spawn:MobSpawn, habitat:Habitat, season:Season, active:Active,) -> JsonBlob:
        return {
            "mob": str(spawn.mob.gameId),
            "amount": {
                "minimum": habitat.group.smallest,
                "maximum": habitat.group.largest,
                "groupdistance": 4,
            },
            "persecond": self._computeSpawnRate(habitat.scarcity),
            "attempts": habitat.group.largest * 4,
            "weights": [ self._computeWeight(habitat.scarcity) ],
            "conditions": self._makeCondition(habitat, season, active),
        }
