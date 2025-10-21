from mcpacker.json import JsonBlob
from mcpacker.format.datapack.blockstate import BlockState
from mcpacker.format.datapack.blockstateprovider import BlockStateProvider
from typing import Any


# Class ############################################################################################

class SimpleStateProvider(BlockStateProvider):

    def __init__(self, state:BlockState):
        super().__init__("minecraft:simple_state_provider")
        self.state = state

    def asJsonBlob(self) -> JsonBlob:
        return {
            "type": self.gameId,
            "state": self.state.asJsonBlob(),
        }
