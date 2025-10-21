from typing import Any


# Class ############################################################################################

class Density:

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
        return f"Density(name={repr(self.name)})"

    def __str__(self) -> str:
        return self.name


# Constants ########################################################################################

SPARSE = Density("sparse")
THIN = Density("thin")
THICK = Density("thick")
PACKED = Density("packed")
CARPET = Density("carpet")

ALL = [SPARSE, THIN, THICK, PACKED, CARPET]
