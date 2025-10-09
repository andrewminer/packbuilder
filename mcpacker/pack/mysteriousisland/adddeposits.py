from mcpacker.model.core.ecology.biomefilter          import BiomeFilter as BF
from mcpacker.model.core.geology.deposit.metaldeposit import MetalDeposit
from mcpacker.model.core.geology.inclusion            import Inclusion as I
from mcpacker.model.modpack                           import ModPack

import mcpacker.model.core.altitude           as AL
import mcpacker.model.core.ecology.flora      as FL
import mcpacker.model.core.ecology.geology    as GE
import mcpacker.model.core.ecology.heat       as HE
import mcpacker.model.core.ecology.humidity   as HU
import mcpacker.model.core.ecology.soil       as SO
import mcpacker.model.core.ecology.water      as WA
import mcpacker.model.core.geology.bulk       as BU
import mcpacker.model.core.geology.proportion as PR
import mcpacker.model.core.scarcity           as SC

# Catalog ##########################################################################################

def addDeposits(pack:ModPack):
    minerals = pack.world.minerals
    deposits = pack.world.deposits

    deposits.add(MetalDeposit(
        name = "bif_iron",
        scarcity = SC.COMMON,
        biomeFilter = BF([GE.METAMORPHIC, (HE.BOREAL, HE.FROZEN), HU.DAMP]),
        inclusions = [
            I(minerals["iron"], 50),
            I(minerals["quartz"], 45),
            I(minerals["uranium"], 5)
        ],
        bulk = BU.LARGE,
        proportion = PR.BED,
    ))
