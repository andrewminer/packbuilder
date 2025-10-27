from mcpacker.model.catalog import Catalog
from mcpacker.model.ecology.biome import Biome
from mcpacker.model.fauna.mob import Mob
from mcpacker.model.fauna.mobspawn import MobSpawn
from mcpacker.model.flora.plant import Plant
from mcpacker.model.flora.plantspawn import PlantSpawn
from mcpacker.model.geology.mineral import Mineral
from mcpacker.model.geology.mineralspawn import MineralSpawn
from mcpacker.model.material.block import Block
from mcpacker.model.material.item import Item


# Class ############################################################################################

class World:

    def __init__(self):
        self.biomes = Catalog[Biome]()
        self.blocks = Catalog[Block]()
        self.items = Catalog[Item]()
        self.minerals = Catalog[Mineral]()
        self.mineralSpawns = Catalog[MineralSpawn]()
        self.mobs = Catalog[Mob]()
        self.mobSpawns = Catalog[MobSpawn]()
        self.plants = Catalog[Plant]()
        self.plantSpawns = Catalog[PlantSpawn]()

    def __str__(self) -> str:
        return (
            "World("
                f"{len(self.biomes)} biomes, "
                f"{len(self.blocks)} blocks, "
                f"{len(self.items)} items, "
                f"{len(self.minerals)} minerals, "
                f"{len(self.mineralSpawns)} mineralSpawns, "
                f"{len(self.mobs)} mobs, "
                f"{len(self.mobSpawns)} mobSpawns, "
                f"{len(self.plants)} plants, "
                f"{len(self.plantSpawns)} plantSpawns"
            ")"
        )

    def __repr__(self) -> str:
        return (
            "World("
                f"biomes={self.biomes!r}, "
                f"blocks={self.blocks!r}, "
                f"items={self.items!r}, "
                f"minerals={self.minerals!r}, "
                f"mineralSpawns={self.mineralSpawns!r}, "
                f"mobs={self.mobs!r}, "
                f"mobSpawns={self.mobSpawns!r}, "
                f"plants={self.plants!r}, "
                f"plantSpawns={self.plantSpawns!r}"
            ")"
        )
