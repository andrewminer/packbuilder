from mcpacker.model.modpack import ModPack
from mcpacker.write.writer import Writer
from pathlib import Path

import mcpacker.json as json


# Class ############################################################################################

class MetaWriter(Writer):

    def __init__(self, pack:ModPack, outputDir:Path):
        super().__init__(pack, outputDir)

    def doWrite(self):
        path = self.locator.dataPack() / "pack.mcmeta"
        self.resetOutputFile(path)

        with path.open("w") as file:
            file.write(json.dumps({
                "pack": {
                    "pack_format": 48,
                    "description": f"auto-generated overrides for {self.pack.name}"
                }
            }, indent="    "))
