from collections.abc                         import Iterable
from mcpacker.model.core.altitude            import Altitude
from mcpacker.model.core.ecology.biomefilter import BiomeFilter
from mcpacker.model.core.fauna.group         import Group
from mcpacker.model.core.fauna.location      import Location
from mcpacker.model.core.scarcity            import Scarcity
from mcpacker.model.core.season              import Season

import mcpacker.model.core.altitude       as A
import mcpacker.model.core.fauna.group    as G
import mcpacker.model.core.fauna.location as L
import mcpacker.model.core.scarcity       as C
import mcpacker.model.core.season         as E


# Class ############################################################################################

class Habitat:
    """
    A description of where and when various features may be present.
    """

    def __init__(
        self,

        altitude:Altitude=A.ANYWHERE,
        biomeFilter:BiomeFilter|None=None,
        seasons:Iterable[Season]|Season=E.ALL,

        group:Group=G.SOLO,
        location:Location=L.OUTSIDE,
        scarcity:Scarcity=C.SPARSE,
    ):
        self.altitude = altitude
        self.biomeFilter = biomeFilter or BiomeFilter()
        self.seasons = [seasons] if isinstance(seasons, Season) else seasons

        self.group = group
        self.location = location
        self.scarcity = scarcity

        self._source:Habitat|None = None

    def __str__(self) -> str:
        return "".join([str(p) for p in [
            self.altitude, "|",
            self.biomeFilter, "|",
            ", ".join([str(s) for s in self.seasons]), "|",
            self.group, "|",
            self.location, "|",
            self.scarcity
        ]])

    def __repr__(self) -> str:
        return "".join([str(p) for p in [
            "Habitat(",
                "altitude=", repr(self.altitude), ", ",
                "biomeFilter=", repr(self.biomeFilter), ", ",
                "seasons=[", ", ".join([repr(s) for s in self.seasons]), "], ",
                "group=", repr(self.group), ", ",
                "location=", repr(self.location), ", ",
                "scarcity=", repr(self.scarcity),
            ")"
        ]])

    def derive(
        self,
        *,
        altitude:Altitude|None=None,
        biomeFilter:BiomeFilter|None=None,
        seasons:Iterable[Season]|Season|None=None,
        group:Group|None=None,
        location:Location|None=None,
        scarcity:Scarcity|None=None,
    ):
        result = Habitat(
            altitude    or self.altitude,
            biomeFilter or self.biomeFilter,
            seasons     or self.seasons,
            group       or self.group,
            location    or self.location,
            scarcity    or self.scarcity
        )
        result._source = self

        return result

    def collect(self) -> "Iterable[Habitat]":
        stack:list[Habitat] = []
        current:Habitat|None = self
        while current:
            stack.append(current)
            current = current._source

        while stack:
            yield stack.pop()
