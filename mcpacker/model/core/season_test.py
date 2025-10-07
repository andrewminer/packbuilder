from pytest import fixture

import mcpacker.model.core.season as season


# Fixtures #########################################################################################

@fixture(name="notSummer")
def createNotSummerList():
    yield season.excluding(season.SUMMER)


# Tests ############################################################################################

def test_excluding(notSummer):
    assert ", ".join([str(s) for s in notSummer]) == "spring, autumn, winter"
