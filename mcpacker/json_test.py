from mcpacker.json import JsonBlob
from pytest        import fixture
from typing        import cast

import mcpacker.json as json


# Fixtures #########################################################################################

@fixture(name="blob")
def createBlob():
    yield {
        "alpha": "a",
        "bravo": 12,
        "charlie": True,
        "delta": [
            "foxtrot",
            13,
            False,
            [ "golf" ],
            { "hotel": "india" },
            None,
        ],
        "juliette": {
            "kilo": "lima",
            "mike": {},
            "november": None
        },
        "oscar": None,
        "papa": [],
    }

@fixture(name="noNone")
def removeNoneValues(blob:JsonBlob):
    yield json.removeNoneValues(blob)

@fixture(name="noEmpty")
def remmoveEmptyObjects(blob:JsonBlob):
    yield json.removeEmptyObjects(blob)


# Tests ############################################################################################

def test_removeNoneValues(noNone:JsonBlob):
    assert len(cast(dict[str,list[str]], noNone)["delta"]) == 5
    assert "november" not in cast(dict[str,dict[str,JsonBlob]], noNone)["juliette"]
    assert "oscar" not in cast(dict[str,JsonBlob], noNone)

def test_removeEmptyObjects(noEmpty:JsonBlob):
    assert "mike" not in cast(dict[str,dict[str,JsonBlob]], noEmpty)["juliette"]
    assert "papa" in cast(dict[str,JsonBlob], noEmpty)
