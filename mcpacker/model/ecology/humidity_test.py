from pytest import fixture

import mcpacker.model.ecology.humidity as humidity


# Tests ############################################################################################

def test_within():
    assert humidity.within(humidity.DAMP, humidity.DRY) == [humidity.DAMP, humidity.DRY]
