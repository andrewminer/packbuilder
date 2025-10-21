from collections.abc import Iterable
from mcpacker.model.altitude import Altitude
from mcpacker.model.ecology.biomefilter import BiomeFilter
from mcpacker.model.geology.bulk import Bulk
from mcpacker.model.geology.deposit import Deposit
from mcpacker.model.geology.mineral import Mineral
from mcpacker.model.scarcity import Scarcity

import mcpacker.model.altitude as altitude
import mcpacker.model.scarcity as scarcity


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
