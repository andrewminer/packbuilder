from pytest import fixture

import mcpacker.model.core.ecology.heat as heat


# Tests ############################################################################################

def test_within():
    assert (
        heat.within(heat.SUBTROPICAL, heat.BOREAL)
        ==
        [heat.SUBTROPICAL, heat.TEMPERATE, heat.BOREAL]
    )
