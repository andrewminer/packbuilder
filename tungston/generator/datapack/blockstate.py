from typing import Any


# Class ############################################################################################

class BlockState:

    def __init__(self, blockId:str, properties:dict[str,str]=None):
        self.blockId = blockId
        self.properties = properties

    def asData(self) -> dict[str,Any]:
        result = { "Name": self.blockId }

        if self.properties:
            result["Properties"] = self.properties

        return result
