from tungston.core.ecology.biometrait import BiomeTrait

import tungston.core.ecology.biometrait as biomeTrait


# Class ############################################################################################

class Humidity(BiomeTrait):
    """
    The general level of humidity present in the air.
    """
    pass


# Constants ########################################################################################

WET  = Humidity("wet")
DAMP = Humidity("damp")
DRY  = Humidity("dry")

ALL = [WET, DAMP, DRY]

# Helpers ##########################################################################################

def within(start:Humidity, end:Humidity) -> list[Humidity]:
    return biomeTrait.within(ALL, start, end)
