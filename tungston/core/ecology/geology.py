from tungston.core.ecology.biometrait import BiomeTrait


# Class ############################################################################################

class Geology(BiomeTrait):
    """
    The natural of the rock strata in a biome.
    """
    pass


# Constants ########################################################################################

IGNEOUS     = Geology("igneous")
METAMORPHIC = Geology("metamorphic")
SEDIMENTARY = Geology("sedimentary")

ALL = [IGNEOUS, METAMORPHIC, SEDIMENTARY]
