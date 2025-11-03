from mcpacker.format.json import JsonBlob
from mcpacker.model.flora.patch import Patch
from mcpacker.model.flora.plantspawn import PlantSpawn
from mcpacker.model.modpack import ModPack

import mcpacker.model.flora.immersion as IM


# Class ############################################################################################

class CropPlacedFeature:

    def __init__(self, pack:ModPack, spawn:PlantSpawn):
        self.pack = pack
        self.spawn = spawn

    def asJsonBlob(self) -> JsonBlob:
        return {
            "feature": f"{self.pack.name}:crop/{self.spawn.plant.name}",
            "placement": self._buildPlacements(),
        }

    @property
    def patch(self) -> Patch:
        if not isinstance(self.spawn.plant, Patch): raise ValueError()
        return self.spawn.plant

    # Private Methods ##########################################################

    def _buildPlacements(self) -> list[JsonBlob]:
        livesIn = "minecraft:air"
        if self.patch.immersion == IM.SUBMERGED:
            livesIn = "minecraft:water"

        placements:list[JsonBlob] = [
            {
                "type": "minecraft:block_predicate_filter",
                "predicate": [
                    {
                        "type": "minecraft:matching_blocks",
                        "blocks": livesIn,
                    }, {
                        "type": "minecraft:matching_blocks",
                        "offset": [0, -1, 0],
                        "blocks": list(str(s) for s in self.patch.substrates),
                    },
                ]
            }
        ]

        if self.patch.immersion == IM.ADJACENT:
            placements.append(self._buildWaterAdjacentPlacement())

        return placements

    def _buildWaterAdjacentPlacement(self) -> JsonBlob:
        return {
            "type": "minecraft:any_of",
            "predicates": [
                {
                    "type": "minecraft:matching_fluids",
                    "fluids": [
                        "minecraft:water",
                        "minecraft:flowing_water"
                    ],
                    "offset": [ 1, -1, 0 ]
                }, {
                    "type": "minecraft:matching_fluids",
                    "fluids": [
                        "minecraft:water",
                        "minecraft:flowing_water"
                    ],
                    "offset": [ -1, -1, 0 ]
                }, {
                    "type": "minecraft:matching_fluids",
                    "fluids": [
                        "minecraft:water",
                        "minecraft:flowing_water"
                    ],
                    "offset": [ 0, -1, 1 ]
                }, {
                    "type": "minecraft:matching_fluids",
                    "fluids": [
                        "minecraft:water",
                        "minecraft:flowing_water"
                    ],
                    "offset": [ 0, -1, -1 ]
                }
            ]
        }
