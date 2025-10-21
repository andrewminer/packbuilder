from mcpacker.model.ecology.biometrait import BiomeTrait


# Class ############################################################################################

class Soil(BiomeTrait):
    """
    The nature of the soil within a certain region.
    """
    pass


# Constants ########################################################################################

ACIDIC = Soil("acidic")
CLAYEY = Soil("clayey")
FUNGAL = Soil("fungal")
LOAMY  = Soil("loamy")
PEATY  = Soil("peaty")
ROCKY  = Soil("rocky")
SANDY  = Soil("sandy")

ALL = [ACIDIC, CLAYEY, FUNGAL, LOAMY, PEATY, ROCKY, SANDY]
