from mcpacker.pack.mysteriousisland.modpack import buildModPack
from mcpacker.ui.runner import Runner

import sys


# Script ###########################################################################################

if __name__ == "__main__":
    Runner(buildModPack()).run(sys.argv)
