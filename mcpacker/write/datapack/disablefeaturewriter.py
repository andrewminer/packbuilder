from mcpacker.format.datapack.biomemodifier.removefeature import RemoveFeatureBiomeModifier
from mcpacker.format.datapack.configuredfeature import ConfiguredFeature
from mcpacker.format.datapack.placedfeature import PlacedFeature
from mcpacker.write.writer import Writer

import mcpacker.json as json


# Class ############################################################################################

class DisableFeatureWriter(Writer):

    def doWrite(self):
        if not self.pack.disabledFeatures: return

        self._writeRemoveFeaturesBiomeModifier()
        self._writeNoopConfiguredFeature()
        self._writeNoopPlacedFeatures()

    # Private Methods ##########################################################

    def _writeNoopConfiguredFeature(self):
        feature = ConfiguredFeature("minecraft:no_op")
        path = self.locator.configuredFeatures() / "noop.json"
        self.resetOutputFile(path)
        path.write_text(json.dumps(feature.asJsonBlob(), indent=json.INDENT))

    def _writeNoopPlacedFeatures(self):
        for placedFeature in self.pack.disabledFeatures:
            path = self.locator.placedFeatures(placedFeature.mod) / f"{placedFeature.name}.json"
            self.resetOutputFile(path)
            feature = PlacedFeature(f"{self.pack.name}:noop", [])
            path.write_text(json.dumps(feature.asJsonBlob(), indent=json.INDENT))

    def _writeRemoveFeaturesBiomeModifier(self):
        features = [str(f) for f in self.pack.disabledFeatures]
        modifier = RemoveFeatureBiomeModifier("#c:is_overworld", features)
        path = self.locator.biomeModifiers() / "remove_disabled_features.json"
        self.resetOutputFile(path)
        path.write_text(json.dumps(modifier.asJsobBlob(), indent=json.INDENT))
