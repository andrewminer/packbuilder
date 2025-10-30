from mcpacker.format.json import JsonBlob
from mcpacker.model.flora.companion import Companion
from mcpacker.model.flora.patch import Patch
from typing import cast

import mcpacker.format.json as json
import mcpacker.model.flora.immersion as IM


# Class ############################################################################################

class CropConfiguredFeature:

    def __init__(self, patch:Patch):
        self.patch = patch

    def asJsonBlob(self) -> JsonBlob:
        return {
            "type": "minecraft:simple_block",
            "config": {
                "to_place": {
                    "type": "minecraft:weighted_state_provider",
                    "entries": self._buildCompanionEntries(),
                }
            }
        }

    # Private Methods ##########################################################

    def _buildBaseProperties(self) -> JsonBlob:
        result = { k: str(v) for k, v in (self.patch.blocks[0].properties or {}).items() }
        if self.patch.immersion == IM.SUBMERGED:
            result["waterlogged"] = "true"

        return cast(JsonBlob, result)

    def _buildCompanionEntries(self) -> JsonBlob:
        usedWeight = sum(c.weight for c in self.patch.companions)
        weight = 100 - usedWeight

        results:list[JsonBlob] = []
        results.append(self._buildPlantState(weight))

        for companion in self.patch.companions:
            results.append({
                "data": { "Name": str(companion.gameId) },
                "weight": companion.weight,
            })

        return results

    def _buildPlantState(self, weight) -> JsonBlob:
        result = {
            "data": {
                "Name": str(self.patch.blocks[0].gameId),
            },
            "weight": weight,
        }

        properties = self._buildBaseProperties()
        if properties:
            result["data"]["Properties"] = properties

        return result
