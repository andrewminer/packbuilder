from mcpacker.model.spawnable import Spawnable


# Class ############################################################################################

class Plant(Spawnable):

    def __repr__(self) -> str:
        return f"Plant(name={self.name!r})"
