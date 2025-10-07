from mcpacker.model.core.ecology.biomefilter import BiomeFilter
from mcpacker.model.core.geology.bulk import Bulk
from mcpacker.model.core.geology.mineral import Mineral
from mcpacker.model.core.scarcity import Scarcity

import mcpacker.model.core.scarcity as scarcity


# Class ############################################################################################

class Deposit:

    def __init__(
        self,
        name:str,
        scarcity:Scarcity=scarcity.SPARSE,
        biomeFilter:BiomeFilter|None=None,
    ):
        self.name = name
        self.biomeFilter = biomeFilter or BiomeFilter()
        self.scarcity = scarcity

