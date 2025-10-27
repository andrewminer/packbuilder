from mcpacker.model.modpack import ModPack
from mcpacker.pack.mysteriousisland.addbiomes import addBiomes
from mcpacker.pack.mysteriousisland.addblocks import addBlocks
from mcpacker.pack.mysteriousisland.adddisabledfeatures import addDisabledFeatures
from mcpacker.pack.mysteriousisland.additems import addItems
from mcpacker.pack.mysteriousisland.addminerals import addMinerals
from mcpacker.pack.mysteriousisland.addmineralspawns import addMineralSpawns
from mcpacker.pack.mysteriousisland.addmobs import addMobs
from mcpacker.pack.mysteriousisland.addmobspawns import addMobSpawns
from mcpacker.pack.mysteriousisland.addplants import addPlants
from mcpacker.pack.mysteriousisland.addplantspawns import addPlantSpawns


# Constants ########################################################################################

def buildModPack():
    pack = ModPack("mysteriousisland")

    # Order is significant as layers have dependencies
    pack.augment(addBiomes)
    pack.augment(addItems)
    pack.augment(addBlocks)
    pack.augment(addMinerals)
    pack.augment(addMineralSpawns)
    pack.augment(addPlants)
    pack.augment(addPlantSpawns)
    pack.augment(addMobs)
    pack.augment(addMobSpawns)
    pack.augment(addDisabledFeatures)

    return pack
