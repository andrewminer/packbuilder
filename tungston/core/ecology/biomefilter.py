from tungston.core.ecology.biome import Biome
from tungston.core.ecology.biometrait import BiomeTrait


# Class ############################################################################################

class BiomeFilter:
    """
    A description of which biomes may be considered for a given purpose.

    This class works by allowing *both* allowed and prohibited traits.

    The list of allowed traits may contain either individual trait objects, or a list of such
    objects.  When an individual trait is given, only biomes with that exact trait are permitted.
    When a list of traits is given, biomes containing any of the listed traits are permitted.  To
    put it another way, each individual item in the required list is an "OR" filter, and the results
    of the entire list are "AND"ed together.

    The list of prohibited traits only permits individual traits, but multiple traits of the same
    sort may be given.

    The filter only accepts biomes which pass *both* lists.  That is, it must possess *all* the
    required traits while simultaneously not possessing *any* of the prohibited ones.
    """

    def __init__(
        self,
        required:list[BiomeTrait|list[BiomeTrait]]=None,
        prohibited:list[BiomeTrait]=None,
    ):
        self.required = required or []
        self.prohibited = prohibited or []

    def __repr__(self) -> str:
        return f"BiomeFilter([{repr(self.required)}], [{repr(self.prohibited)}])"

    def accepts(self, biome: Biome) -> bool:
        biomeTraits = biome.traits()

        for condition in self.required:
            if isinstance(condition, BiomeTrait):
                trait = condition
                if trait not in biomeTraits: return False
            else:
                traitOptions = condition
                foundMatch = False
                for trait in traitOptions:
                    if trait in biomeTraits:
                        foundMatch = True
                        break

                if not foundMatch: return False

        for prohibitedTrait in self.prohibited:
            if prohibitedTrait in biomeTraits: return False

        return True
