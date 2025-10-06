from pytest import fixture

import tungston.core.ecology.humidity as humidity


# Tests ############################################################################################

def test_within():
    assert humidity.within(humidity.DAMP, humidity.DRY) == [humidity.DAMP, humidity.DRY]
