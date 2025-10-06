from tungston.core.ecology.biometrait import BiomeTrait

import tungston.core.ecology.biometrait as biomeTrait


# Class ############################################################################################

class Flora(BiomeTrait):
    """
    Describes how densely the foiliage covers a biome.
    """
    pass


# Constants ########################################################################################

CANOPY   = Flora("canopy")
FOREST   = Flora("forest")
CLEARING = Flora("clearing")
FIELD    = Flora("field")
BARREN   = Flora("barren")

ALL = [CANOPY, FOREST, CLEARING, FIELD, BARREN]

# Helpers ##########################################################################################

def within(start:Flora, end:Flora) -> list[Flora]:
    return biomeTrait.within(ALL, start, end)
