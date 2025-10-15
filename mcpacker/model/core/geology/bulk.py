from typing import Any
import math


# Class ############################################################################################

class Bulk:

    def __init__(self, name:str, smallest:int, largest:int):
        self.name = name
        self.smallest = smallest
        self.largest = largest

    def __eq__(self, other:Any) -> bool:
        if type(self) != type(other): return False
        if self.name != other.name: return False
        return True

    def __hash__(self) -> int:
        return hash(self.name)

    def __repr__(self) -> str:
        return f"Bulk(name='{self.name}', smallest={self.smallest}, largest={self.largest})"

    def __str__(self) -> str:
        return f"{self.name} ({self.smallest} to {self.largest})"

    def scale(self, factor) -> "Bulk":
        return Bulk(
            self.name,
            math.floor(self.smallest * factor),
            math.floor(self.largest * factor)
        )


# Constants ########################################################################################

TINY   = Bulk("tiny",   250,  500)
SMALL  = Bulk("small",  500,  750)
MEDIUM = Bulk("small",  750, 1000)
LARGE  = Bulk("large", 1250, 1500)
HUGE   = Bulk("huge",  1500, 1750)

ALL = [TINY, SMALL, MEDIUM, LARGE, HUGE]
