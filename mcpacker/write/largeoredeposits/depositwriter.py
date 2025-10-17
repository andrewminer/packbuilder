from mcpacker.format.largeoredeposit.mineraldepositcomposer import MineralDepositComposer
from mcpacker.model.core.geology.deposit.mineraldeposit import MineralDeposit
from mcpacker.model.modpack import ModPack
from mcpacker.write.writer import Writer
from pathlib import Path


# Class ############################################################################################

class DepositWriter(Writer):

    def doWrite(self):
        for deposit in self.pack.world.deposits:
            if not isinstance(deposit, MineralDeposit): continue

            path = self.locator.lod_deposits() / f"{deposit.name}.cfg"
            self.resetOutputFile(path)

            path.write_text(str(MineralDepositComposer(deposit).compose()))
