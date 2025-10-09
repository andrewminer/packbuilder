from mcpacker.model.catalog import Catalog
from pytest import fixture
from typing import Any


# Helpers ##########################################################################################

class SampleItem:

    def __init__(self, gameId:str):
        self.gameId = gameId

    def __eq__(self, other:Any):
        return self.gameId == other.gameId

    def __repr__(self) -> str:
        return self.gameId


# Fixtures #########################################################################################

@fixture(name="empty")
def buildEmptyCatalog():
    yield Catalog()

@fixture(name="full")
def buildFullCatalog():
    yield Catalog([
        SampleItem("alpha"),
        SampleItem("bravo"),
        SampleItem("charlie"),
        SampleItem("delta"),
    ])

@fixture(name="almostFull")
def buildAlmostFullCatalog(full):
    del full["bravo"]
    yield full

@fixture(name="almostEmpty")
def buildAlmostEmptyCatalog(empty):
    empty.add(SampleItem("echo"))
    yield empty

@fixture(name="filtered")
def buildFilteredList(full):
    yield list(full.filter(lambda x: x.gameId.endswith("a")))

@fixture(name="mapped")
def buildMappedList(full):
    yield list(full.map(lambda x: x.gameId))


# Tests ############################################################################################

def test_add(almostEmpty):
    assert "echo" in almostEmpty

def test_contains(empty, full):
    assert "bravo" not in empty
    assert "bravo" in full

def test_del(almostFull):
    assert "bravo" not in almostFull

def test_eq():
    assert Catalog([SampleItem("alpha")]) == Catalog([SampleItem("alpha")])
    assert Catalog([SampleItem("alpha")]) != Catalog([SampleItem("bravo")])

def test_filter(filtered):
    assert [a.gameId for a in filtered] == ["alpha", "delta"]

def test_getitem(full):
    assert full["bravo"].gameId == "bravo"

def test_iter(full):
    assert [s.gameId for s in full] == ["alpha", "bravo", "charlie", "delta"]

def test_len(empty, full):
    assert len(empty) == 0
    assert len(full) == 4

def test_map(mapped):
    assert mapped == ["alpha", "bravo", "charlie", "delta"]

def test_repr(empty, full):
    assert repr(empty) == "Catalog[]"
    assert repr(full) == "Catalog[alpha, bravo, charlie, delta]"
