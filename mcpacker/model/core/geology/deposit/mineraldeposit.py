from collections.abc import Iterable
from mcpacker.model.core.altitude import Altitude
from mcpacker.model.core.ecology.biomefilter import BiomeFilter
from mcpacker.model.core.geology.bulk import Bulk
from mcpacker.model.core.geology.deposit import Deposit
from mcpacker.model.core.geology.inclusion import Inclusion
from mcpacker.model.core.geology.proportion import Proportion
from mcpacker.model.core.scarcity import Scarcity

import mcpacker.model.core.altitude as AL
import mcpacker.model.core.geology.bulk as BU
import mcpacker.model.core.geology.proportion as PR
import mcpacker.model.core.scarcity as SC


# Class ############################################################################################

class MineralDeposit(Deposit):

    def __init__(
        self,
        name:str,
        altitude:Altitude=AL.ANYWHERE,
        biomeFilters:Iterable[BiomeFilter]|BiomeFilter|None=None,
        bulk:Bulk=BU.MEDIUM,
        inclusions:Iterable[Inclusion]|None=None,
        proportion:Proportion=PR.BODY,
        scarcity:Scarcity=SC.SPARSE,
    ):
        super().__init__(name, altitude, biomeFilters, scarcity)

        self.bulk = bulk
        self.inclusions = list(inclusions or [])
        self.proportion = proportion

    def __repr__(self) -> str:
        return "".join([str(p) for p in [
            "MineralDeposit(" +
                "name=", repr(self.name), ", ",
                "altitude=", repr(self.altitude), ", ",
                "biomeFilters=", repr(self.biomeFilters), ", ",
                "bulk=", repr(self.bulk), ", ",
                "inclusions=[", ", ".join([repr(m) for m in self.inclusions]), "], ",
                "proportion=", repr(self.proportion), ", ",
                "scarcity=", repr(self.scarcity),
            ")"
        ]])

    def __str__(self) -> str:
        return self.name
