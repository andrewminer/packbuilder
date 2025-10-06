from tungston.core.ecology.biomefilter import BiomeFilter
from tungston.core.geology.bulk import Bulk
from tungston.core.geology.mineral import Mineral
from tungston.core.scarcity import Scarcity

import tungston.core.scarcity as scarcity


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

