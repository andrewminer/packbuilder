from collections.abc import Iterable


# Class ############################################################################################

class Altitude:
    """
    A range of world heights from a bottom to a top.
    """

    def __init__(self, name:str, bottom:int, top:int):
        self.name = name
        self.bottom = bottom
        self.top = top

    def __eq__(self, other) -> bool:
        if type(self) != type(other): return False
        if self.bottom != other.bottom: return False
        if self.top != other.top: return False
        return True

    def __hash__(self) -> int:
        return hash((self.bottom, self.top))

    def __str__(self) -> str:
        return f"{self.name} ({self.bottom} to {self.top})"

    def __repr__(self) -> str:
        return f"Altitude(name={self.name}, bottom={self.bottom}, top={self.top})"


# Constants ########################################################################################

# Aboveground
SKY        = Altitude("sky",     284, 316)
SUMMIT     = Altitude("summit",  252, 284)
PEAKS      = Altitude("peaks",   222, 252)
CRAGS      = Altitude("crags",   190, 222)
ALPINE     = Altitude("alpine",  156, 190)
HILLS      = Altitude("hills",   124, 156)
UPLANDS    = Altitude("uplands",  92, 124)
LOWLANDS   = Altitude("lowlands", 70,  92)
DUNES      = Altitude("dunes",    62,  70)

# Transition
EVAPORITES = Altitude("evaporites",  60,  64)
ANYWHERE   = Altitude("anywhere",   -64, 320)

# Underground
SOIL       = Altitude("soil",        48,  62)
SUBSTRATE  = Altitude("substrate",   32,  48)
OVERBURDEN = Altitude("overburden",   0,  32)
CRUST      = Altitude("crust",      -32,  32)
MANTLE     = Altitude("mantle",     -54, -32)
PLUTONIC   = Altitude("plutonic",   -64, -54)

# Underwater
SURFACE    = Altitude("surface",  58,  62)
SHALLOWS   = Altitude("shallows", 46,  58)
DEEPS      = Altitude("deeps",     0,  46)
ABYSS      = Altitude("abyss",   -32,   0)

# Groups
OVERGROUND  = (DUNES, LOWLANDS, UPLANDS, HILLS, ALPINE, CRAGS, PEAKS, SUMMIT, SKY)
UNDERGROUND = (SOIL, SUBSTRATE, OVERBURDEN, CRUST, MANTLE, PLUTONIC)
UNDERWATER  = (SURFACE, SHALLOWS, DEEPS, ABYSS)

ALL = OVERGROUND + UNDERGROUND + UNDERWATER


# Helper Functions #################################################################################

def span(*altitudes:Altitude):
    if not altitudes: return ANYWHERE
    result = Altitude("", ANYWHERE.top, ANYWHERE.bottom)

    bottom = OVERGROUND[-1].top
    bottomAltitude = OVERGROUND[-1]

    top = UNDERGROUND[-1].bottom
    topAltitude = UNDERGROUND[-1]

    for altitude in altitudes:
        if altitude.bottom < bottom:
            bottom = altitude.bottom
            bottomAltitude = altitude

        if altitude.top > top:
            top = altitude.top
            topAltitude = altitude

    if bottomAltitude == topAltitude:
        return bottomAltitude

    result = Altitude(f"{bottomAltitude.name} to {topAltitude.name}", bottom, top)
    return result
