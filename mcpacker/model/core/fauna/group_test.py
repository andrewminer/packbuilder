from pytest import fixture

import mcpacker.model.core.fauna.group as group


# Fixtures #########################################################################################

@fixture(name="atomicFamily")
def createAtomicFamily():
    yield group.merge(group.PAIR, group.FAMILY)


# Tests ############################################################################################

def test_merge(atomicFamily):
    assert atomicFamily.smallest == 2
    assert atomicFamily.largest == 4
