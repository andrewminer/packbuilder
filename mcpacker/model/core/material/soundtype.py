# Class ############################################################################################

class SoundType:

    def __init__(self, name:str):
        self.name = name

    def __eq__(self, other) -> bool:
        if type(self) != type(other): return False
        if self.name != other.name: return False
        return True

    def __hash__(self) -> int:
        return hash(self.name)

    def __repr__(self) -> str:
        return f"SoundType<{self.name}>"

    def __str__(self) -> str:
        return self.name

# Constants ########################################################################################

CRYSTAL = SoundType("crystal")
DIRT    = SoundType("dirt")
FOLIAGE = SoundType("foliage")
GLASS   = SoundType("glass")
GRAVEL  = SoundType("gravel")
HONEY   = SoundType("honey")
METAL   = SoundType("metal")
SCULK   = SoundType("sculk")
SLIME   = SoundType("slime")
STONE   = SoundType("stone")
WOOD    = SoundType("wood")
WOOL    = SoundType("wool")
