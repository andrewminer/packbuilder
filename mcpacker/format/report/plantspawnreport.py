from mcpacker.model.core.flora.patch import Patch
from mcpacker.model.core.flora.tree import Tree
from mcpacker.format.report.composer import ReportComposer
from mcpacker.model.core.ecology.biometrait import BiomeTrait
from mcpacker.model.modpack import ModPack
from pathlib import Path


# Class ############################################################################################

class PlantSpawnReport(ReportComposer):

    def doCompose(self):
        for spawn in self.pack.world.plantSpawns:
            self.line(f"Plant: {spawn.name}")
            self.indent() # plant

            if isinstance(spawn.plant, Patch):
                patch:Patch = spawn.plant

                self.line().line("Patch Biology:")
                self.indent() # botany
                self.text("blocks: ").line(", ".join(str(b) for b in patch.blocks))
                self.text("immersion: ").line(patch.immersion)
                self.text("radius: ").line(patch.radius)
                self.text("density: ").text(patch.density).line(f" ({patch.attempts()} attempts)")
                self.text("substrates: ").line(", ".join(str(s) for s in patch.substrates))
                self.outdent() # botany

            elif isinstance(spawn.plant, Tree):
                tree:Tree = spawn.plant

                self.line().line("Tree Biology:")
                self.indent() # botany
                self.text("foliage: ").line(tree.foliage)
                self.text("log: ").line(tree.log)
                self.text("trunkShape: ").line(tree.trunkShape)
                self.text("trunkHeightMin: ").line(tree.trunkHeightMin)
                self.text("trunkHeightMax: ").line(tree.trunkHeightMax)
                self.text("canopyShape: ").line(tree.canopyShape)
                self.text("canopyHeight: ").line(tree.canopyHeight)
                self.text("canopyRadius: ").line(tree.canopyRadius)
                self.outdent() # botany

            self.line().line("Habitat:")
            self.indent() # habitat
            self.text("altitude: ").line(spawn.altitude)
            self.text("biomeFilters: ").line(" -OR- ".join(str(f) for f in spawn.biomeFilters))
            self.text("scarcity: ").line(spawn.scarcity)
            self.outdent() # habitat

            self.line().line("Biomes:")
            self.indent() # biomes
            biomes = self.pack.world.biomes.filter(lambda b: spawn.acceptsBiome(b))
            for biome in biomes:
                self.line(biome)
            self.outdent() # biomes

            self.outdent() # plant
            self.line()
