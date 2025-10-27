from collections.abc import Sequence
from collections.abc import Iterable
from mcpacker.model.resourceid import ResourceId
from mcpacker.model.ecology.biome import Biome
from mcpacker.model.ecology.biometrait import BiomeTrait


# Class ############################################################################################

class BiomeFilter:
    """
    A description of which biomes may be considered for a given purpose.

    This class works by accepting *both* allowed and prohibited traits.

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

    @staticmethod
    def collate(biomes:Iterable[Biome], biomeFilters:Iterable["BiomeFilter"]) -> list[Biome]:
        """
        Return the subset of given biomes which are accepted by all of the given filters.
        """
        accepted:set[Biome] = set()

        for biome in biomes:
            for biomeFilter in biomeFilters:
                if not biomeFilter.accepts(biome): continue
                accepted.add(biome)
                break

        return sorted(accepted)

    def __init__(
        self,
        required:Sequence[BiomeTrait|ResourceId|Sequence[BiomeTrait]]|None=None,
        prohibited:Sequence[BiomeTrait|ResourceId]|None=None,
    ):
        self.required = list(required or [])
        self.prohibited = list(prohibited or [])

    def __repr__(self) -> str:
        return (
            "BiomeFilter(" +
                f"required={repr(self.required)}, " +
                f"prohibited={repr(self.prohibited)}" +
            ")"
        )

    def __str__(self) -> str:
        required = []
        for trait in self.required:
            if isinstance(trait, BiomeTrait):
                required.append(str(trait))
            elif isinstance(trait, ResourceId):
                required.append(str(trait))
            else:
                required.append("(" +
                    " or ".join([str(option) for option in trait]) +
                ")")

        prohibited = []
        for trait in self.prohibited:
            prohibited.append(str(trait))

        if not prohibited:
            result = " and ".join(required)
        else:
            result = "".join([
                "must:[", " and ".join(required), "], ",
                "not:[", " or ".join(prohibited), "]",
            ])

        return result

    def accepts(self, biome: Biome) -> bool:
        biomeTraits = biome.traits()

        for condition in self.required:
            if isinstance(condition, BiomeTrait):
                trait = condition
                if trait not in biomeTraits: return False
            elif isinstance(condition, ResourceId):
                if condition != biome.gameId: return False
            else:
                traitOptions = condition
                foundMatch = False
                for trait in traitOptions:
                    if trait in biomeTraits:
                        foundMatch = True
                        break

                if not foundMatch: return False

        for prohibitedTrait in self.prohibited:
            if isinstance(prohibitedTrait, ResourceId):
                if prohibitedTrait == biome.gameId: return False
            else:
                if prohibitedTrait in biomeTraits: return False

        return True
