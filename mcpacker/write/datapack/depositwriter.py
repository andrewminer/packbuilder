from mcpacker.format.datapack.structure import Structure
from mcpacker.model.geology.deposit import Deposit
from mcpacker.model.resourceid import ResourceId
from mcpacker.write.writer import Writer

import mcpacker.json as json


# Class ############################################################################################

class DepositWriter(Writer):

    def doWrite(self):
        self._writeDepositMarkerStructures()

    # Private Methods ##########################################################

    def _writeDepositMarkerStructures(self):
        biomes = self.pack.world.biomes

        for deposit in self.pack.world.deposits:
            biomeNames = [b.gameId for b in biomes.filter(lambda b: deposit.acceptsBiome(b))]
            resourceId = ResourceId.parse(f"{self.pack.name}:{deposit.name}")
            structure = Structure(resourceId, biomeNames)
            path = self.locator.structures() / f"{deposit.name}_marker.json"
            self.resetOutputFile(path)
            path.write_text(json.dumps(structure.asJsonBlob(), indent=json.INDENT))
