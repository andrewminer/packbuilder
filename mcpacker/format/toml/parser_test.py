from pytest import fixture
from mcpacker.format.toml.parser import TomlParser

import textwrap


# Fixtures #########################################################################################

@fixture(name="basicTomlDocument")
def createBasicTomlDocument():
    return TomlParser(textwrap.dedent("""
        [alpha.foxtrot]
        bravo = "cha\\"rlie"
        # comment
        delta = 12.123
        echo = [
            1, 2, 3
        ]

        ["golf hotel"]
        india = { juliette = false }
    """).strip()).parse()

# Tests ############################################################################################

def test_basicTomlDocument(basicTomlDocument):
    assert repr(basicTomlDocument) == (
        "TomlDocument{entries:[" +
            "TomlTable{path:TomlTablePath{parts:['alpha'.'foxtrot']},entries:[" +
                "TomlPair{key:'bravo',value:TomlScalar{value:'cha\"rlie'}}," +
                "TomlComment{text:'comment'}," +
                "TomlPair{key:'delta',value:TomlScalar{value:12.123}}," +
                "TomlPair{key:'echo',value:TomlArray{entries:[" +
                    "TomlScalar{value:1.0}," +
                    "TomlScalar{value:2.0}," +
                    "TomlScalar{value:3.0}" +
                "]}}" +
            "]}," +
            "TomlTable{path:TomlTablePath{parts:['golf hotel']},entries:[" +
                "TomlPair{key:'india',value:TomlMap{entries:[" +
                    "TomlPair{key:'juliette',value:TomlScalar{value:False}}" +
                "]}}" +
            "]}" +
        "]}"
    )
