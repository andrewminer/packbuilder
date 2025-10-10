from mcpacker.write.writer  import Writer
from mcpacker.model.modpack import ModPack
from pathlib                import Path
from typing                 import TextIO

import os
import shutil


# Constants ########################################################################################

INDENT          = "  "
REPORT_DIR_PATH = "reports"


# Class ############################################################################################

class MarkdownWriter(Writer):

    def __init__(self, name:str, pack:ModPack, outputDir:Path):
        super().__init__(pack, outputDir)

        self._file:TextIO|None = None
        self._name = name
        self._indent = 0
        self._lineBuffer:list[str] = []

    def write(self):
        path = self.outputDir / self.pack.name / REPORT_DIR_PATH / self._name

        path.parent.mkdir(exist_ok=True, parents=True)
        with path.open("w") as file:
            try:
                self._file = file
                self.compose()
            finally:
                self._file = None

    def compose(self) -> str:
        raise NotImplementedError()

    # Helper Methods ###########################################################

    def indent(self) -> "MarkdownWriter":
        self._indent += 1
        self._lineBuffer.insert(0, INDENT)
        return self

    def line(self, text:str="") -> "MarkdownWriter":
        assert self._file != None
        self.text(text)

        self._file.write("".join(self._lineBuffer) + "\n")
        self._lineBuffer = []
        while len(self._lineBuffer) < self._indent:
            self._lineBuffer.append(INDENT)

        return self

    def outdent(self) -> "MarkdownWriter":
        self._indent = max(0, self._indent - 1)

        if self._lineBuffer:
            if self._lineBuffer[0] == INDENT:
                self._lineBuffer.pop()

        return self

    def text(self, text:str) -> "MarkdownWriter":
        self._lineBuffer.append(str(text))
        return self
