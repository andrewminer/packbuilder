from mcpacker.format.textcomposer import TextComposer
from mcpacker.model.modpack import ModPack
from mcpacker.write.textwriter import TextWriter
from pathlib import Path
from pytest import fixture


# Helper Classes ###################################################################################

class SampleComposer(TextComposer):

    def doCompose(self):
        self.line("alpha bravo")
        self.line("charlie")


# Fixtures #########################################################################################

@fixture(name="composer")
def createComposer():
    yield SampleComposer()

@fixture(name="pack")
def createModPack():
    yield ModPack("testModPack")

@fixture(name="writer")
def createWriter(pack:ModPack, tmp_path:Path, composer:TextComposer):
    yield TextWriter(pack, tmp_path, Path("reports")/"test.md", composer).write()


# Tests ############################################################################################

def test_writer(tmp_path:Path, writer:TextWriter):
    path = tmp_path/"testModPack"/"reports"/"test.md"
    assert path.read_text() == "alpha bravo\ncharlie"

