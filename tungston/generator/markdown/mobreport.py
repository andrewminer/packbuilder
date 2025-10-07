from tungston.core.world import World
from tungston.core.ecology.biometrait import BiomeTrait
from tungston.generator.markdown.report import Report


# Class ############################################################################################

class MobReport(Report):

    def __init__(self, world:World):
        super().__init__("mobs.md", world)

    def build(self):
        for placement in self.world.mobs.all():
            self.line(f"# Mob: {placement.mob.name} <{placement.mob.gameId}>")
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
