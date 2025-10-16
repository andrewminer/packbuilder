from typing import Any


# Class ############################################################################################

class GenerationStep:

    def __init__(self, gameId:str):
        self.gameId = gameId

    def __eq__(self, other:Any) -> bool:
        if type(self) != type(other): return False
        if self.gameId != other.gameId: return False
        return True

    def __hash__(self) -> int:
        return hash(self.gameId)

    def __repr__(self) -> str:
        return f"GenerationStep(gameId={repr(self.gameId)})"

    def __str__(self) -> str:
        return self.gameId


# Constants ########################################################################################

RAW_GENERATION         = GenerationStep("raw_generation")
LAKES                  = GenerationStep("lakes")
LOCAL_MODIFICATIONS    = GenerationStep("local_modifications")
UNDERGROUND_STRUCTURES = GenerationStep("underground_structures")
SURFACE_STRUCTURES     = GenerationStep("surface_structures")
STRONGHOLDS            = GenerationStep("strongholds")
UNDERGROUND_ORES       = GenerationStep("underground_ores")
UNDERGROUND_DECORATION = GenerationStep("underground_decoration")
FLUID_SPRINGS          = GenerationStep("fluid_springs")
VEGETAL_DECORATION     = GenerationStep("vegetal_decoration")
TOP_LAYER_MODIFICATION = GenerationStep("top_layer_modification")

ALL = [
    RAW_GENERATION,
    LAKES,
    LOCAL_MODIFICATIONS,
    UNDERGROUND_STRUCTURES,
    SURFACE_STRUCTURES,
    STRONGHOLDS,
    UNDERGROUND_ORES,
    UNDERGROUND_DECORATION,
    FLUID_SPRINGS,
    VEGETAL_DECORATION,
    TOP_LAYER_MODIFICATION,
]
