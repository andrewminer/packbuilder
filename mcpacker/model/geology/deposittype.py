from typing import Any


# Class ############################################################################################

class DepositType:

    def __init__(self, name:str):
        self.name = name

    def __eq__(self, other:Any) -> bool:
        if type(self) != type(other): return False
        if self.name != other.name: return False
        return True

    def __hash__(self) -> int:
        return hash(self.name)

    def __repr__(self) -> str:
        return f"DepositType(name={self.name!r})"

    def __str__(self) -> str:
        return self.name


# Constants ########################################################################################

VEIN = DepositType("vein")
DISK = DepositType("disk")
STRATA = DepositType("strata")

ALL = [VEIN, STRATA]
