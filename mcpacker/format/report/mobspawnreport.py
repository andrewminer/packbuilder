from mcpacker.format.report.composer import ReportComposer
from mcpacker.model.ecology.biometrait import BiomeTrait
from mcpacker.model.modpack import ModPack
from pathlib import Path


# Class ############################################################################################

class MobSpawnReport(ReportComposer):

    def doCompose(self):
        for mob in self.pack.world.mobs:
            self.line(f"Mob: {mob.name}")
            self.indent()

            needsDelimiter = False
            for spawn in self.pack.world.mobSpawns:
                if spawn.mob != mob: continue
                habitat = spawn.habitat
                ecotype = spawn.ecotype

                self.line().text("Spawn: ").line(spawn.name)
                self.indent()
                self.text("altitude: ").line(habitat.altitude)
                self.text("biomeFilter: ")
                self.line(" -OR- ".join(str(b) for b in habitat.biomeFilters))
                self.text("seasons: ").line(", ".join([str(s) for s in habitat.seasons]))
                self.line()
                self.text("group: ").line(ecotype.group)
                self.text("location: ").line(ecotype.location)
                self.text("scarcity: ").line(ecotype.scarcity)
                self.outdent()

            self.outdent()
            self.line()
