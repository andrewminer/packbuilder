import math


# Class ############################################################################################

class Bulk:

    def __init__(self, name:str, smallest:int, largest:int):
        self.name = name
        self.smallest = smallest
        self.largest = largest

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Bulk<{self.name}>{{smallest: {self.smallest}, largest: {self.largest}}}"

    def scale(self, factor) -> "Bulk":
        return Bulk(
            self.name,
            math.floor(self.smallest * factor),
            math.floor(self.largest * factor)
        )


# Constants ########################################################################################

SMALL  = Bulk("tiny", 250, 500)
MEDIUM = Bulk("small", 500, 1000)
LARGE  = Bulk("small", 1000, 2000)

ALL = [SMALL, MEDIUM, LARGE]
