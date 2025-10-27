from mcpacker.write.packmetawriter import PackMetaWriter
from pathlib import Path


# Class ############################################################################################

class DataPackMetaWriter(PackMetaWriter):
    """
    Writes the meta.mcinfo for the datapack as a whole.
    """

    @property
    def packRoot(self) -> Path:
        return self.locator.dataPack()
