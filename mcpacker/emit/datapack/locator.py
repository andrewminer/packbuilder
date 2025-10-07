from os.path import join


# Class ############################################################################################

class Locator:

    def __init__(self, basePath:str):
        self.basePath = basePath

    def biomeModifier(self) -> str:
        return join(self.basePath, "data", self.mod, "neoforge", "biome_modifier")

    def blockTag(self) -> str:
        return join(self.basePath, "data", self.mod, "tags", "blocks")

    def configuredFeature(self) -> str:
        return join(self.basePath, "data", self.mod, "worldgen", "configured_feature")

    def function(self) -> str:
        return join(self.basePath, "data", self.mod, "functions")

    def placedFeature(self) -> str:
        return join(self.basePath, "data", self.mod, "worldgen", "placed_feature")

    def structure(self) -> str:
        return join(self.basePath, "data", self.mod, "worldgen", "structure")

    def structureNbt(self) -> str:
        return join(self.basePath, "data", self.mod, "structure")

    def structureSet(self) -> str:
        return join(self.basePath, "data", self.mod, "worldgen", "structure_set")

    def templatePool(self) -> str:
        return join(self.basePath, "data", self.mod, "worldgen", "template_pool")
