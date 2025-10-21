from pytest import fixture

import mcpacker.model.ecology.flora as flora


# Tests ############################################################################################

def test_within():
    assert flora.within(flora.FOREST, flora.FIELD) == [flora.FOREST, flora.CLEARING, flora.FIELD]
