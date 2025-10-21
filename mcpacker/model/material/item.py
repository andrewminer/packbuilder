from mcpacker.model.resourceid import ResourceId


# Class ############################################################################################

class Item:

    def __init__(self, gameId:ResourceId|str):
        self.gameId = ResourceId.parse(gameId)

    def __repr__(self) -> str:
        return f"Item(gameId={repr(self.gameId)})"

    @property
    def name(self) -> str:
        return str(self.gameId)
