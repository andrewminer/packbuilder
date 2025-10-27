from collections.abc import Iterable
from mcpacker.model.ecology.biometrait import BiomeTrait

import mcpacker.model.ecology.biometrait as biomeTrait


# Class ############################################################################################

class Humidity(BiomeTrait):
    """
    The general level of humidity present in the air.
    """
    pass


# Constants ########################################################################################

SOAKED  = Humidity("soaked")
WET  = Humidity("wet")
DAMP = Humidity("damp")
DRY = Humidity("dry")
ARID  = Humidity("arid")

ALL = [SOAKED, WET, DAMP, DRY, ARID]


# Helpers ##########################################################################################

def within(start:Humidity, end:Humidity) -> Iterable[Humidity]:
    return biomeTrait.within(ALL, start, end)
