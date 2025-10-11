from mcpacker.model.modpack import ModPack
from pathlib import Path
from typing import Protocol
from typing import TypeVar
from typing import TypeAlias


# Class ############################################################################################

class Locator:
    """
    Locator identifies various important paths within a modpack.

    It currently has added support for the following mods:

      * Cold Sweat
      * InControl!
      * InfoDump
      * KubeJS
      * Large Ore Deposits
      * Thirst Was Taken
    """

    def __init__(self, pack:ModPack, outputDir:Path):
        self._pack = pack
        self._outputDir = outputDir

    def biomeModifiers(self, modName:str|None=None, dataPackName:str|None=None) -> Path:
        return self.dataPackMod(modName, dataPackName) / "neoforge" / "biome_modifier"

    def blockStates(self, modName:str|None=None, resourcePackName:str|None=None) -> Path:
        return self.resourcePackMod(modName, resourcePackName) / "blockstates"

    def config(self) -> Path:
        return self.root() / "config"

    def configuredFeatures(self, modName:str|None=None, dataPackName:str|None=None) -> Path:
        return self.dataPackMod(modName, dataPackName) / "worldgen" / "configured_feature"

    def dataPack(self, dataPackName:str|None=None):
        return self.dataPacks() / (dataPackName or f"{self._pack.name}_override")

    def dataPackMod(self, modName:str|None=None, dataPackName:str|None=None):
        return self.dataPack(dataPackName) / "data" / (modName or self._pack.name)

    def dataPacks(self) -> Path:
        return self.root() / "datapacks"

    def functions(self, modName:str|None=None, dataPackName:str|None=None) -> Path:
        return self.dataPackMod(modName, dataPackName) / "functions"

    def lootModifiers(self, modName:str|None=None, dataPackName:str|None=None) -> Path:
        return self.dataPackMod(modName, dataPackName) / "loot_modifiers"

    def lootTables(self, modName:str|None=None, dataPackName:str|None=None) -> Path:
        return self.dataPackMod(modName, dataPackName) / "loot_tables"

    def models(self, modName:str|None=None, resourcePackName:str|None=None) -> Path:
        return self.resourcePackMod(modName, resourcePackName) / "models"

    def placedFeatures(self, modName:str|None=None, dataPackName:str|None=None) -> Path:
        return self.dataPackMod(modName, dataPackName) / "worldgen" / "placed_feature"

    def recipes(self, modName:str|None=None, dataPackName:str|None=None) -> Path:
        return self.dataPackMod(modName, dataPackName) / "recipes"

    def resourcePack(self, resourcePackName:str|None=None) -> Path:
        return self.resourcePacks() / (resourcePackName or f"{self._pack.name}_override")

    def resourcePackMod(self, modName:str|None=None, resourcePackName:str|None=None) -> Path:
        return self.resourcePack(resourcePackName) / "assets" / (modName or self._pack.name)

    def resourcePacks(self) -> Path:
        return self.root() / "resourcepacks"

    def root(self) -> Path:
        return self._outputDir / self._pack.name

    def structures(self, modName:str|None=None, dataPackName:str|None=None) -> Path:
        return self.dataPackMod(modName, dataPackName) / "structure"

    def structureSets(self, modName:str|None=None, dataPackName:str|None=None) -> Path:
        return self.dataPackMod(modName, dataPackName) / "structure_set"

    def tags(self, modName:str|None=None, dataPackName:str|None=None) -> Path:
        return self.dataPackMod(modName, dataPackName) / "tags"

    def templatePools(self, modName:str|None=None, dataPackName:str|None=None) -> Path:
        return self.dataPackMod(modName, dataPackName) / "template_pool"

    # ColdSweat Mixins #########################################################

    def cos_config(self) -> Path:
        return self.config() / "coldsweat"

    # InControl Mixins #########################################################

    def inc_config(self) -> Path:
        return self.config() / "incontrol"

    # InfoDump Mixins ##########################################################

    def ifd_root(self) -> Path:
        return self.root() / "infodump"

    # KubeJS Mixins ############################################################

    def kbj_root(self) -> Path:
        return self.root() / "kubejs"

    def kbj_clientScripts(self) -> Path:
        return self.kbj_root() / "client_scripts"

    def kbj_serverScripts(self) -> Path:
        return self.kbj_root() / "server_scripts"

    def kbj_startupScripts(self) -> Path:
        return self.kbj_root() / "startup_scripts"

    # Large Ore Deposits Mixins ################################################

    def lod_config(self) -> Path:
        return self.config() / "adlods"

    def lod_deposits(self) -> Path:
        return self.lod_config() / "Deposits"

    def lod_geodes(self) -> Path:
        return self.lod_config() / "Geodes"

    def lod_vanilla(self) -> Path:
        return self.lod_config() / "Vanilla"

    # ThirstWasTaken ###########################################################

    def twt_config(self) -> Path:
        return self.config() / "thirst"
