from mcpacker.write.packmetawriter import PackMetaWriter
from pathlib import Path


# Class ############################################################################################

class ResourcePackMetaWriter(PackMetaWriter):

    @property
    def packRoot(self) -> Path:
        return self.locator.resourcePack()
