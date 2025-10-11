from mcpacker.model.modpack import ModPack
from mcpacker.write.writer  import Writer
from pathlib                import Path

import shutil


# Constants ########################################################################################

SOURCE_BASE = Path("mcpacker") / "pack"


# Class ############################################################################################

class StaticWriter(Writer):

    def __init__(self, pack:ModPack, outputDir:Path):
        super().__init__(pack, outputDir)

    def write(self):
        sourcePath = SOURCE_BASE / self.pack.name / "static"
        targetPath = self.outputDir / self.pack.name
        shutil.copytree(sourcePath, targetPath, dirs_exist_ok=True)
