from mcpacker.model.core.ecology.biomefilter import BiomeFilter
from mcpacker.model.core.geology.bulk import Bulk
from mcpacker.model.core.geology.deposit import Deposit
from mcpacker.model.core.geology.inclusion import Inclusion
from mcpacker.model.core.geology.proportion import Proportion
from mcpacker.model.core.scarcity import Scarcity

import mcpacker.model.core.geology.bulk       as BU
import mcpacker.model.core.geology.proportion as PR
import mcpacker.model.core.scarcity           as SC


# Class ############################################################################################

class MetalDeposit(Deposit):

    def __init__(
        self,
        name:str,
        inclusions:tuple[Inclusion],
        bulk:Bulk=BU.MEDIUM,
        proportion:Proportion=PR.BODY,
        biomeFilter:BiomeFilter=None,
        scarcity:Scarcity=SC.SPARSE,
    ):
        super().__init__(name, scarcity, biomeFilter)
        self.inclusions = inclusions
        self.bulk = bulk
        self.proportion = proportion

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return "".join([str(p) for p in [
            "MetalDeposit<", self.name, ">{",
                "scarcity: ", repr(self.scarcity), ", ",
                "biomeFilter: ", self.biomeFilter, ", ",
                "inclusions: [", ", ".join([repr(m) for m in self.inclusions]), "], ",
                "bulk: ", repr(self.bulk), ", ",
                "proportion: ", repr(self.proportion),
            "}"
        ]])
