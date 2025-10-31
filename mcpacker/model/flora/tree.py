from mcpacker.model.flora.canopyshape import CanopyShape
from mcpacker.model.flora.trunkshape import TrunkShape
from mcpacker.model.resourceid import ResourceId
from mcpacker.model.flora.plant import Plant

import mcpacker.model.flora.canopyshape as CA
import mcpacker.model.flora.trunkshape as TR


# Class ############################################################################################

class Tree(Plant):

    def __init__(
        self,
        name:str,
        foliage:ResourceId|str,
        log:ResourceId|str,
        trunkShape:TrunkShape=TR.STRAIGHT,
        trunkHeightMin:int=3,
        trunkHeightMax:int=5,
        canopyShape:CanopyShape=CA.BLOB,
        canopyHeight:int=3,
        canopyRadius:int=2,
    ):
        super().__init__(name)

        self.foliage = ResourceId.parse(foliage)
        self.log = log
        self.trunkShape = trunkShape
        self.trunkHeightMin = trunkHeightMin
        self.trunkHeightMax = trunkHeightMax
        self.canopyShape = canopyShape
        self.canopyHeight = canopyHeight
        self.canopyRadius = canopyRadius

    def __repr__(self) -> str:
        return "".join([
            "Tree(",
                "name=", repr(self.name), ", ",
                "foliage=", repr(self.foliage), ", ",
                "log=", repr(self.log), ", ",
                "trunkShape=", repr(self.trunkShape), ", ",
                "trunkHeightMin=", repr(self.trunkHeightMin), ", ",
                "trunkHeightMax=", repr(self.trunkHeightMax), ", ",
                "canopyShape=", repr(self.canopyShape), ", ",
                "canopyHeight=", repr(self.canopyHeight), ", ",
                "canopyRadius=", repr(self.canopyRadius),
            ")"
        ])
