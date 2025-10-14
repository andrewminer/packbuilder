from mcpacker.format.textcomposer import TextComposer
from mcpacker.model.modpack import ModPack
from mcpacker.write.writer import Writer
from pathlib import Path


# Class ############################################################################################

class TextWriter(Writer):

    def __init__(self, pack:ModPack, outputDir:Path, filePath:Path, composer:TextComposer):
        super().__init__(pack, outputDir)
        self.composer = composer
        self.filePath = filePath

    def doWrite(self):
        path = self.locator.root() / self.filePath
        self.resetOutputFile(path)

        with path.open("w") as file:
            file.write(str(self.composer.compose()))
