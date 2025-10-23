from mcpacker.model.scarcity import Scarcity
from typing import Any

import mcpacker.model.scarcity as SC


# Class ############################################################################################

class Ecotype:

    def __init__(self, scarcity:Scarcity|None=None):
        self.scarcity = scarcity or SC.SPARSE

    def __eq__(self, other:Any) -> bool:
        if type(self) != type(other): return False
        if self.scarcity != other.scarcity: return False
        return True

    def __repr__(self) -> str:
        return f"Ecotype(scarcity={self.scarcity!r})"
