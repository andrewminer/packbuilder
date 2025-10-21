from collections.abc import Iterable
from mcpacker.model.core.blockstate import BlockState
from mcpacker.model.core.flora.companion import Companion
from mcpacker.model.core.flora.density import Density
from mcpacker.model.core.flora.immersion import Immersion
from mcpacker.model.core.flora.plant import Plant
from mcpacker.model.core.resourceid import ResourceId
from mcpacker.model.core.scarcity import Scarcity

import math
import mcpacker.model.core.flora.density as DE
import mcpacker.model.core.flora.immersion as IM


# Class ############################################################################################

class Patch(Plant):

    def __init__(
        self,
        name:str,
        blocks:Iterable[BlockState|str]|BlockState|str,
        density:Density=DE.THICK,
        radius:int=4,
        substrates:Iterable[ResourceId]|Iterable[str]|ResourceId|str|None=None,
        companions:Iterable[Companion]|Companion|None=None,
        immersion:Immersion=IM.DRY,
    ):
        super().__init__(name)

        if isinstance(blocks, str) or isinstance(blocks, BlockState):
            blocks = [blocks]

        if not companions:
            companions = []
        if isinstance(companions, Companion):
            companions = [companions]

        if not substrates:
            substrates = ["#minecraft:dirt"]
        if not isinstance(substrates, Iterable):
            substrates = [substrates]

        self.blocks = [BlockState.parse(b) for b in blocks]
        self.companions = list(companions)
        self.density = density
        self.immersion = immersion
        self.radius = radius
        self.substrates = [ResourceId.parse(s) for s in substrates]

    def __repr__(self) -> str:
        return (
            "Patch("
                f"blocks={self.blocks!r}, "
                f"companions={self.companions!r}, "
                f"density={self.density!r}, "
                f"immersion={self.immersion!r}, "
                f"radius={self.radius!r}, "
                f"substrates={self.substrates!r}"
            ")"
        )

    def attempts(self, successRate:float=0.25) -> int:
        """
        Estimate how many placement attempts a generator should make for this patch.

        The value models repeated random placement within a circular area until the expected
        fraction of successful placements (`coverage`) for the patch's density is reached.  It
        accounts for both for the presumed rate of successful placements (controlled by
        `successRate`) and duplicate hits on already–filled blocks.

        The relationship is derived from the expected coverage equation:

            coverage = 1 - (1 - successRate / area) ** attempts

        which rearranges to the continuous approximation:

            attempts = -(area / successRate) * ln(1 - coverage)

        where:
            area         = π * radius²
            successRate  = probability that any single attempt succeeds
            coverage     = target fill fraction for this patch's density

        see ChatGPT conversation for full details: http://bit.ly/4neps2i
        """
        coverage = {
            DE.CARPET: 0.99,
            DE.PACKED: 0.8,
            DE.THICK: 0.6,
            DE.THIN: 0.4,
            DE.SPARSE: 0.2,
        }[self.density]

        return math.ceil(max(1/successRate,
            -(math.pi * self.radius * self.radius / successRate) * math.log(1 - coverage)
        ))
