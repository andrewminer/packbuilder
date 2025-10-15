from collections.abc import Iterable
from mcpacker.model.core.altitude import Altitude
from mcpacker.model.core.ecology.biomefilter import BiomeFilter
from mcpacker.model.core.geology.bulk import Bulk
from mcpacker.model.core.geology.deposit import Deposit
from mcpacker.model.core.geology.mineral import Mineral
from mcpacker.model.core.scarcity import Scarcity

import mcpacker.model.core.altitude as altitude
import mcpacker.model.core.scarcity as scarcity


# Class ############################################################################################

class GeodeDeposit(Deposit):

    def __init__(
        self,
        name:str,
        altitude:Altitude=altitude.ANYWHERE,
        biomeFilters:Iterable[BiomeFilter]|BiomeFilter|None=None,
        scarcity:Scarcity=scarcity.SPARSE,
    ):
        super().__init__(name, altitude, biomeFilters, scarcity)
        # TODO: add geode layers
