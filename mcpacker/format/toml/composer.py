from mcpacker.format.textcomposer import TextComposer
from mcpacker.format.toml.model import TomlArray
from mcpacker.format.toml.model import TomlArrayEntry
from mcpacker.format.toml.model import TomlComment
from mcpacker.format.toml.model import TomlDocument
from mcpacker.format.toml.model import TomlDocumentEntry
from mcpacker.format.toml.model import TomlMap
from mcpacker.format.toml.model import TomlMapEntry
from mcpacker.format.toml.model import TomlPair
from mcpacker.format.toml.model import TomlScalar
from mcpacker.format.toml.model import TomlScalarValue
from mcpacker.format.toml.model import TomlTable
from mcpacker.format.toml.model import TomlTableEntry
from mcpacker.format.toml.model import TomlTablePath
from mcpacker.format.toml.model import TomlValue
from typing import get_args


# Class ############################################################################################

class TomlComposer(TextComposer):

    def __init__(self, document:TomlDocument):
        super().__init__()
        self._document = document

    def doCompose(self):
        self.reset()

        for entry in self._document.entries:
            if isinstance(entry, TomlComment): self._composeComment(entry)
            if isinstance(entry, TomlPair): self._composePair(entry)
            if isinstance(entry, TomlTable): self._composeTable(entry)

    # Private Methods ##########################################################

    def _composeComment(self, comment:TomlComment):
        self.text("# ").line(comment.text)

    def _composeMap(self, tomlMap:TomlMap):
        self.text("{")
        self.indent()
        for entry in tomlMap.entries:
            if isinstance(entry, TomlComment): self._composeComment(entry)
            if isinstance(entry, TomlPair): self._composePair(entry)
        self.outdent()
        self.text("}")

    def _composeArray(self, array:TomlArray):
        self.line("[")
        self.indent()
        needsDelimiter = False
        for element in array.entries:
            if needsDelimiter: self.line(",")
            needsDelimiter = True

            if isinstance(element, TomlComment):
                self._composeComment(element)
            else:
                self._composeValue(element)

        self.line()
        self.outdent()
        self.text("]")

    def _composePair(self, pair:TomlPair):
        self.text(pair.key).text(" = ")
        if isinstance(pair.value, TomlScalar): self._composeScalar(pair.value)
        if isinstance(pair.value, TomlArray): self._composeArray(pair.value)
        if isinstance(pair.value, TomlMap): self._composeMap(pair.value)

    def _composeScalar(self, scalar:TomlScalar):
        if isinstance(scalar.value, bool):
            self.text("true" if scalar.value else "false")
        elif isinstance(scalar.value, int):
            self.text(f"{scalar.value:d}")
        elif isinstance(scalar.value, float):
            self.text(f"{scalar.value:0.3f}")
        elif isinstance(scalar.value, str):
            value = (scalar.value
                .replace("\\", "\\\\")
                .replace('"', '\\"')
                .replace("\t", "\\t")
                .replace("\n", "\\n")
                .replace("\r", "\\r")
            )
            self.text("\"").text(value).text("\"")

    def _composeTable(self, table:TomlTable):
        self.resetIndent()
        self.text("[")
        needsDelimiter = False
        for pathPart in table.path.parts:
            if needsDelimiter: self.text(".")
            needsDelimiter = True
            self.text(pathPart)
        self.line("]")

        for entry in table.entries:
            if isinstance(entry, TomlComment):
                self._composeComment(entry)
            elif isinstance(entry, TomlPair):
                self._composePair(entry)
                self.line()

        if len(table.entries) > 0:
            self.line()

    def _composeValue(self, value:TomlValue):
        if isinstance(value, TomlScalar): self._composeScalar(value)
        if isinstance(value, TomlArray): self._composeArray(value)
        if isinstance(value, TomlMap): self._composeMap(value)
