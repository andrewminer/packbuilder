from mcpacker.format.resourcepack.blockstate import BlockState
from mcpacker.format.resourcepack.variant import Variant
from mcpacker.format.resourcepack.model import Model
from mcpacker.model.modpack import ModPack
from mcpacker.model.resourceid import ResourceId
from mcpacker.format.datapack.recipe.shapedrecipe import ShapedRecipe


# Class ############################################################################################

class BlockFactory:

    def __init__(self, pack:ModPack):
        self.pack = pack

    def makeBasicBlock(self, name:str, gameId:ResourceId):
        basicCubeModelId = ResourceId.parse("block/cube_all")
        textureId = ResourceId.parse(f"{gameId.mod}:block/{gameId.name}")
        blockId = ResourceId.parse(f"{gameId.mod}:block/{gameId.name}")

        resource = self.pack.resourcePack.get(gameId.mod)
        resource.blockModels.append(Model(basicCubeModelId, {"all": textureId}))
        resource.itemModels.append(Model(blockId))
        resource.blockStates.append(BlockState(Variant(blockId)))

        data = self.pack.dataPack.get(gameId.mod)
