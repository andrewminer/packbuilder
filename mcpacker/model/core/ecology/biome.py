from mcpacker.model.core.ecology.biometrait import BiomeTrait
from mcpacker.model.core.ecology.flora import Flora
from mcpacker.model.core.ecology.geology import Geology
from mcpacker.model.core.ecology.heat import Heat
from mcpacker.model.core.ecology.humidity import Humidity
from mcpacker.model.core.ecology.soil import Soil
from mcpacker.model.core.ecology.water import Water


####################################################################################################

class Biome(object):
    """
    A region of the world defined by a unique combination of geology, topography, and ecology.
    """

    def __init__(
        self,
        city:str,
        gameId:str,
        flora:Flora,
        geology:Geology,
        heat:Heat,
        humidity:Humidity,
        soil:Soil,
        water:Water,
    ):
        self.city = city
        self.gameId = gameId

        self.flora = flora
        self.geology = geology
        self.heat = heat
        self.humidity = humidity
        self.soil = soil
        self.water = water

    def __eq__(self, other) -> bool:
        if type(self) != type(other): return False
        if self.biomeId != other.biomeId: return False
        if self.city != other.city: return False
        return True

    def __hash__(self) -> int:
        return hash((self.biomeId, self.city))

    def __str__(self) -> str:
        return f"{self.city}<{self.gameId}>"

    def __repr__(self) -> str:
        return "".join([str(p) for p in [
            str(self), "{",
                repr(self.flora), ", ",
                repr(self.geology), ", ",
                repr(self.heat), ", ",
                repr(self.humidity), ", ",
                repr(self.soil), ", ",
                repr(self.water),
            "}"
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
