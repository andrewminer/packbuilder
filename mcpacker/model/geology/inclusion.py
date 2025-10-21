from mcpacker.model.geology.mineral import Mineral


# Class ############################################################################################

class Inclusion:

    def __init__(self, mineral:Mineral, weight:int=100):
        self.mineral = mineral
        self.weight = weight

    def __str__(self) -> str:
        if self.weight == 100:
            return self.mineral.name

        return f"{self.mineral.name} ({self.weight}%)"

    def __repr__(self) -> str:
        return "".join([str(p) for p in [
            "Inclusion(",
                "mineral=", repr(self.mineral), ", ",
                "weight=", repr(self.weight),
            ")"
        ]])
