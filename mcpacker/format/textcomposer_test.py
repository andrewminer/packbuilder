from mcpacker.format.textcomposer import TextComposer
from pytest import fixture

import textwrap


# Helper Classes ###################################################################################

class SampleComposer(TextComposer):

    def doCompose(self):
        self.text("alpha").line(" bravo")
        self.indent()
        self.line("charlie")
        self.outdent()
        self.text("delta").line(" echo")

# Fixtures #########################################################################################

@fixture(name="composer")
def composeText():
    yield SampleComposer().compose()

# Tests ############################################################################################

def test_composer(composer:TextComposer):
    assert str(composer) == textwrap.dedent("""
        alpha bravo
            charlie
        delta echo
    """).strip()
