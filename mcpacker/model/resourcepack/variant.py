from mcpacker.model.core.resourceid import ResourceId


# Class ############################################################################################

class Variant:

    def __init__(self, model:ResourceId|str, x:int=0, y:int=0, uvlock:bool=False, weight:int=1):
        self.model = ResourceId.parse(model)
        self.x = x
        self.y = y
        self.uvlock = uvlock
        self.weight = weight
