from pytest import fixture

import mcpacker.model.core.season as season


# Fixtures #########################################################################################

@fixture(name="notSummer")
def createNotSummerList():
    yield season.exclude(season.SUMMER)


# Tests ############################################################################################

def test_exclude(notSummer):
    assert ", ".join([str(s) for s in notSummer]) == "spring, autumn, winter"
