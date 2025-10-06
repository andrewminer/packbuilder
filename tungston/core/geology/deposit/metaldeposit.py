from tungston.core.ecology.biomefilter import BiomeFilter
from tungston.core.geology.bulk import Bulk
from tungston.core.geology.deposit import Deposit
from tungston.core.geology.inclusion import Inclusion
from tungston.core.geology.proportion import Proportion
from tungston.core.scarcity import Scarcity

import tungston.core.geology.bulk       as BU
import tungston.core.geology.proportion as PR
import tungston.core.scarcity           as SC


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
