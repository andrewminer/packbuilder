from mcpacker.write.writer  import Writer
from mcpacker.model.modpack import ModPack
from pathlib                import Path
from pytest                 import fixture


# Helpers ##########################################################################################

class SampleWriter(Writer):

    def write(self):
        path = self.outputDir/self.pack.name/"samplewriter.md"
        self.resetOutputFile(path)
        path.write_text("alpha bravo charlie")


# Fixtures #########################################################################################

@fixture(name="writer")
def createWriter(tmp_path):
    writer = SampleWriter(ModPack("testpack"), tmp_path)
    writer.write()
    yield writer


# Tests ############################################################################################

def test_write(tmp_path:Path, writer:SampleWriter):
    path = tmp_path/"testpack"/"samplewriter.md"
    assert path.read_text() == "alpha bravo charlie"
