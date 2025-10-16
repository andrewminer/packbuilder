from mcpacker.json import JsonBlob


# Class ############################################################################################

class ConfiguredFeature:

    def __init__(self, gameId:str):
        self.gameId = gameId

    def asJsonBlob(self) -> JsonBlob:
        return {
            "type": self.gameId,
            "config": {},
        }
