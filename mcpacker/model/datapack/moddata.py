from mcpacker.model.datapack.configuredfeature import ConfiguredFeature
from mcpacker.model.datapack.placedfeature import PlacedFeature
from typing import Any


# Class ############################################################################################

class ModData:

    def __init__(self, name:str):
        self.name = name
        self.biomeModifiers:list[Any] = []
        self.configuredFeatures:list[ConfiguredFeature] = []
        self.functions:list[Any] = []
        self.functionTags:list[Any] = []
        self.lootModifiers:list[Any] = []
        self.lootTables:list[Any] = []
        self.placedFeatures:list[PlacedFeature] = []
        self.recipes:list[Any] = []
        self.structures:list[Any] = []
        self.structureSets:list[Any] = []
        self.tags:list[Any] = []
        self.templatePools:list[Any] = []
