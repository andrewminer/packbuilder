# Class ############################################################################################

class HeightMapType:
    """
    A cached record of the top block at all points in the world.

    see: https://minecraft.wiki/w/Heightmap
    """

    def __init__(self, gameId:str):
        self.gameId = gameId

    def asData(self) -> str:
        return self.gameId


# Constants ########################################################################################

MOTION_BLOCKING           = HeightMapType("MOTION_BLOCKING")
MOTION_BLOCKING_NO_LEAVES = HeightMapType("MOTION_BLOCKING_NO_LEAVES")
OCEAN_FLOOR               = HeightMapType("OCEAN_FLOOR")
OCEAN_FLOOR_WG            = HeightMapType("OCEAN_FLOOR_WG")
WORLD_SURFACE             = HeightMapType("WORLD_SURFACE")
WORLD_SURFACE_WG          = HeightMapType("WORLD_SURFACE_WG")
