from collections.abc import Iterable
from mcpacker.model.geology.replacement import Replacement
from mcpacker.model.resourceid import ResourceId
from mcpacker.model.spawnable import Spawnable


# Class ############################################################################################

class Mineral(Spawnable):

    def __init__(self, name:str, replacements:Iterable[Replacement]|Replacement):
        super().__init__(name)

        if isinstance(replacements, Replacement):
            replacements = [replacements]

        self.name = name
        self.replacements = list(replacements)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return (
            "Mineral("
                f"name={self.name!r}, "
                f"replacements={self.replacements!r}"
            ")"
        )
