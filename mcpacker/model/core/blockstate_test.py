from pytest import fixture
from mcpacker.model.core.blockstate import BlockState
from mcpacker.model.core.resourceid import ResourceId


# Fixtures #########################################################################################

@fixture(name="block")
def createBlockState():
    yield BlockState("oak_fence", { "waterlogged": "true" })


# Tests ############################################################################################

def test_repr(block):
    assert repr(block) == (
        "BlockState(" +
            "gameId=ResourceId(isTag=False, mod='minecraft', name='oak_fence'), " +
            "properties={'waterlogged': 'true'}" +
        ")"
    )
