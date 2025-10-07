from collections.abc import Iterator
from tungston.core.world import World


# Constants ########################################################################################

INDENT = "  "

# Class ############################################################################################

class Report:

    def __init__(self, name:str, world:World):
        self.name = name
        self.world = world
        self.reset()

    def __str__(self) -> str:
        return "\n".join(self._lines).strip()

    def __repr__(self) -> str:
        return (
            "Report{" +
                f"lines: {len(self._lines)} lines, " +
                f"lineBuffer: {len(self._lineBuffer)} chunks, " +
                f"indent: {self._indent}" +
            "}"
        )

    def build(self):
        raise NotImplementedError()

    def reset(self) -> "Report":
        self._lineBuffer = []
        self._lines = []
        self._indent = 0
        return self

    def asLines(self) -> Iterator[str]:
        for line in self._lines:
            yield line

    # Helper Methods ###########################################################

    def indent(self) -> "Report":
        self._indent += 1
        self._lineBuffer.insert(0, INDENT)
        return self

    def line(self, text:str="") -> "Report":
        self.text(text)

        self._lines.append("".join(self._lineBuffer))
        self._lineBuffer = []
        while len(self._lineBuffer) < self._indent:
            self._lineBuffer.append(INDENT)

        return self

    def outdent(self) -> "Report":
        self._indent = max(0, self._indent - 1)

        if self._lineBuffer:
            if self._lineBuffer[0] == INDENT:
                self._lineBuffer.pop()

        return self

    def text(self, text:str) -> "Report":
        self._lineBuffer.append(str(text))
        return self
