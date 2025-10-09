from collections.abc import Iterable
from mcpacker.json import JsonBlob

import mcpacker.json as json


# Class ############################################################################################

class ExtraCondition:

    def __init__(
        self,
        autumn:bool|None=None,
        biome:Iterable[str]|None=None,
        cave:bool|None=None,
        seeSky:bool|None=None,
        spring:bool|None=None,
        summer:bool|None=None,
        timeMax:int|None=None,
        timeMin:int|None=None,
        winter:bool|None=None,
    ):
        self.autumn  = autumn
        self.biome   = biome
        self.cave    = cave
        self.seeSky  = seeSky
        self.spring  = spring
        self.summer  = summer
        self.timeMax = timeMax
        self.timeMin = timeMin
        self.winter  = winter

    def asJsonBlob(self) -> JsonBlob:
        return json.removeNoneValues({
            "autumn": self.autumn,
            "biome": None if not self.biome else "[" + ", ".join(self.biome) + "]",
            "cave": self.cave,
            "seesky": self.seeSky,
            "spring": self.spring,
            "summer": self.summer,
            "maxtime": self.timeMax,
            "mintime": self.timeMin,
            "winter": self.winter,
        })
