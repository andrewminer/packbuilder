from mcpacker.json                           import JsonBlob
from mcpacker.model.incontrol.extracondition import ExtraCondition
from mcpacker.model.core.dimension           import Dimension

import mcpacker.json                 as json
import mcpacker.model.core.altitude  as A
import mcpacker.model.core.dimension as D


# Class ############################################################################################

class Condition:

    def __init__(
        self,
        dimension:Dimension=D.OVERWORLD,
        heightMin:int|None=None,
        heightMax:int|None=None,
        thisMax:int|None=None,
        inWater:bool|None=None,
        andCondition:ExtraCondition|None=None,
    ):
        self.dimension    = dimension
        self.heightMin    = heightMin
        self.heightMax    = heightMax
        self.thisMax      = thisMax
        self.inWater      = inWater
        self.andCondition = andCondition

    def asJsonBlob(self) -> JsonBlob:
        return json.removeNoneValues({
            "dimension": self.dimension.name,
            "heightmin": self.heightMin,
            "heightmax": self.heightMax,
            "maxthis":   self.thisMax,
            "inwater":   self.inWater,
            "and":       None if not self.andCondition else self.andCondition.asJsonBlob(),
        })
