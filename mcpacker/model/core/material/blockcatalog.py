from mcpacker.model.core.material.block import Block
from typing import Iterator


# Class ############################################################################################

class BlockCatalog:

    def __init__(self, blocks:tuple[Block]=None):
        self._blocks = {}

        for block in (blocks or []):
            self.add(block)

    def __len__(self) -> int:
        return len(self._blocks)

    def add(self, block:Block) -> "BlockCatalog":
        if block.name in self._blocks:
            raise Exception(f"Catalog already contains an entry for {block.name}")

        self._blocks[block.name] = block

    def all(self) -> Iterator[Block]:
        for block in self._blocks.values():
            yield block

    def get(self, name:str) -> Block|None:
        return self._blocks.get(name, None)

