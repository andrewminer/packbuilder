from tungston.core.habitat import Habitat


# Class ############################################################################################

class Placement:
    """
    Abstract base class for placing something into its various habitats.
    """

    def __init__(self, habitats:tuple[Habitat]=None):
        self.habitats = habitats

        if not self.habitats:
            self.habitats = ()

        if isinstance(self.habitats, Habitat):
            self.habitats = self.habitats.collect()


    def __repr__(self) -> str:
        return (
            "Placement{" +
                f"habitats: [{', '.join([repr(h) for h in self.habitats])}]" +
            "}"
        )
