from mcpacker.json import JsonBlob
from mcpacker.model.core.resourceid import ResourceId
from typing import Any


# Class ############################################################################################

class BlockState:

    @staticmethod
    def parse(value:"BlockState|str") -> "BlockState":
        if isinstance(value, BlockState): return value
        return BlockState(ResourceId.parse(value))

    def __init__(self, gameId:ResourceId|str, properties:JsonBlob=None):
        self.gameId = ResourceId.parse(gameId)
        self.properties = properties

    def __eq__(self, other:Any) -> bool:
        if type(self) != type(other): return False
        if self.gameId != other.gameId: return False
        if self.properties != other.properties: return False
        return True

    def __hash__(self) -> int:
        return hash((self.gameId, self.properties))

    def __repr__(self) -> str:
        return f"BlockState(gameId={self.gameId!r}, properties={self.properties!r})"

    def __str__(self) -> str:
        if not self.properties:
            return str(self.gameId)

        return f"{self.gameId}{self.properties}"
