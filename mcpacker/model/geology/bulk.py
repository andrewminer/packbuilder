from typing import Any
import math


# Class ############################################################################################

class Bulk:
    """
    Bulk describes the tendency of the material in a mineral deposit to clump together.

    The `blobCount` describes how many blobs of mineral will appear in a 16mx16mx16m cube, more bulk
    implies fewer overall blobs of larger size. For 2D deposit types (e.g., disk), this refers to
    how many individual shapes are placed.

    In any case, the total amount of mineral deposited remains the same (i.e., controlled by
    `Scarcity`).
    """

    def __init__(self, name:str, blobCount:int):
        self.name = name
        self.blobCount = blobCount

    def __eq__(self, other:Any) -> bool:
        if type(self) != type(other): return False
        if self.name != other.name: return False
        return True

    def __hash__(self) -> int:
        return hash(self.name)

    def __repr__(self) -> str:
        return f"Bulk(name={self.name!r}, blobCount={self.blobCount!r})"

    def __str__(self) -> str:
        return f"{self.name} ({self.blobCount})"


# Constants ########################################################################################

TINY   = Bulk("tiny", 5)
SMALL  = Bulk("small", 4)
MEDIUM = Bulk("medium", 3)
LARGE  = Bulk("large", 2)
HUGE   = Bulk("huge", 1)

ALL = [TINY, SMALL, MEDIUM, LARGE, HUGE]

# Helper Functions #################################################################################

# TODO: The following properly belong somewhere in mcpacker.format, but I'm not sure where yet.

ORE_MAX_BLOCKS = [
    0, 0, 0, 4, 5, 8, 9, 10, 10, 13, 16, 17, 23, 24, 24, 29, 32, 37, 46, 52, 52, 60, 68, 68, 74, 82,
    94, 104, 106, 120, 128, 135, 149, 160, 180, 190, 204, 212, 228, 246, 262, 276, 292, 308, 324,
    344, 360, 381, 403, 429, 452, 480, 500, 530, 558, 584, 616, 634, 664, 694, 730, 760, 790, 826,
    864
]

def convertBlockCountToSize(blockCount:int) -> int:
    """Return the smallest integer `size` whose vein can reach at least max_blocks."""
    for size, maxCount in enumerate(ORE_MAX_BLOCKS):
        if maxCount >= blockCount:
            return size

    return len(ORE_MAX_BLOCKS) - 1
