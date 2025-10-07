from mcpacker.model.core.world import World
from mcpacker.pack.mysteriousisland.biomecatalog import CATALOG as biomeCatalog
from mcpacker.pack.mysteriousisland.depositcatalog import CATALOG as depositCatalog
from mcpacker.pack.mysteriousisland.mineralcatalog import CATALOG as mineralCatalog
from mcpacker.pack.mysteriousisland.mobcatalog import CATALOG as mobCatalog


# Constants ########################################################################################

WORLD = World(biomeCatalog, depositCatalog, mineralCatalog, mobCatalog)
