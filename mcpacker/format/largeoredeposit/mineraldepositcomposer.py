from collections.abc import Iterator
from collections.abc import Mapping
from mcpacker.model.geology.inclusion import Inclusion
from mcpacker.format.templatecomposer import TemplateComposer
from mcpacker.model.geology.deposit.mineraldeposit import MineralDeposit


# Constants ########################################################################################

TEMPLATE = """
Config {{
    B:enabled = true
}}

Deposit {{
    S:customReplacements <
        {customReplacements}
    >
    S:ores <
        {ores}
    >
    I:rarity={rarity}
    S:replaceableBlocks <
        {replaceableBlocks}
    >
    B:vanilla=false
    Dimensions {{
        S:blackList <
        >
        S:whiteList <
        >
    }}
    Biomes {{
        S:blackList <
        >
        S:whiteList <
        >
    }}
    Altitude {{
        I:min={altitudeMin}
        I:max={altitudeMax}
    }}
    Miscellaneous {{
        B:exposed=true
        S:proportions={proportions}
        B:strictBounds=false
        B:strictStart=false
    }}
    Indicator {{
        S:circles <
        >
        S:continuity=0
        I:distortion=0
        S:id={indicatorId}
        S:threshold=100
    }}
    Size {{
        i:min={sizeMin}
        I:max={sizeMax}
    }}
}}
""".strip()

# Class ############################################################################################

class MineralDepositComposer(TemplateComposer):

    def __init__(self, deposit:MineralDeposit):
        super().__init__(TEMPLATE)
        self._deposit = deposit

    def gatherData(self) -> dict[str,str]:
        return {
            "altitudeMin": f"{self._deposit.altitude.bottom}",
            "altitudeMax": f"{self._deposit.altitude.top}",
            "customReplacements": "\n        ".join(self._gatherCustomReplacements()),
            "indicatorId": f"deposit/{self._deposit.gameId}_marker",
            "ores": "\n        ".join(self._gatherOres()),
            "proportions": f"{self._deposit.proportion.ratio:0.2f}",
            "rarity": f"{self._gatherRarity()}",
            "replaceableBlocks": "\n        ".join(self._gatherReplaceableBlocks()),
            "sizeMin": f"{self._deposit.bulk.smallest}",
            "sizeMax": f"{self._deposit.bulk.largest}",
        }

    # Private Methods ##########################################################

    def _gatherCustomReplacements(self) -> list[str]:
        result = {}

        for inclusion in self._deposit.inclusions:
            if len(inclusion.mineral.replacements) < 2: continue
            for replacement in inclusion.mineral.replacements[1:]:
                result[f"{replacement.source}->{replacement.target},{inclusion.weight}"] = True

        return list(result.keys())

    def _gatherOres(self) -> list[str]:
        result = {}

        for inclusion in self._deposit.inclusions:
            if len(inclusion.mineral.replacements) < 1: continue
            for replacement in inclusion.mineral.replacements[0:1]:
                result[f"{replacement.target},{inclusion.weight}"] = True

        return list(result.keys())

    def _gatherReplaceableBlocks(self) -> list[str]:
        result = {}

        for inclusion in self._deposit.inclusions:
            if len(inclusion.mineral.replacements) < 1: continue
            for replacement in inclusion.mineral.replacements[0:1]:
                result[f"{replacement.source}"] = True

        return list(result.keys())

    def _gatherRarity(self) -> int:
        return {
            "absent": 1000**2,
            "rare": 21**2,
            "unusual": 13**2,
            "sparse": 8**2,
            "uncommon": 5**2,
            "common": 3**2,
            "carpet": 1**2,
        }[self._deposit.scarcity.name]
