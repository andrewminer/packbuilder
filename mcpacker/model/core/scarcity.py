# Class ############################################################################################

class Scarcity:
    """
    How frequently something appears within a given region.
    """

    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Scarcity(name='{self.name}')"


# Constants ########################################################################################

ABSENT   = Scarcity("absent")
RARE     = Scarcity("rare")
UNUSUAL  = Scarcity("unusual")
SPARSE   = Scarcity("sparse")
UNCOMMON = Scarcity("uncommon")
COMMON   = Scarcity("common")
CARPET   = Scarcity("carpet")

ALL = [ABSENT, RARE, UNUSUAL, SPARSE, UNCOMMON, COMMON, CARPET]
