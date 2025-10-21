from mcpacker.model.core.ecology.biomecatalog import BiomeCatalog
from mcpacker.model.core.fauna.mobcatalog import MobCatalog
from mcpacker.model.core.fauna.mobspawncatalog import MobSpawnCatalog
from mcpacker.model.core.flora.plantcatalog import PlantCatalog
from mcpacker.model.core.flora.plantspawncatalog import PlantSpawnCatalog
from mcpacker.model.core.geology.depositcatalog import DepositCatalog
from mcpacker.model.core.geology.mineralcatalog import MineralCatalog
from mcpacker.model.core.material.blockcatalog import BlockCatalog
from mcpacker.model.core.material.itemcatalog import ItemCatalog


# Class ############################################################################################

class World:

    def __init__(
        self,
        biomes:BiomeCatalog|None=None,
        blocks:BlockCatalog|None=None,
        deposits:DepositCatalog|None=None,
        items:ItemCatalog|None=None,
        minerals:MineralCatalog|None=None,
        mobs:MobCatalog|None=None,
        mobSpawns:MobSpawnCatalog|None=None,
        plants:PlantCatalog|None=None,
        plantSpawns:PlantSpawnCatalog|None=None,
    ):
        self.biomes = biomes or BiomeCatalog()
        self.blocks = blocks or BlockCatalog()
        self.deposits = deposits or DepositCatalog()
        self.items = items or ItemCatalog()
        self.minerals = minerals or MineralCatalog()
        self.mobs = mobs or MobCatalog()
        self.mobSpawns = mobSpawns or MobSpawnCatalog()
        self.plants = plants or PlantCatalog()
        self.plantSpawns = plantSpawns or PlantSpawnCatalog()

    def __repr__(self) -> str:
        return "".join([
            "World(",
                "biomes=", repr(self.biomes), ", ",
                "blocks=", repr(self.blocks), ", ",
                "deposits=", repr(self.deposits), ", ",
                "items=", repr(self.items), ", ",
                "minerals=", repr(self.minerals), ", ",
                "mobs=", repr(self.mobs), ", ",
                "mobSpawns=", repr(self.mobSpawns), ", ",
                "plants=", repr(self.plants), ", ",
                "plantSpawns=", repr(self.plantSpawns),
            ")"
        ])
