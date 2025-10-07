from mcpacker.model.datapack.placement import Placement
from typing import Any

# Class ############################################################################################

class InSquare(Placement):

    def __init__(self):
        super().__init__("minecraft:in_square")

    def asData(self) -> dict[str,Any]:
        return { "type": self.gameId }

