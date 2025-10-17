from mcpacker.format.composer import Composer
from typing import Any
from typing import Self


# Class ############################################################################################

class TextComposer(Composer):

    def __init__(self, indentText:str="    "):
        self._indent = 0
        self._indentText = indentText
        self._lineBuffer:list[str] = []
        self._lines:list[str] = []

    def __str__(self) -> str:
        return "\n".join(self._lines)

    # Helper Methods ###########################################################

    def doCompose(self):
        raise NotImplementedError()

    def include(self, composer:"TextComposer") -> Self:
        composer.reset()
        composer.compose()
        for line in composer._lines:
            self._lines.append(line)

        return self

    def indent(self) -> Self:
        self._indent += 1
        self._lineBuffer.insert(0, self._indentText)
        return self

    def line(self, text:Any="") -> Self:
        self.text(text)

        self._lines.append("".join(self._lineBuffer).rstrip())
        self._lineBuffer = []
        while len(self._lineBuffer) < self._indent:
            self._lineBuffer.append(self._indentText)

        return self

    def outdent(self) -> Self:
        self._indent = max(0, self._indent - 1)

        if self._lineBuffer:
            if self._lineBuffer[0] == self._indentText:
                del self._lineBuffer[0]

        return self

    def reset(self) -> Self:
        self._lineBuffer = []
        self._lines = []
        self._indent = 0
        return self

    def resetIndent(self) -> Self:
        self._indent = 0
        return self

    def text(self, text:Any) -> Self:
        self._lineBuffer.append(str(text))
        return self
