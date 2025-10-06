from tungston.core.altitude import Altitude
from tungston.core.ecology.biomefilter import BiomeFilter
from tungston.core.fauna.group import Group
from tungston.core.fauna.location import Location
from tungston.core.scarcity import Scarcity
from tungston.core.season import Season

import tungston.core.altitude as A
import tungston.core.fauna.group as G
import tungston.core.fauna.location as L
import tungston.core.scarcity as C
import tungston.core.season as E


# Class ############################################################################################

class Habitat:
    """
    A description of where and when various features may be present.
    """

    def __init__(
        self,

        altitudes:tuple[Altitude]|Altitude=[A.ANYWHERE],
        biomeFilter:BiomeFilter=None,
        seasons:tuple[Season]=E.ALL,

        group:Group=G.SOLO,
        location:Location=L.OUTSIDE,
        scarcity:Scarcity=C.SPARSE,
    ):
        self.altitudes = (altitudes,) if isinstance(altitudes, Altitude) else altitudes
        self.biomeFilter = biomeFilter or BiomeFilter()
        self.seasons = (seasons,) if isinstance(seasons, Season) else seasons

        self.group = group
        self.location = location
        self.scarcity = scarcity

        self._source = None

    def __str__(self) -> str:
        return "".join(str(p) for p in [
            self.altitude, "|",
            self.biomeFilter, "|",
            self.seasons, "|",
            self.group, "|",
            self.location, "|",
            self.scarcity
        ])

    def __repr__(self) -> str:
        return "".join([str(p) for p in [
            "Habitat{",
                "altitude: [", ", ".join([repr(a) for a in self.altitudes]), "], ",
                "biomeFilter: ", repr(self.biomeFilter), ", ",
                "seasons: [", ", ".join([repr(s) for s in self.seasons]), "], ",
                "group: ", repr(self.group), ", ",
                "location: ", repr(self.location), ", ",
                "scarcity: ", repr(self.scarcity),
            "}"
        ]])

    def derive(self, **kwargs):
        kwargs = {
            "altitudes": self.altitudes,
            "biomeFilter": self.biomeFilter,
            "seasons": self.seasons,
            "group": self.group,
            "location": self.location,
            "scarcity": self.scarcity
        } | kwargs

        result = Habitat(**kwargs)
        result._source = self

        return result

    def collect(self) -> "tuple[Habitat]":
        result = []

        current = self
        while current:
            result.append(current)
            current = current._source

        return tuple(reversed(result))

