from mcpacker.write.zipwriter import ZipWriter
from pathlib import Path


# Class ############################################################################################

class DataPackWriter(ZipWriter):
    """
    Write a zip file containing the modpack's own datapack.
    """

    @property
    def archiveFile(self) -> Path:
        return self.locator.dataPacks() / f"{self.pack.name}.jar"

    @property
    def gatherFromDir(self) -> Path:
        return self.locator.dataPack()
