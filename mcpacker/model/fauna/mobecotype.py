from mcpacker.model.ecotype import Ecotype
from mcpacker.model.fauna.group import Group
from mcpacker.model.fauna.location import Location
from mcpacker.model.scarcity import Scarcity

import mcpacker.model.fauna.group as GR
import mcpacker.model.fauna.location as LO
import mcpacker.model.scarcity as SC


# Class ############################################################################################

class MobEcotype(Ecotype):

    def __init__(
        self,
        scarcity:Scarcity=SC.SPARSE,
        group:Group=GR.SOLO,
        location:Location=LO.OUTSIDE
    ):
        super().__init__(scarcity)
        self.group = group
        self.location = location

    def __str__(self) -> str:
        return f"{self.group!s}|{self.location!s}|{self.scarcity!s}"

    def __repr__(self) -> str:
        return (
            "MobEcotype("
                f"group={self.group!r}, "
                f"location={self.location!r}, "
                f"scarcity={self.scarcity!r}"
            ")"
        )
