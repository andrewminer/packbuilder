from mcpacker.json import JsonBlob


# Classes ##########################################################################################

class BiomeModifier:

    def asJsonBlob(self) -> JsonBlob:
        return {
            "type": "neoforge:none",
        }
