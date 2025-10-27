from mcpacker.model.ecotype import Ecotype
from mcpacker.model.geology.bulk import Bulk
from mcpacker.model.geology.deposittype import DepositType
from mcpacker.model.scarcity import Scarcity
from mcpacker.model.resourceid import ResourceId

import mcpacker.model.geology.bulk as BU
import mcpacker.model.geology.deposittype as DE



# Class ############################################################################################

class MineralEcotype(Ecotype):

    def __init__(self, scarcity:Scarcity, bulk:Bulk=BU.MEDIUM, depositType:DepositType=DE.VEIN):
        super().__init__(scarcity)
        self.bulk = bulk
        self.depositType = depositType
