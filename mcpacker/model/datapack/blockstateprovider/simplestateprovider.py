from mcpacker.model.datapack.blockstate import BlockState
from mcpacker.model.datapack.blockstateprovider import BlockStateProvider
from typing import Any


# Class ############################################################################################

class SimpleStateProvider(BlockStateProvider):

    def __init__(self, state:BlockState):
        super().__init__("minecraft:simple_state_provider")
        self.state = state

    def asData(self) -> dict[str, Any]:
        return {
            "type": self.gameId,
            "state": self.state.asData(),
        }
