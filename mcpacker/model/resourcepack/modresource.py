# Class ############################################################################################

class ModResource:

    def __init__(self, name:str):
        self.name = name
        self.blockStates:list[str] = []
        self.models:list[str] = []
        self.textures:list[str] = []
