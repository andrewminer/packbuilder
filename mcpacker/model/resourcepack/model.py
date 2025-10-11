from mcpacker.model.core.resourceid import ResourceId


# Class ############################################################################################

class Model:
    """
    Describes how to create a 2D or 3D representation of an object in the game
    """

    def __init__(self, parent:ResourceId, textures:dict[str,ResourceId]|None=None):
        self.parent = parent
        self.textures = {k:v for k,v in (textures or {}).items()}
