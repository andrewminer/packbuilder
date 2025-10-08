from mcpacker.model.core.material.item import Item


# Class ############################################################################################

class Loot:

    def __init__(self, item:Item, maxCount:int=1, minCount:int=1, weight:int=1):
        self.item = item
        self.maxCount = maxCount
        self.minCount = minCount
        self.weight = weight

    def __repr__(self) -> str:
        return "".join([repr(p) for p in [
            "Loot{",
                "item: ", self.item, ", ",
                "minCount: ", self.minCount, ", ",
                "weight: ", self.weight,
            "}"
        ]])

    def __str__(self) -> str:
        return f"{str(item)} ({self.minCount}..{self.maxCount} @ {self.weight})"
