# Class ############################################################################################

class Plant:

    def __init__(self, name:str):
        self.name = name

    def __repr__(self) -> str:
        return f"Plant(name={repr(self.name)})"

    def __str__(self) -> str:
        return self.name
