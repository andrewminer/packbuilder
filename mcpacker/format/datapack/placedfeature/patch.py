from mcpacker.model.altitude import Altitude
from mcpacker.format.json import JsonBlob
from mcpacker.model.flora.patch import Patch
from mcpacker.model.flora.plantspawn import PlantSpawn
from mcpacker.model.modpack import ModPack

import mcpacker.model.altitude as AL
import mcpacker.model.scarcity as SC


# Class ############################################################################################

class PatchPlacedFeature:

    def __init__(self, pack:ModPack, spawn:PlantSpawn, altitude:Altitude):
        self.altitude = altitude
        self.pack = pack
        self.spawn = spawn

    def asJsonBlob(self) -> JsonBlob|None:
        fullRange = self.spawn.habitat.altitude
        band = AL.intersect(self.altitude, fullRange)
        if not band: return None

        kind = "tree"
        if isinstance(self.spawn.plant, Patch):
            kind = "patch"

        return {
            "feature": f"{self.pack.name}:{kind}/{self.spawn.plant.name}",
            "placement": [
                {
                    "type": "mincraft:rarity_filter",
                    "chance": self._getRarityChance(),
                }, {
                    "type": "minecraft:in_square",
                }, {
                    "type": "minecraft:biome",
                }, {
                    "type": "minecraft:height_range",
                    "height": {
                        "type": "minecraft:constant",
                        "value": {
                            "absolute": band.bottom,
                        },
                    },
                }, {
                    "type": "minecraft:block_predicate_filter",
                    "predicate": {
                        "type": "minecraft:matching_blocks",
                        "blocks": "minecraft:air",
                    },
                }, {
                    "type": "minecraft:environment_scan",
                    "direction_of_search": "up",
                    "max_steps": min(32, band.top - band.bottom),
                    "target_condition": {
                        "type": "minecraft:matching_blocks",
                        "blocks": "minecraft:air",
                    },
                },
            ],
        }


    # Private Methods ##########################################################

    def _getRarityChance(self) -> int:
        return {
            SC.ABSENT: 100000,
            SC.RARE: 64,
            SC.UNUSUAL: 32,
            SC.SPARSE: 16,
            SC.UNCOMMON: 8,
            SC.COMMON: 3,
            SC.CARPET: 2
        }[self.spawn.ecotype.scarcity]
