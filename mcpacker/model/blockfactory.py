from mcpacker.model.resourcepack.blockstate import BlockState
from mcpacker.model.resourcepack.variant import Variant
from mcpacker.model.resourcepack.model import Model
from mcpacker.model.modpack import ModPack
from mcpacker.model.core.resourceid import ResourceId


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

