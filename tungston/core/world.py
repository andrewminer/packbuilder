from tungston.core.ecology.biomecatalog import BiomeCatalog
from tungston.core.fauna.mobcatalog import MobCatalog
from tungston.core.geology.mineralcatalog import MineralCatalog
from tungston.core.geology.depositcatalog import DepositCatalog


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
