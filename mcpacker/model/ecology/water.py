from mcpacker.model.ecology.biometrait import BiomeTrait


# Class ############################################################################################

class Water(BiomeTrait):
    """
    The kind of large body of water which dominates a biome.
    """
    pass


# Constants ########################################################################################

RIVER  = Water("river")
SWAMP  = Water("swamp")
OCEAN  = Water("ocean")
COAST  = Water("coast")
INLAND = Water("inland")

ALL = (RIVER, SWAMP, OCEAN, COAST, INLAND)
