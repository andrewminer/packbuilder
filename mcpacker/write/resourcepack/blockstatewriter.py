from mcpacker.write.writer import Writer

# Class ############################################################################################

class BlockStateWiter(Writer):

    def write(self):
        for mod in self.pack.resourcePack.mods:
            for blockState in mod.blockStates:
                path = self.outputDir/self.pack.name/"resourcepacks"


