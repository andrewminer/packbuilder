from mcpacker.model.core.ecology.biometrait import BiomeTrait


# Class ############################################################################################

class Location:
    """
    Where a creature is most likely to be encountered.
    """

    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Location(name='{self.name}')"


# Constants ########################################################################################

OUTSIDE = Location("outside")
CAVE    = Location("cave")
WATER   = Location("water")

ALL = [OUTSIDE, CAVE, WATER]
