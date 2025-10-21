from mcpacker.format.resourcepack.variant import Variant


# Class ############################################################################################

class BlockState:
    """
    A mapping between a block and the model(s) used to represent it in game.

    see: https://minecraft.wiki/w/Tutorial:Models#Block_states
    """

    def __init__(self, defaultVariant:Variant|None=None):
        self.variants:dict[str,Variant] = {}

        if defaultVariant:
            self.defaultVariant = defaultVariant

    @property
    def defaultVariant(self) -> Variant|None:
        return self.variants.get("", None)

    @defaultVariant.setter
    def defaultVariant(self, value:Variant):
        self.variants[""] = value
