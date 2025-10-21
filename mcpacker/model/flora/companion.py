from mcpacker.model.flora.plant import Plant


# Class ############################################################################################

class Companion:

    def __init__(self, plant:Plant, weight:int):
        self.plant = plant
        self.weight = weight
