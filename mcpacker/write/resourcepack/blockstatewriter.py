from mcpacker.write.writer import Writer

# Class ############################################################################################

class BlockStateWriter(Writer):

    def doWrite(self):
        for mod in self.pack.resourcePack.mods:
            for blockState in mod.blockStates:
                path = self.locator.blockStates() # filename?
                # TODO: not implemented


