# Class ############################################################################################

class Proportion:

    def __init__(self, name:str, ratio:float):
        self.name = name
        self.ratio = ratio

    def __eq__(self, other) -> bool:
        if type(self) != type(other): return False
        if self.name != other.name: return False
        return True

    def __hash__(self) -> int:
        return hash(self.name)

    def __str__(self) -> str:
        return f"{self.name} ({self.ratio})"

    def __repr__(self) -> str:
        return f"Proportion(name='{self.name}', ratio={self.ratio})"


# Constants ########################################################################################

BED   = Proportion("bed",   0.1) # salt, nitrate, redbed, loam, bif iron, peat coal
LENS  = Proportion("lens",  0.4) # bit.coal, aluminum, lapis, quartzite
LODE  = Proportion("lode",  0.7) # au.quartz, mvt lead
BODY  = Proportion("body",  1.0) # sed.iron
STOCK = Proportion("stock", 1.3) # tin
VENT  = Proportion("vent",  1.6) # sulfur
PIPE  = Proportion("pipe",  1.9) # por.copper

ALL = [BED, LENS, LODE, BODY, STOCK, VENT, PIPE]
