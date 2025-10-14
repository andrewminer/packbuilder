from collections.abc import Iterable
from mcpacker.model.modpack import ModPack
from mcpacker.write.compositewriter import CompositeWriter
from mcpacker.write.writer import Writer
from mcpacker.write.locator import Locator
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile
from zipfile import ZIP_DEFLATED

import mcpacker.json as json
import os


# Class ############################################################################################

class DataPackWriter(CompositeWriter):

    def doWrite(self):
        outputDir = self.locator.outputDir
        archivePath = self.locator.dataPacks() / f"{self.pack.name}.jar"

        with TemporaryDirectory() as buildDir:
            self.locator.outputDir = Path(buildDir)
            for writer in self._writers:
                writer.locator.outputDir = self.locator.outputDir
                writer.write()

            dataPackPath = self.locator.dataPack()
            archivePath.parent.mkdir(exist_ok=True, parents=True)

            with ZipFile(archivePath, "w", ZIP_DEFLATED) as zipFile:
                for path in dataPackPath.rglob("*"):
                    if not path.is_file(): continue
                    zipFile.write(path, path.relative_to(dataPackPath.parent))

        self.locator.outputDir = outputDir
