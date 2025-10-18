from mcpacker.model.catalog import Catalog
from pytest import fixture
from typing import Any


# Helpers ##########################################################################################

class SampleItem:

    def __init__(self, name:str):
        self.name = name

    def __eq__(self, other:Any):
        return self.name == other.name

    def __repr__(self) -> str:
        return self.name


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
    yield list(full.filter(lambda x: x.name.endswith("a")))

@fixture(name="mapped")
def buildMappedList(full):
    yield list(full.map(lambda x: x.name))


# Tests ############################################################################################

def test_add(almostEmpty):
    assert "echo" in almostEmpty

def test_contains(empty, full):
    assert "bravo" not in empty
    assert "bravo" in full

def test_del(almostFull):
    assert "bravo" not in almostFull

def test_filter(filtered):
    assert [a.name for a in filtered] == ["alpha", "delta"]

def test_getitem(full):
    assert full["bravo"].name == "bravo"

def test_iter(full):
    assert [s.name for s in full] == ["alpha", "bravo", "charlie", "delta"]

def test_len(empty, full):
    assert len(empty) == 0
    assert len(full) == 4

def test_map(mapped):
    assert mapped == ["alpha", "bravo", "charlie", "delta"]

def test_repr(empty, full):
    assert repr(empty) == "Catalog(items={})"
    assert repr(full) == (
        "Catalog(items={'alpha': alpha, 'bravo': bravo, 'charlie': charlie, 'delta': delta})"
    )
