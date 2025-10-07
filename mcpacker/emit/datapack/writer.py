from mcpacker.model.core.world import World


# Class ############################################################################################

class Writer:

    def __init__(self, world:World):
        self.world = world

    def write(self):
        raise NotImplementedError()
