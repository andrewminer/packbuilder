from collections.abc import Iterable
from mcpacker.model.ecotype import Ecotype
from mcpacker.model.habitat import Habitat
from mcpacker.model.spawnable import Spawnable


# Class ############################################################################################

class Spawn[SpawnableKind: Spawnable, EcotypeKind: Ecotype]:
    """
    Abstract base class for placing something into a habitat with local variations.
    """

    def __init__(self, name:str, habitat:Habitat, spawnable:SpawnableKind, ecotype:EcotypeKind):
        self.ecotype = ecotype
        self.habitat = habitat
        self.name = name
        self.spawnable = spawnable

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}("
                f"ecotype={self.ecotype!r}, "
                f"habitat={self.habitat!r}, "
                f"name={self.name!r}, "
                f"spawnable={self.spawnable!r}"
            ")"
        )
