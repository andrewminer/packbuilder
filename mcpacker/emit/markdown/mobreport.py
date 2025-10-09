from mcpacker.emit.markdown.report          import Report
from mcpacker.model.core.ecology.biometrait import BiomeTrait
from mcpacker.model.modpack                 import ModPack


# Class ############################################################################################

class MobReport(Report):

    def __init__(self, pack:ModPack):
        super().__init__("mobs.md", pack)

    def build(self):
        for placement in self.pack.world.mobs:
            self.line(f"# Mob: {placement.gameId}")
            self.line()

            self.indent()
            for index, habitat in enumerate(placement.habitats, start=1):
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
                    category = type(trait[0]).__name__
                    self.text("* ").text(category).text(": not: ").line(trait.name)

                self.outdent()

                self.text("* seasons: ").line(", ".join([s.name for s in habitat.seasons]))
                self.text("* group: ").line(habitat.group.name)
                self.text("* location: ").line(habitat.location.name)
                self.text("* scarcity: ").line(habitat.scarcity.name)
                self.outdent()

            self.outdent()
            self.line()
