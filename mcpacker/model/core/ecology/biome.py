from mcpacker.model.core.ecology.biometrait import BiomeTrait
from mcpacker.model.core.ecology.flora import Flora
from mcpacker.model.core.ecology.geology import Geology
from mcpacker.model.core.ecology.heat import Heat
from mcpacker.model.core.ecology.humidity import Humidity
from mcpacker.model.core.ecology.soil import Soil
from mcpacker.model.core.ecology.water import Water
from mcpacker.model.core.resourceid import ResourceId


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

    def __eq__(self, other) -> bool:
        if type(self) != type(other): return False
        if self.gameId != other.gameId: return False
        if self.name != other.name: return False
        return True

    def __hash__(self) -> int:
        return hash((self.gameId, self.name))

    def __str__(self) -> str:
        return f"{self.gameId} ({self.name})"

    def __repr__(self) -> str:
        return "".join([str(p) for p in [
            "Biome(",
                "flora=", repr(self.flora), ", ",
                "geology=", repr(self.geology), ", ",
                "heat=", repr(self.heat), ", ",
                "humidity=", repr(self.humidity), ", ",
                "soil=", repr(self.soil), ", ",
                "water=", repr(self.water),
            ")"
        ]])

    def traits(self) -> list[BiomeTrait]:
        return list([
            self.flora,
            self.geology,
            self.heat,
            self.humidity,
            self.soil,
            self.water,
        ])
