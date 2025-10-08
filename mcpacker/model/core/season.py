# Class ############################################################################################

class Season:
    """
    A time of year demonstrating different climate and activity among flora and fauna.
    """

    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Season<{self.name}>"


# Constants ########################################################################################

SPRING = Season("spring")
SUMMER = Season("summer")
AUTUMN = Season("autumn")
WINTER = Season("winter")

ALL = [SPRING, SUMMER, AUTUMN, WINTER]

WET = [WINTER, SPRING]
DRY = [SUMMER, AUTUMN]

HOT  = [SUMMER]
COOL = [SPRING, AUTUMN]
COLD = [WINTER]


# Constants ########################################################################################

def exclude(target:Season) -> list[Season]:
    result = []

    for season in ALL:
        if season == target: continue
        result.append(season)

    return result
