from mcpacker.format.json import JsonBlob
from mcpacker.model.flora.patch import Patch
from mcpacker.model.modpack import ModPack


# Class ############################################################################################

class PatchConfiguredFeature:

    def __init__(self, pack:ModPack, patch:Patch):
        self.pack = pack
        self.patch = patch

    def asJsonBlob(self) -> JsonBlob:
        return {
            "type": "minecraft:random_patch",
            "config": {
                "tries": self.patch.attempts(),
                "xz_spread": self.patch.radius,
                "y_spread": self.patch.radius / 2,
                "feature": f"{self.pack.name}:plant/{self.patch.name}",
            }
        }
