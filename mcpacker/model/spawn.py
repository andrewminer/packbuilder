from collections.abc import Iterable
from mcpacker.model.habitat import Habitat


# Class ############################################################################################

class Spawn:
    """
    Abstract base class for placing something into its various habitats.
    """

    def __init__(self, habitats:Iterable[Habitat]|Habitat|None=None):
        if isinstance(habitats, Habitat):
            habitats = list(habitats.collect())

        self.habitats = list(habitats or [])

    def __repr__(self) -> str:
        return f"Spawn(habitats={self.habitats!r})"

