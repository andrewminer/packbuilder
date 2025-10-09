from mcpacker.json import JsonBlob


# Class ############################################################################################

class BlockStateProvider:

    def __init__(self, gameId:str):
        self.gameId = gameId

    def asJsonBlob(self) -> JsonBlob:
        raise NotImplementedError()
