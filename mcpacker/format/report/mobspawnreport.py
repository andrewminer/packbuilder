from mcpacker.format.report.composer import ReportComposer
from mcpacker.model.core.ecology.biometrait import BiomeTrait
from mcpacker.model.modpack import ModPack
from pathlib import Path


# Class ############################################################################################

class MobSpawnReport(ReportComposer):

    def doCompose(self):
        for spawn in self.pack.world.mobSpawns:
            self.line(f"# Mob: {spawn.gameId}")
            self.line()

            self.indent()
            for index, habitat in enumerate(spawn.habitats, start=1):
                self.text("* habitat ").line(index)
                self.indent()
                self.text("* altitude: ").line(habitat.altitude)
                self.line("* biomeFilter:")

                self.indent()
                for trait in habitat.biomeFilter.required:
                    if isinstance(trait, BiomeTrait):
                        self.text("* ").line(trait)
                    else:
                        category = type(trait[0]).__name__
                        self.text("* ").\
                            text(category).\
                            text(": any of: ").\
                            line(", ".join([t.name for t in trait]))

                for trait in habitat.biomeFilter.prohibited:
                    category = type(trait).__name__
                    self.text("* ").text(category).text(": not: ").line(trait.name)

                self.outdent()

                self.text("* seasons: ").line(", ".join([s.name for s in habitat.seasons]))
                self.text("* group: ").line(habitat.group.name)
                self.text("* location: ").line(habitat.location.name)
                self.text("* scarcity: ").line(habitat.scarcity.name)
                self.outdent()

            self.outdent()
            self.line()
