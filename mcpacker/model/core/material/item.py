from mcpacker.model.core.resourceid import ResourceId


# Class ############################################################################################

class Item:

    def __init__(self, gameId:ResourceId):
        self.gameId = gameId

        if not isinstance(self.gameId, ResourceId):
            self.gameId = ResourceId.parse(str(self.gameId))
