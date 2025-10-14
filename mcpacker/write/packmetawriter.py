from mcpacker.model.modpack import ModPack
from mcpacker.write.writer import Writer
from pathlib import Path

import mcpacker.json as json


# Class ############################################################################################

class PackMetaWriter(Writer):

    def __init__(self, pack:ModPack, outputDir:Path, formatVersion:int):
        super().__init__(pack, outputDir)
        self.formatVersion = formatVersion

    @property
    def packRoot(self) -> Path:
        raise NotImplementedError()

    def doWrite(self):
        path = self.packRoot / "pack.mcmeta"
        self.resetOutputFile(path)

        with path.open("w") as file:
            file.write(json.dumps({
                "pack": {
                    "pack_format": self.formatVersion,
                    "description": f"auto-generated overrides for {self.pack.name}"
                }
            }, indent="    "))
