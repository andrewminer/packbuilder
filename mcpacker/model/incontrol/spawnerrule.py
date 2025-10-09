from mcpacker.json                      import JsonBlob
from mcpacker.model.core.fauna.mobspawn import MobSpawn
from mcpacker.model.incontrol.condition import Condition


# Class ############################################################################################

class SpawnerRule:

    def __init__(
        self,
        mobGameId:str,
        condition:Condition,
        amountMin:int=1,
        amountMax:int=1,
        rate:float=1.0,
        attempts:int=1,
        weight:int=1,
    ):
        self.mobGameId = mobGameId
        self.amountMin = amountMin
        self.amountMax = amountMax
        self.rate      = rate
        self.attempts  = attempts
        self.weight    = weight
        self.condition = condition

    def asJsonBlob(self) -> JsonBlob:
        return {
            "mob": [self.mobGameId],
            "amount": {
                "minimum": self.amountMin,
                "maximum": self.amountMax,
                "groupdistance": 4,
            },
            "persecond": self.rate,
            "attempts": self.attempts,
            "weights": [self.weight],
            "conditions": self.condition.asJsonBlob(),
        }

