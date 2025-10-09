# Class ############################################################################################

class Kind:

    def __init__(self, name:str):
        self.name = name

    def __eq__(self, other) -> bool:
        if type(self) != type(other): return False
        if self.name != other.name: return False
        return True

    def __repr__(self) -> str:
        return f"Kind<{self.name}>"

    def __str__(self) -> str:
        return self.name


# Constants ########################################################################################

ITEM = Kind("item")
BLOCK = Kind("block")
