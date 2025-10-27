from collections.abc import Iterable
from mcpacker.format.datapack.generationstep import GenerationStep
from mcpacker.format.json import JsonBlob


# Class ############################################################################################

class AddFeatureBiomeModifier:

    def __init__(self, biomes:Iterable[str]|str, features:Iterable[str]|str, step:GenerationStep):
        if isinstance(biomes, str):
            biomes = [biomes]

        if isinstance(features, str):
            features = [features]

        self.biomes = biomes
        self.features = features
        self.step = step

    def asJsobBlob(self) -> JsonBlob:
        return {
            "type": "forge:add_features",
            "biomes": list(self.biomes),
            "features": list(self.features),
            "step": str(self.step),
        }
