from mcpacker.format.datapack.biomemodifier.addfeature import AddFeatureBiomeModifier
from mcpacker.format.datapack.configuredfeature.crop import CropConfiguredFeature
from mcpacker.format.datapack.configuredfeature.patch import PatchConfiguredFeature
from mcpacker.format.datapack.configuredfeature.tree import TreeConfiguredFeature
from mcpacker.format.datapack.placedfeature.crop import CropPlacedFeature
from mcpacker.format.datapack.placedfeature.patch import PatchPlacedFeature
from mcpacker.write.writer import Writer
from mcpacker.model.flora.patch import Patch
from mcpacker.model.flora.tree import Tree
from mcpacker.model.modpack import ModPack
from mcpacker.write.json import dumps
from pathlib import Path

import mcpacker.model.altitude as AL
import mcpacker.format.datapack.generationstep as GE


# Class ############################################################################################

class PlantWriter(Writer):

    def __init__(self, pack:ModPack, outputDir:Path):
        super().__init__(pack, outputDir)

    def doWrite(self):
        self._writeBiomeModifiers()
        self._writeCropConfiguredFeatures()
        self._writeCropPlacedFeatures()
        self._writePatchConfiguredFeatures()
        self._writePatchPlacedFeatures()
        self._writeTreeConfiguredFeatures()
        self._writeTreePlacedFeatures()

    # Private Methods ##########################################################

    def _writeBiomeModifiers(self):
        modName = self.pack.name

        for biome in self.pack.world.biomes:
            features:list[str] = []
            for spawn in self.pack.world.plantSpawns:
                if not spawn.habitat.accepts(biome): continue

                kind = None
                if isinstance(spawn.plant, Patch):
                    kind = "patch"
                if isinstance(spawn.plant, Tree):
                    kind = "tree"

                if not kind: continue

                features.append(f"{self.pack.name}:{kind}/{spawn.plant.name}")

            modifier = AddFeatureBiomeModifier(str(biome.gameId), features, GE.STRONGHOLDS)
            path = self.locator.biomeModifiers() / f"add_{biome.gameId.name!s}_plants.json"
            self.resetOutputFile(path)
            path.write_text(dumps(modifier.asJsobBlob()))

    def _writeCropConfiguredFeatures(self):
        for spawn in self.pack.world.plantSpawns:
            if not isinstance(spawn.plant, Patch): continue

            feature = CropConfiguredFeature(spawn.plant)
            path = self.locator.configuredFeatures() / "crop" / f"{spawn.name}.json"
            self.resetOutputFile(path)
            path.write_text(dumps(feature.asJsonBlob()))

    def _writeCropPlacedFeatures(self):
        for spawn in self.pack.world.plantSpawns:
            if not isinstance(spawn.plant, Patch): continue

            feature = CropPlacedFeature(self.pack, spawn)
            path = self.locator.placedFeatures() / "crop" / f"{spawn.name}.json"
            self.resetOutputFile(path)
            path.write_text(dumps(feature.asJsonBlob()))

    def _writePatchConfiguredFeatures(self):
        for spawn in self.pack.world.plantSpawns:
            if not isinstance(spawn.plant, Patch): continue

            feature = PatchConfiguredFeature(self.pack, spawn.plant)
            path = self.locator.configuredFeatures() / "patch" / f"{spawn!s}.json"
            self.resetOutputFile(path)
            path.write_text(dumps(feature.asJsonBlob()))

    def _writePatchPlacedFeatures(self):
        for spawn in self.pack.world.plantSpawns:
            if not isinstance(spawn.plant, Patch): continue

            for altitude in AL.ALL:
                band = AL.intersect(altitude, spawn.habitat.altitude)
                if not band: continue

                feature = PatchPlacedFeature(self.pack, spawn, altitude)
                path = self.locator.placedFeatures() / "patch" / f"{spawn!s}_{band.name!s}.json"
                self.resetOutputFile(path)
                path.write_text(dumps(feature.asJsonBlob()))

    def _writeTreeConfiguredFeatures(self):
        for spawn in self.pack.world.plantSpawns:
            if not isinstance(spawn.plant, Tree): continue

            feature = TreeConfiguredFeature(spawn.plant)
            path = self.locator.configuredFeatures() / "tree" / f"{spawn!s}.json"
            self.resetOutputFile(path)
            path.write_text(dumps(feature.asJsonBlob()))

    def _writeTreePlacedFeatures(self):
        for spawn in self.pack.world.plantSpawns:
            if not isinstance(spawn.plant, Tree): continue

            for altitude in AL.ALL:
                band = AL.intersect(altitude, spawn.habitat.altitude)
                if not band: continue

                feature = PatchPlacedFeature(self.pack, spawn, altitude)
                path = self.locator.placedFeatures() / "tree" / f"{spawn!s}_{band.name!s}.json"
                self.resetOutputFile(path)
                path.write_text(dumps(feature.asJsonBlob()))
