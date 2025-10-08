from mcpacker.model.modpack                        import ModPack
from mcpacker.pack.mysteriousisland.biomecatalog   import addBiomes
from mcpacker.pack.mysteriousisland.blockcatalog   import addBlocks
from mcpacker.pack.mysteriousisland.depositcatalog import addDeposits
from mcpacker.pack.mysteriousisland.itemcatalog    import addItems
from mcpacker.pack.mysteriousisland.mineralcatalog import addMinerals
from mcpacker.pack.mysteriousisland.mobcatalog     import addMobs
from mcpacker.pack.mysteriousisland.datapack       import addDataPack
from mcpacker.pack.mysteriousisland.resourcepack   import addResourcePack


# Constants ########################################################################################

def buildModPack():
    pack = ModPack("mysteriousisland")

    # Order is significant as layers have dependencies
    pack.augment(addBiomes)
    pack.augment(addItems)
    pack.augment(addBlocks)
    pack.augment(addMinerals)
    pack.augment(addDeposits)
    pack.augment(addMobs)
    pack.augment(addResourcePack)
    pack.augment(addDataPack)

    return pack
