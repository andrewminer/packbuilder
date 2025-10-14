from collections.abc import Iterable
from mcpacker.model.modpack import ModPack
from mcpacker.write.compositewriter import CompositeWriter
from mcpacker.write.writer import Writer
from mcpacker.write.locator import Locator
from pathlib import Path
from zipfile import ZipFile
from zipfile import ZIP_DEFLATED

import mcpacker.json as json
import os


# Class ############################################################################################

class ZipWriter(CompositeWriter):

    @property
    def archiveFile(self) -> Path:
        raise NotImplementedError()

    @property
    def gatherFromDir(self) -> Path:
        raise NotImplementedError()

    def doWrite(self):
        archiveFile = self.archiveFile # grab before locator moves

        with self.locator.inTempDir():
            for writer in self._writers:
                writer.locator.outputDir = self.locator.outputDir
                writer.write()

            archiveFile.parent.mkdir(exist_ok=True, parents=True)

            with ZipFile(archiveFile, "w", ZIP_DEFLATED) as zipFile:
                for path in self.gatherFromDir.rglob("*"):
                    if not path.is_file(): continue
                    zipFile.write(path, path.relative_to(self.gatherFromDir.parent))
