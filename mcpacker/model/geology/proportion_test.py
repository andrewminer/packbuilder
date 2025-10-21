from pytest import fixture

import mcpacker.model.geology.proportion as proportion


# Tests ############################################################################################

def test_str():
    assert str(proportion.LENS) == "lens (0.4)"

def test_repr():
    assert repr(proportion.LENS) == "Proportion(name='lens', ratio=0.4)"
