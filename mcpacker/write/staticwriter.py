from mcpacker.model.modpack import ModPack
from mcpacker.write.writer  import Writer
from pathlib                import Path

import shutil


# Constants ########################################################################################

SOURCE_BASE = Path("mcpacker") / "pack"


# Class ############################################################################################

class StaticWriter(Writer):

    def doWrite(self):
        sourcePath = SOURCE_BASE / self.pack.name / "static"
        targetPath = self.locator.root()
        shutil.copytree(sourcePath, targetPath, dirs_exist_ok=True)
