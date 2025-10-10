from mcpacker.model.modpack                 import ModPack
from mcpacker.write.markdown.markdownwriter import MarkdownWriter
from pathlib                                import Path
from pytest                                 import fixture

import textwrap


# Helpers ##########################################################################################

class SampleWriter(MarkdownWriter):

    def compose(self):
        (self.text("alpha")
            .line("bravo")
            .indent()
            .line("charlie")
            .indent()
            .line("delta")
            .outdent()
            .line("echo")
        )


# Fixtures #########################################################################################

@fixture(name="writer")
def createWriter(tmp_path:Path):
    writer = SampleWriter("testReport.md", ModPack("testModPack"), tmp_path)
    writer.write()
    yield writer


# Tests ############################################################################################

def test_write(tmp_path, writer):
    path = tmp_path / "testModPack" / "reports" / "testReport.md"
    assert path.read_text() == textwrap.dedent("""
        alphabravo
          charlie
            delta
          echo
    """).lstrip()
