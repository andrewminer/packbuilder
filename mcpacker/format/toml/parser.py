from mcpacker.format.tokenizer import Tokenizer
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


# Helper Classes ###################################################################################

class TomlParseError(Exception):

    def __init__(self, message:str, line:int):
        self.message = message
        self.line = line

    def __str__(self) -> str:
        return f"TomlParseError:{self.line}: {self.message}"


# Class ############################################################################################

class TomlParser:

    def __init__(self, text:str):
        self._tokenizer = Tokenizer(text)

    def parse(self) -> TomlDocument:
        entries = []
        while True:
            entry = self._parseDocumentEntry()
            if not entry: break
            entries.append(entry)

        return TomlDocument(entries)

    # Private Methods ##########################################################

    def _parseArray(self) -> TomlArray|None:
        openToken = self._tokenizer.next()
        if openToken.name != "open-bracket":
            self._tokenizer.reject(openToken)
            return None

        entries = []
        while True:
            entry = self._parseArrayEntry()
            if not entry: break
            entries.append(entry)

            commaToken = self._tokenizer.next()
            if commaToken.name != "comma":
                self._tokenizer.reject(commaToken)
                break

        closeToken = self._tokenizer.next()
        if closeToken.name != "close-bracket":
            raise TomlParseError(f"expected ] but found {closeToken.text}", closeToken.line)

        return TomlArray(entries)

    def _parseArrayEntry(self) -> TomlArrayEntry|None:
        return self._parseComment() or self._parseValue()

    def _parseComment(self) -> TomlComment|None:
        token = self._tokenizer.next()
        if token.name != "comment":
            self._tokenizer.reject(token)
            return None

        return TomlComment(token.text)

    def _parseDocumentEntry(self) -> TomlDocumentEntry|None:
        return self._parseComment() or self._parseTable() or self._parsePair()

    def _parseMapEntry(self) -> TomlMapEntry|None:
        return self._parseComment() or self._parsePair()

    def _parseMap(self) -> TomlMap|None:
        openToken = self._tokenizer.next()
        if openToken.name != "open-brace":
            self._tokenizer.reject(openToken)
            return None

        entries = []
        while True:
            entry = self._parseMapEntry()
            if not entry: break
            entries.append(entry)

            commaToken = self._tokenizer.next()
            if commaToken.name != "comma":
                self._tokenizer.reject(commaToken)
                break

        closeToken = self._tokenizer.next()
        if closeToken.name != "close-brace":
            raise TomlParseError(f"expected }} but found {closeToken.text}", closeToken.line)

        return TomlMap(entries)

    def _parsePair(self) -> TomlPair|None:
        keyToken = self._tokenizer.next()
        if keyToken.name not in ["identifier", "quoted-text"]:
            self._tokenizer.reject(keyToken)
            return None

        equalToken = self._tokenizer.next()
        if equalToken.name != "equal":
            self._tokenizer.reject(equalToken)
            self._tokenizer.reject(keyToken)
            return None

        value = self._parseValue()
        if not value:
            self._tokenizer.reject(equalToken)
            self._tokenizer.reject(keyToken)
            return None

        return TomlPair(keyToken.text, value)

    def _parseScalar(self) -> TomlScalar|None:
        token = self._tokenizer.next()
        result = None

        if token.name == "bool":
            result = TomlScalar(True if token.text.lower() == "true" else False)
        elif token.name == "int":
            result = TomlScalar(int(token.text))
        elif token.name == "float":
            result = TomlScalar(float(token.text))
        elif token.name == "quoted-text":
            result = TomlScalar(token.text)
        else:
            self._tokenizer.reject(token)

        return result

    def _parseTable(self) -> TomlTable|None:
        path = self._parseTablePath()

        entries:list[TomlTableEntry] = []
        while True:
            entry = self._parseTableEntry()
            if not entry: break
            entries.append(entry)

        if not (path or entries):
            return None
        elif not path:
            path = TomlTablePath([""])

        return TomlTable(path, entries)

    def _parseTableEntry(self) -> TomlTableEntry|None:
        return self._parseComment() or self._parsePair()

    def _parseTablePath(self) -> TomlTablePath|None:
        openToken = self._tokenizer.next()
        if openToken.name != "open-bracket":
            self._tokenizer.reject(openToken)
            return None

        quotedNameToken = self._tokenizer.next()
        if quotedNameToken.name == "quoted-text":
            closeToken = self._tokenizer.next()
            if closeToken.name != "close-bracket":
                raise TomlParseError(f"expected ], but found {closeToken.text}", closeToken.line)

            return TomlTablePath([quotedNameToken.text])
        else:
            self._tokenizer.reject(quotedNameToken)

        nameParts:list[str] = []
        while True:
            namePartToken = self._tokenizer.next()
            if namePartToken.name != "identifier":
                raise TomlParseError(
                    f"expected a name part, but found {namePartToken.text}",
                    namePartToken.line
                )

            nameParts.append(namePartToken.text)

            periodToken = self._tokenizer.next()
            if periodToken.name != "period":
                self._tokenizer.reject(periodToken)
                break

        closeToken = self._tokenizer.next()
        if closeToken.name != "close-bracket":
            raise TomlParseError(f"expected ], but found {closeToken.text}", closeToken.line)

        return TomlTablePath(nameParts)

    def _parseValue(self) -> TomlValue|None:
        return self._parseScalar() or self._parseArray() or self._parseMap()
