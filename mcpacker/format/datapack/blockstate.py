from mcpacker.json import JsonBlob
from typing import Any
from typing import cast


# Class ############################################################################################

class BlockState:

    def __init__(self, blockId:str, properties:JsonBlob|None=None):
        self.blockId = blockId
        self.properties = properties

    def asJsonBlob(self) -> JsonBlob:
        result = cast(dict[str,JsonBlob], { "Name": self.blockId })

        if self.properties:
            result["Properties"] = self.properties

        return result
