from mcpacker.format.datapack.placement import Placement


# Class ############################################################################################

class PlacedFeature:

    def __init__(self, gameId:str, placements:list[Placement]):
        self.gameId = gameId
        self.placements = placements
