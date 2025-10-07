from mcpacker.model.core.geology.deposit import Deposit
from mcpacker.model.core.geology.mineralcatalog import MineralCatalog
from typing import Iterator


# Class ############################################################################################

class DepositCatalog:

    def __init__(self, deposits:None|tuple[Deposit]=None):
        self._deposits = {}

        for deposit in (deposits or []):
            self.add(deposit)

    def add(self, deposit:Deposit) -> "DepositCatalog":
        if deposit.name in self._deposits:
            raise Exception("Catalog already has an entry for {deposit.name}")

        self._deposits[deposit.name] = deposit

    def all(self) -> Iterator[Deposit]:
        for deposit in self._deposits.values():
            yield deposit

    def get(self, name:str) -> Deposit|None:
        return self._deposits.get(name, None)
