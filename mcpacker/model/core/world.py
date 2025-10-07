from mcpacker.model.core.ecology.biomecatalog import BiomeCatalog
from mcpacker.model.core.fauna.mobcatalog import MobCatalog
from mcpacker.model.core.geology.depositcatalog import DepositCatalog
from mcpacker.model.core.geology.mineralcatalog import MineralCatalog


# Class ############################################################################################

class World:

    def __init__(
        self,
        biomes:BiomeCatalog,
        deposits:DepositCatalog,
        minerals:MineralCatalog,
        mobs:MobCatalog
    ):
        self.biomes = biomes
        self.deposits = deposits
        self.minerals = minerals
        self.mobs = mobs
