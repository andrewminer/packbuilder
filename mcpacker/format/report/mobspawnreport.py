from mcpacker.format.report.composer import ReportComposer
from mcpacker.model.ecology.biometrait import BiomeTrait
from mcpacker.model.modpack import ModPack
from pathlib import Path


# Class ############################################################################################

class MobSpawnReport(ReportComposer):

    def doCompose(self):
        for spawn in self.pack.world.mobSpawns:
            self.line(f"Mob: {spawn.name}")
            self.line()

            self.indent()
            needsDelimiter = False
            for index, habitat in enumerate(spawn.habitats, start=1):
                if needsDelimiter: self.line()
                needsDelimiter = True

                self.text("Habitat ").line(index)
                self.indent()
                self.text("altitude: ").line(habitat.altitude)
                self.text("biomeFilter: ").line(habitat.biomeFilter)
                self.text("seasons: ").line(", ".join([str(s) for s in habitat.seasons]))
                self.text("group: ").line(habitat.group)
                self.text("location: ").line(habitat.location)
                self.text("scarcity: ").line(habitat.scarcity)
                self.outdent()

            self.outdent()
            self.line()
