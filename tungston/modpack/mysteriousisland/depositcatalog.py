from tungston.core.ecology.biomefilter import BiomeFilter as BF
from tungston.core.geology.deposit.metaldeposit import MetalDeposit
from tungston.core.geology.depositcatalog import DepositCatalog
from tungston.core.geology.inclusion import Inclusion as I
from tungston.modpack.mysteriousisland.mineralcatalog import CATALOG as M

import tungston.core.altitude         as AL
import tungston.core.ecology.flora    as FL
import tungston.core.ecology.geology  as GE
import tungston.core.ecology.heat     as HE
import tungston.core.ecology.humidity as HU
import tungston.core.ecology.soil     as SO
import tungston.core.ecology.water    as WA
import tungston.core.geology.bulk     as BU
import tungston.core.scarcity         as SC

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
