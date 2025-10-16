from collections.abc import Iterable
from mcpacker.model.modpack import ModPack
from mcpacker.write.locator import Locator
from mcpacker.write.writer import Writer
from pathlib import Path


# Class ############################################################################################

class CompositeWriter(Writer):

    def __init__(
        self,
        pack:ModPack,
        outputDir:Path,
        writers:Iterable[Writer]|None=None,
    ):
        super().__init__(pack, outputDir)
        self._writers:list[Writer] = list(writers or [])

    def doWrite(self):
        for writer in self._writers:
            writer.write()
