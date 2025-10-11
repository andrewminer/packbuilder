from collections.abc        import Iterable
from mcpacker.model.modpack import ModPack
from mcpacker.write.writer  import Writer
from pathlib                import Path
from typing                 import TypeVar

import os
import shutil


# Type Support #####################################################################################

WriterSubclass = TypeVar("WriterSubclass", bound=Writer)


# Class ############################################################################################

class CompositeWriter(Writer):

    def __init__(
        self,
        pack:ModPack,
        outputDir:Path,
        writers:Iterable[type[WriterSubclass]]|None=None
    ):
        super().__init__(pack, outputDir)

        self._writers:list[Writer] = []
        for writerClass in (writers or []):
            self.add(writerClass)

    def add(self, writerClass:type[WriterSubclass]):
        self._writers.append(writerClass(self.pack, self.outputDir))

    def write(self):
        for writer in self._writers:
            writer.write()
