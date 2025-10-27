from mcpacker.format.json import JsonBlob


# Class ############################################################################################

class NoopBiomeModifier:

    def asJsonBlob(self) -> JsonBlob:
        return {
            "type": "forge:none",
        }
