from mcpacker.format.json import JsonBlob


# Class ############################################################################################

class NoopConfiguredFeature:

    def asJsonBlob(self) -> JsonBlob:
        return {
            "type": "minecraft:noop",
            "config": {},
        }

class NoopPlacedFeature:

    def asJsonBlob(self) -> JsonBlob:
        return {
            "feature": NoopConfiguredFeature().asJsonBlob(),
            "placement": []
        }

