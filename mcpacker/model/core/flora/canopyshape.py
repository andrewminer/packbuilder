from typing import Any


# Class ############################################################################################

class CanopyShape:

    def __init__(self, name:str):
        self.name = name

    def __eq__(self, other:Any) -> bool:
        if type(self) != type(other): return False
        if self.name != other.name: return False
        return True

    def __hash__(self) -> int:
        return hash(self.name)

    def __lt__(self, other:Any) -> bool:
        if type(self) != type(other): raise ValueError()
        return self.name < other.name

    def __repr__(self) -> str:
        return f"CanopyShape(name={repr(self.name)})"

    def __str__(self) -> str:
        return self.name


# Constants ########################################################################################

ACACIA = CanopyShape("acacia")
BLOB = CanopyShape("blob")
BUSH = CanopyShape("bush")
CHERRY = CanopyShape("cherry")
DARK_OAK = CanopyShape("dark_oak")
FANCY = CanopyShape("fancy")
JUNGLE = CanopyShape("jungle")
MEGA_PINE = CanopyShape("mega_pine")
PINE = CanopyShape("pine")
RANDOM_SPREAD = CanopyShape("random_spread")
SPRUCE = CanopyShape("spruce")

ALL = [ACACIA, BLOB, BUSH, CHERRY, DARK_OAK, FANCY, JUNGLE, MEGA_PINE, PINE, RANDOM_SPREAD, SPRUCE]
