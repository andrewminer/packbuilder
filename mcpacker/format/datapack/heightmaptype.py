# Class ############################################################################################

class HeightMapType:
    """
    A cached record of the top block at all points in the world.

    see: https://minecraft.wiki/w/Heightmap
    """

    def __init__(self, name:str):
        self.name = name

    def __repr__(self) -> str:
        return f"HeightMapType(name={self.name})"

    def __str__(self) -> str:
        return self.name

    def asData(self) -> str:
        return self.name


# Constants ########################################################################################

MOTION_BLOCKING           = HeightMapType("MOTION_BLOCKING")
MOTION_BLOCKING_NO_LEAVES = HeightMapType("MOTION_BLOCKING_NO_LEAVES")
OCEAN_FLOOR               = HeightMapType("OCEAN_FLOOR")
OCEAN_FLOOR_WG            = HeightMapType("OCEAN_FLOOR_WG")
WORLD_SURFACE             = HeightMapType("WORLD_SURFACE")
WORLD_SURFACE_WG          = HeightMapType("WORLD_SURFACE_WG")
