from mcpacker.model.modpack import ModPack
from mcpacker.write.locator import Locator
from pathlib import Path
from typing import Self

import os
import shutil


# Class ############################################################################################

class Writer:

    def __init__(self, pack:ModPack, outputDir:Path):
        self.locator = Locator(pack, outputDir)
        self.pack = pack

    def resetOutputFile(self, file:Path):
        if file.exists():
            os.remove(file)

        file.parent.mkdir(parents=True, exist_ok=True)

    def write(self) -> Self:
        self.doWrite()
        return self

    def doWrite(self):
        raise NotImplementedError()
