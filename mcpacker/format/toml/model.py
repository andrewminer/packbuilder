from __future__ import annotations
from collections.abc import Iterable
from typing import Union


# Type Support #####################################################################################

type TomlScalarValue = bool | int | float | str

type TomlValue = TomlScalar | TomlArray | TomlMap

type TomlArrayEntry = TomlComment | TomlValue

type TomlMapEntry = TomlComment | TomlPair

type TomlTableEntry = TomlComment | TomlPair

type TomlDocumentEntry = TomlComment | TomlPair | TomlTable


# Classes ##########################################################################################

class TomlArray:

    def __init__(self, entries:Iterable[TomlArrayEntry]):
        self.entries = entries

    def __repr__(self) -> str:
        return (
            "TomlArray{entries:[" +
                ",".join(repr(e) for e in self.entries) +
            "]}"
        )

class TomlComment:

    def __init__(self, text:str):
        self.text = text

    def __repr__(self) -> str:
        return f"TomlComment{{text:{repr(self.text)}}}"

class TomlDocument:

    def __init__(self, entries:Iterable[TomlDocumentEntry]|None=None):
        self.entries = list(entries or [])

    def findTable(self, name:str) -> TomlTable|None:
        for entry in self.entries:
            if isinstance(entry, TomlTable):
                if entry.name == name:
                    return entry

        return None

    def __repr__(self) -> str:
        return (
            "TomlDocument{entries:[" +
                ",".join(repr(e) for e in self.entries) +
            "]}"
        )

class TomlMap:

    def __init__(self, entries:Iterable[TomlMapEntry]):
        self.entries = entries

    def __repr__(self) -> str:
        return (
            "TomlMap{entries:[" +
                ",".join(repr(e) for e in self.entries) +
            "]}"
        )

class TomlPair:

    def __init__(self, key:str, value:TomlValue):
        self.key = key
        self.value = value

    def __repr__(self) -> str:
        return f"TomlPair{{key:{repr(self.key)},value:{repr(self.value)}}}"

class TomlScalar:

    def __init__(self, value:TomlScalarValue):
        self.value = value

    def __repr__(self) -> str:
        return f"TomlScalar{{value:{repr(self.value)}}}"

class TomlTable:

    def __init__(
        self,
        path:TomlTablePath,
        entries:Iterable[TomlTableEntry]|None=None,
    ):
        self.path = path
        self.entries = list(entries or [])

    @property
    def name(self) -> str:
        return str(self.path)

    def __repr__(self) -> str:
        return (
            "TomlTable{" +
                f"path:{repr(self.path)}," +
                f"entries:[" +
                    ",".join(repr(e) for e in self.entries) +
                "]" +
            "}"

        )

class TomlTablePath:

    def __init__(self, parts:Iterable[str]):
        self.parts = parts

    def __str__(self) -> str:
        return ".".join(self.parts)

    def __repr__(self) -> str:
        return (
            "TomlTablePath{parts:[" +
                ".".join(repr(p) for p in self.parts) +
            "]}"
        )
