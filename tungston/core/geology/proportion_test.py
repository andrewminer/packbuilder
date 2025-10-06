from pytest import fixture

import tungston.core.geology.proportion as proportion


# Tests ############################################################################################

def test_str():
    assert str(proportion.LENS) == "lens"

def test_repr():
    assert repr(proportion.LENS) == "Proportion<lens>{ratio: 0.4}"
