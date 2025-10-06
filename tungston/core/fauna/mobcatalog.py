from tungston.core.fauna.mob import Mob


# Class ############################################################################################

class MobCatalog:

    def __init__(self, mobs):
        self.mobs = mobs

    def findByName(self, name):
        for mob in self.mobs:
            if mob.name == name:
                return mob

        return None
