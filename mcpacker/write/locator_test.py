from mcpacker.write.locator import Locator
from mcpacker.model.modpack import ModPack
from pathlib import Path
from pytest import fixture


# Fixtures #########################################################################################

@fixture(name="locator")
def createLocator():
    return Locator(ModPack("testPack"), Path("output"))


# Tests ############################################################################################

def test_blockStates(locator:Locator):
    assert (
        locator.blockStates() ==
        Path(
            "output/testPack/resourcepacks/testPack_override/" +
            "assets/testPack/blockstates"
        )
    )

def test_configuredFeatures(locator:Locator):
    assert (
        locator.configuredFeatures() ==
        Path(
            "output/testPack/datapacks/testPack_override/" +
            "data/testPack/worldgen/configured_feature"
        )
    )

def test_configuredFeaturesSpecificDataPack(locator:Locator):
    assert (
        locator.configuredFeatures(dataPackName="alternate") ==
        Path(
            "output/testPack/datapacks/alternate/" +
            "data/testPack/worldgen/configured_feature"
        )
    )

def test_configuredFeaturesSpecificMod(locator:Locator):
    assert (
        locator.configuredFeatures("farmersdelight") ==
        Path(
            "output/testPack/datapacks/testPack_override/" +
            "data/farmersdelight/worldgen/configured_feature"
        )
    )

def test_kbj_serverScripts(locator:Locator):
    assert locator.kbj_serverScripts() == Path("output/testPack/kubejs/server_scripts")

def test_root(locator:Locator):
    assert locator.root() == Path("output/testPack")
