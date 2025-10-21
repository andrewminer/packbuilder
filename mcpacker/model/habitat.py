from collections.abc import Iterable
from mcpacker.model.altitude import Altitude
from mcpacker.model.ecology.biome import Biome
from mcpacker.model.ecology.biomefilter import BiomeFilter
from mcpacker.model.fauna.group import Group
from mcpacker.model.fauna.location import Location
from mcpacker.model.scarcity import Scarcity
from mcpacker.model.season import Season

import mcpacker.model.altitude as A
import mcpacker.model.fauna.group as G
import mcpacker.model.fauna.location as L
import mcpacker.model.scarcity as C
import mcpacker.model.season as E


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

    def accepts(self, biome:Biome) -> bool:
        return self.biomeFilter.accepts(biome)

    def collect(self) -> "Iterable[Habitat]":
        stack:list[Habitat] = []
        current:Habitat|None = self
        while current:
            stack.append(current)
            current = current._source

        while stack:
            yield stack.pop()

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
