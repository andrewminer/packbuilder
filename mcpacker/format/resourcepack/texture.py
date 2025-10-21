from mcpacker.format.resourcepack.kind import Kind


# Class ############################################################################################

class Texture:

    def __init__(self, imageFileName:str, kind:Kind):
        self.imageFileName = imageFileName
        self.kind = kind
