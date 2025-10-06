from tungston.core.ecology.biometrait import BiomeTrait

import tungston.core.ecology.biometrait as biomeTrait


# Class ############################################################################################

class Heat(BiomeTrait):
    """
    The general range of ambient temperatures in a biome (in °F).
    """

    def __init__(self, name, low:int, high:int):
        super().__init__(name)
        self.low = low
        self.high = high


# Constants ########################################################################################

TROPICAL    = Heat("tropical",     75,  88)
SUBTROPICAL = Heat("subtropical",  58,  82)
TEMPERATE   = Heat("temperate",    36,  66)
BOREAL      = Heat("boreal",       10,  54)
FROZEN      = Heat("frozen",      -20,  32)

ALL = [TROPICAL, SUBTROPICAL, TEMPERATE, BOREAL, FROZEN]


# Helpers ##########################################################################################

def within(start:Heat, end:Heat) -> list[Heat]:
    return biomeTrait.within(ALL, start, end)
