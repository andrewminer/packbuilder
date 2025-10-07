# Class ############################################################################################

class BiomeTrait:
    """
    Any of the many characteristics which uniquely define a biome.
    """

    def __init__(self, name:str):
        self.name = name

    def __eq__(self, other) -> bool:
        if type(self).__name__ != type(other).__name__: return False
        if self.name != other.name: return False
        return True

    def __hash__(self) -> int:
        return hash((type(self).__name__, self.name))

    def __str__(self):
        return f"{type(self).__name__}: {self.name}"

    def __repr__(self) -> str:
        return f"{type(self).__name__}<{self.name}>"


# Helper Functions #################################################################################

def within(allTraits:list[BiomeTrait], start:BiomeTrait, end:BiomeTrait) -> list[BiomeTrait]:
    if not allTraits: return []
    start = start if start else allTraits[0]
    end = end if end else allTraits[-1]

    minIndex = 0
    maxIndex = len(allTraits) - 1

    for index, trait in enumerate(allTraits):
        if trait == start:
            minIndex = index
        elif trait == end:
            maxIndex = index

    if minIndex > maxIndex:
        minIndex, maxIndex = maxIndex, minIndex

    result = []
    for index in range(minIndex, maxIndex+1):
        result.append(allTraits[index])

    return result
