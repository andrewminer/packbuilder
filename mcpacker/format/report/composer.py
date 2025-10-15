from mcpacker.format.textcomposer import TextComposer
from mcpacker.model.modpack import ModPack


# Class ############################################################################################

class ReportComposer(TextComposer):

    def __init__(self, pack:ModPack):
        super().__init__()
        self.pack = pack
