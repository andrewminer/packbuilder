from mcpacker.model.modpack import ModPack
from pathlib                import Path

import os
import shutil


# Class ############################################################################################

class Writer:

    def __init__(self, pack:ModPack, outputDir:Path):
        self.pack = pack
        self.outputDir = outputDir

    def resetOutputFile(self, file:Path):
        if file.exists():
            os.remove(file)
        file.parent.mkdir(parents=True, exist_ok=True)

    def write(self):
        raise NotImplementedError()
