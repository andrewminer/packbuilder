# Class ############################################################################################

class Group:
    """
    How many individuals are commonly present when encountering a creature.
    """

    def __init__(self, name:str, smallest:int, largest:int):
        self.name = name
        self.smallest = smallest
        self.largest = largest

    def __eq__(self, other) -> bool:
        if type(other) != type(self): return False
        if other.largest != self.largest: return False
        if other.smallest != self.smallest: return False
        return True

    def __hash__(self) -> int:
        return hash((self.smallest, self.largest))

    def __str__(self) -> str:
        return f"{self.name} ({self.smallest} to {self.largest})"

    def __repr__(self) -> str:
        return f"Group(name='{self.name}', smallest={self.smallest}, largest={self.largest})"


# Constants ########################################################################################

SOLO   = Group("solo",   1, 1)
PAIR   = Group("pair",   2, 2)
FAMILY = Group("family", 2, 4)
TROUP  = Group("troup",  3, 6)
HERD   = Group("herd",   4, 8)

ALL = [SOLO, PAIR, FAMILY, TROUP, HERD]


# Helper Functions #################################################################################

def merge(*groups:Group):
    if not groups: return SOLO

    smallest = ALL[-1].largest
    smallestGroup = ALL[-1]

    largest = ALL[0].smallest
    largestGroup = ALL[0]

    for group in groups:
        if group.smallest < smallest:
            smallest = group.smallest
            smallestGroup = group

        if group.largest > largest:
            largest = group.largest
            largestGroup = group

    return Group(f"{smallestGroup.name} to {largestGroup.name}", smallest, largest)
