from tungston.core.world import World
from tungston.modpacks.mysteriousisland.biomecatalog import CATALOG as biomeCatalog
from tungston.modpacks.mysteriousisland.depositcatalog import CATALOG as depositCatalog
from tungston.modpacks.mysteriousisland.mineralcatalog import CATALOG as mineralCatalog
from tungston.modpacks.mysteriousisland.mobcatalog import CATALOG as mobCatalog


# Constants ########################################################################################

WORLD = World(biomeCatalog, depositCatalog, mineralCatalog, mobCatalog)
