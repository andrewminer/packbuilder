from mcpacker.format.resourcepack.blockstate import BlockState
from mcpacker.format.resourcepack.model import Model


# Class ############################################################################################

class ModResource:

    def __init__(self, mod:str):
        self.mod = mod
        self.blockStates:list[BlockState] = []
        self.blockModels:list[Model] = []
        self.itemModels:list[Model] = []
