from collections.abc import Iterable
from mcpacker.model.fauna.active import Active
from mcpacker.model.resourceid import ResourceId
from mcpacker.model.spawnable import Spawnable

import mcpacker.model.fauna.active as AC


# Class ############################################################################################

class Mob(Spawnable):
    """
    A creature which may appear in the game world.
    """

    def __init__(self, gameId:ResourceId|str, active:Active|Iterable[Active]=AC.DIURNAL):
        super().__init__(str(gameId))

        if isinstance(active, Active):
            active = [active]

        self.gameId = ResourceId.parse(gameId)
        self.active = active

    def __repr__(self) -> str:
        return f"Mob(gameId={self.gameId!r}, active={self.active!r})"
