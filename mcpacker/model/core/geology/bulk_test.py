from mcpacker.model.core.geology.bulk import Bulk
from pytest import fixture


# Fixture ##########################################################################################

@fixture(name="bulk")
def createBulk():
    return Bulk("chunk", 64, 128)

@fixture(name="scaledBulk")
def scaleBulk(bulk):
    yield bulk.scale(2.0)


# Fixture ##########################################################################################

def test_repr(bulk, scaledBulk):
    assert repr(bulk) == "Bulk<chunk>{smallest: 64, largest: 128}"
    assert repr(scaledBulk) == "Bulk<chunk>{smallest: 128, largest: 256}"
