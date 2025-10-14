from mcpacker.write.zipwriter import ZipWriter
from pathlib import Path


# Class ############################################################################################

class ResourcePackWriter(ZipWriter):

    @property
    def archiveFile(self) -> Path:
        return self.locator.resourcePacks() / f"{self.pack.name}.jar"

    @property
    def gatherFromDir(self) -> Path:
        return self.locator.resourcePack()
