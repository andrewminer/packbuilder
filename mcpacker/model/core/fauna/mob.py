from collections.abc import Iterable
from mcpacker.model.core.fauna.active import Active

import mcpacker.model.core.fauna.active as AC


# Class ############################################################################################

class Mob:
    """
    A creature which may appear in the game world.
    """

    def __init__(self, gameId:str, active:Active|Iterable[Active]=AC.DIURNAL):
        if isinstance(active, Active):
            active = [active]

        self.gameId = gameId
        self.active = active

    def __eq__(self, other) -> bool:
        if type(self) != type(other): return False
        if self.gameId != other.gameId: return False
        return True

    def __hash__(self) -> int:
        return hash(self.gameId)

    def __str__(self) -> str:
        return self.gameId

    def __repr__(self) -> str:
        return f"Mob<{self.gameId}>{{active:{self.active}}}"
