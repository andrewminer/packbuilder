from mcpacker.model.core.ecology.biomefilter import BiomeFilter as BF
from mcpacker.model.core.geology.deposit.metaldeposit import MetalDeposit
from mcpacker.model.core.geology.depositcatalog import DepositCatalog
from mcpacker.model.core.geology.inclusion import Inclusion as I
from mcpacker.pack.mysteriousisland.mineralcatalog import CATALOG as M

import mcpacker.model.core.altitude         as AL
import mcpacker.model.core.ecology.flora    as FL
import mcpacker.model.core.ecology.geology  as GE
import mcpacker.model.core.ecology.heat     as HE
import mcpacker.model.core.ecology.humidity as HU
import mcpacker.model.core.ecology.soil     as SO
import mcpacker.model.core.ecology.water    as WA
import mcpacker.model.core.geology.bulk     as BU
import mcpacker.model.core.scarcity         as SC

# Catalog ##########################################################################################

CATALOG = C = DepositCatalog()

C.add(MetalDeposit(
    name        = "bif_iron",
    scarcity    = SC.COMMON,
    biomeFilter = BF([GE.METAMORPHIC, (HE.BOREAL, HE.FROZEN), HU.DAMP]),
    inclusions  = [I(M.get("iron"), 50), I(M.get("quartz"), 45), I(M.get("uranium"), 5)],
    bulk        = BU.LARGE,
    proportion  = 0.2,
))
