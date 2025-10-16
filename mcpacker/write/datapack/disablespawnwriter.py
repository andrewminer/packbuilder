from mcpacker.format.datapack.biomemodifier.removespawn import RemoveSpawnBiomeModifier
from mcpacker.write.writer import Writer

import mcpacker.json as json


# Class ############################################################################################

class DisableSpawnWriter(Writer):
    """
    Writes files to disable vanilla spawns for mobs who are to be spawned using custom rules.
    """

    def doWrite(self):
        entityTypes = [m.gameId for m in self.pack.world.mobs]
        modifier = RemoveSpawnBiomeModifier("#c:is_overworld", entityTypes)
        path = self.locator.biomeModifiers() / "remove_managed_mob_spawns.json"
        self.resetOutputFile(path)
        path.write_text(json.dumps(modifier.asJsonBlob(), indent=json.INDENT))
