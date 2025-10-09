# Class ############################################################################################

class Dimension:

    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Dimension<{self.name}>"


# Constants ########################################################################################

OVERWORLD = Dimension("minecraft:overworld")
NETHER    = Dimension("minecraft:nether")
END       = Dimension("minecraft:end")

ALL = [OVERWORLD, NETHER, END]
