from pytest import fixture

import tungston.core.altitude as A


# Fixtures #########################################################################################

@fixture(name="merged")
def mergeRange():
    yield A.span(A.UPLANDS, A.LOWLANDS)


# Tests ############################################################################################

def test_span(merged):
    assert merged.name == "lowlands-uplands"
    assert merged.bottom == A.LOWLANDS.bottom
    assert merged.top == A.UPLANDS.top
