from mcpacker.model.ecology.biometrait import BiomeTrait
from mcpacker.model.ecology.flora import Flora
from mcpacker.model.ecology.geology import Geology
from mcpacker.model.ecology.heat import Heat
from mcpacker.model.ecology.humidity import Humidity
from mcpacker.model.ecology.soil import Soil
from mcpacker.model.ecology.water import Water
from mcpacker.model.resourceid import ResourceId
from typing import Any


####################################################################################################

class Biome:
    """
    A region of the world defined by a unique combination of geology, topography, and ecology.
    """

    def __init__(
        self,
        name:str,
        gameId:ResourceId|str,
        flora:Flora,
        geology:Geology,
        heat:Heat,
        humidity:Humidity,
        soil:Soil,
        water:Water,
    ):
        self.name = name
        self.gameId = ResourceId.parse(gameId)

        self.flora = flora
        self.geology = geology
        self.heat = heat
        self.humidity = humidity
        self.soil = soil
        self.water = water

    def __eq__(self, other:Any) -> bool:
        if type(self) != type(other): return False
        if self.gameId != other.gameId: return False
        if self.name != other.name: return False
        return True

    def __hash__(self) -> int:
        return hash((self.gameId, self.name))

    def __lt__(self, other:Any) -> bool:
        if type(self) != type(other): raise ValueError()
        return self.gameId < other.gameId

    def __str__(self) -> str:
        return f"{self.gameId} ({self.name})"

    def __repr__(self) -> str:
        return (
            "Biome("
                f"flora={self.flora!r}, "
                f"gameId={self.gameId!r}, "
                f"geology={self.geology!r}, "
                f"heat={self.heat!r}, "
                f"humidity={self.humidity!r}, "
                f"name={self.name!r}, "
                f"soil={self.soil!r}, "
                f"water={self.water!r}"
            ")"
        )

    def traits(self) -> list[BiomeTrait]:
        return list([
            self.flora,
            self.geology,
            self.heat,
            self.humidity,
            self.soil,
            self.water,
        ])
