# Class ############################################################################################

class Active:
    """
    The time of day when a creature is normally most active.
    """

    def __init__(self, name: str, start:int, end:int):
        self.name = name
        self.start = start
        self.end = end

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Active<{self.name}>{{start:{self.start}, end:{self.end}}}"


# Constants ########################################################################################

DAY     = Active("day", 0, 12000)
NIGHT   = Active("night", 13000, 23000)
SUNRISE = Active("sunrise", 23000, 24000)
SUNSET  = Active("sunset", 12000, 13000)

ANY         = (SUNRISE, DAY, SUNSET, NIGHT)
DIURNAL     = (DAY)
NOCTURNAL   = (NIGHT)
CREPUSCULAR = (SUNRISE, SUNSET)
