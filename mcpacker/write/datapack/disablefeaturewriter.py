from mcpacker.format.datapack.biomemodifier.removefeature import RemoveFeatureBiomeModifier
from mcpacker.format.datapack.noop import NoopPlacedFeature
from mcpacker.write.writer import Writer

import mcpacker.write.json as json


# Class ############################################################################################

class DisableFeatureWriter(Writer):
    """
    Disables all the placed features listed as being overridden in the modpack.
    """

    def doWrite(self):
        if not self.pack.disabledFeatures: return

        self._writeRemoveFeaturesBiomeModifier()
        self._writeNoopPlacedFeatures()

    # Private Methods ##########################################################

    def _writeNoopPlacedFeatures(self):
        for placedFeature in self.pack.disabledFeatures:
            path = self.locator.placedFeatures(placedFeature.mod) / f"{placedFeature.name}.json"
            self.resetOutputFile(path)
            path.write_text(json.dumps(NoopPlacedFeature().asJsonBlob()))

    def _writeRemoveFeaturesBiomeModifier(self):
        features = [str(f) for f in self.pack.disabledFeatures]
        modifier = RemoveFeatureBiomeModifier("#c:is_overworld", features)
        path = self.locator.biomeModifiers() / "remove_disabled_features.json"
        self.resetOutputFile(path)
        path.write_text(json.dumps(modifier.asJsobBlob()))
