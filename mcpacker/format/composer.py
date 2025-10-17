from typing import Self


# Class ############################################################################################

class Composer:

    def __str__(self) -> str:
        raise NotImplementedError()

    def compose(self) -> Self:
        self.doCompose()
        return self

    def doCompose(self):
        raise NotImplementedError()
