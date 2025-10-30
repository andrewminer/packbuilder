from mcpacker.model.resourceid import ResourceId


# Class ############################################################################################

class Companion:

    def __init__(self, gameId:ResourceId|str, weight:int):
        self.gameId = ResourceId.parse(gameId)
        self.weight = weight
