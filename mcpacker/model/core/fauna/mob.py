from mcpacker.model.core.fauna.active import Active

import mcpacker.model.core.fauna.active as AC


# Class ############################################################################################

class Mob:
    """
    A creature which may appear in the game world.
    """

    def __init__(self, name:str, gameId:str, active:tuple[Active]=AC.DIURNAL):
        self.name = name
        self.gameId = gameId
        self.active = active

        if not self.active:
            self.active = AC.DIURNAL

        if isinstance(self.active, Active):
            self.active = (self.active,)

    def __eq__(self, other) -> bool:
        if type(self) != type(other): return False
        if self.gameId != other.gameId: return False
        return True

    def __hash__(self) -> int:
        return hash(self.gameId)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{self.name}<{self.gameId}>{{active:{self.active}}}"
