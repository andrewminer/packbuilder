from mcpacker.format.toml.composer import TomlComposer
from mcpacker.format.toml.model import TomlArray
from mcpacker.format.toml.model import TomlArrayEntry
from mcpacker.format.toml.model import TomlComment
from mcpacker.format.toml.model import TomlDocument
from mcpacker.format.toml.model import TomlDocumentEntry
from mcpacker.format.toml.model import TomlMap
from mcpacker.format.toml.model import TomlMapEntry
from mcpacker.format.toml.model import TomlPair
from mcpacker.format.toml.model import TomlScalar
from mcpacker.format.toml.model import TomlScalarValue
from mcpacker.format.toml.model import TomlTable
from mcpacker.format.toml.model import TomlTableEntry
from mcpacker.format.toml.model import TomlTablePath
from mcpacker.format.toml.model import TomlValue
from pytest import fixture

import textwrap


# Fixtures #########################################################################################

@fixture(name="composer")
def createComposer():
    yield TomlComposer(TomlDocument([
        TomlTable(TomlTablePath(['alpha', 'foxtrot']), [
            TomlPair('bravo', TomlScalar('cha\"rlie')),
            TomlComment('comment'),
            TomlPair('delta', TomlScalar(12.123)),
            TomlPair('echo', TomlArray([
                TomlScalar(1.0),
                TomlScalar(2.0),
                TomlScalar(3.0)
            ]))
        ]),
        TomlTable(TomlTablePath(['golf hotel']), [
            TomlPair('india', TomlMap([
                TomlPair('juliette', TomlScalar(False))
            ]))
        ])
    ])).compose()


# Tests ############################################################################################

def test_document(composer):
    assert str(composer) == textwrap.dedent("""
        [alpha.foxtrot]
        bravo = "cha\\"rlie"
        # comment
        delta = 12.123
        echo = [
            1.000,
            2.000,
            3.000
        ]

        [golf hotel]
        india = {juliette = false}
    """).lstrip()
