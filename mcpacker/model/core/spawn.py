from collections.abc import Iterable
from mcpacker.model.core.habitat import Habitat


# Class ############################################################################################

class Spawn:
    """
    Abstract base class for placing something into its various habitats.
    """

    def __init__(self, habitats:Iterable[Habitat]|Habitat|None=None):
        if isinstance(habitats, Habitat):
            habitats = habitats.collect()

        self.habitats = habitats or []


    def __repr__(self) -> str:
        return (
            "Spawn(" +
                f"habitats=[{', '.join([repr(h) for h in self.habitats])}]" +
            ")"
        )
