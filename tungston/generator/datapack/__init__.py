import os


# Class ############################################################################################

class Datapack:

    def __init__(self, path:str):
        self.path = path

    @property
    def name(self) -> str:
        return os.path.basename(self.path)

