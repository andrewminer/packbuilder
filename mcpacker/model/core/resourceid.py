from collections.abc import Callable
from typing import Any


# Typing Support ###################################################################################

type NameTransformFunc = Callable[[str],str]


# Class ############################################################################################

class ResourceId:

    @staticmethod
    def alterName(text:str, doTransform:NameTransformFunc) -> str:
        resourceId = ResourceId.parse(text)
        resourceId.name = doTransform(resourceId.name)
        return str(resourceId)

    @staticmethod
    def canonical(text:str) -> str:
        return str(ResourceId.parse(text))

    @staticmethod
    def parse(text:"ResourceId|str") -> "ResourceId":
        if isinstance(text, ResourceId):
            return text

        isTag = False
        if text.startswith("#"):
            isTag = True
            text = text[1:]

        index = text.find(":")
        if index > 0:
            mod = text[0:index]
            name = text[index+1:]
        elif index == 0:
            mod = "minecraft"
            name = text[1:]
        else:
            mod = "minecraft"
            name = text

        return ResourceId(isTag, mod, name)

    def __init__(self, isTag:bool, mod:str, name:str):
        self.isTag = isTag
        self.mod = mod
        self.name = name

    def __eq__(self, other:Any) -> bool:
        if type(self) != type(other): return False
        if self.isTag != other.isTag: return False
        if self.mod != other.mod: return False
        if self.name != other.name: return False
        return True

    def __hash__(self) -> int:
        return hash((self.isTag, self.mod, self.name))

    def __lt__(self, other:Any) -> bool:
        if type(self) != type(other): raise TypeError()

        if self.isTag != other.isTag:
            return self.isTag
        if self.mod != other.mod:
            return self.mod < other.mod
        if self.name != other.name:
            return self.name < other.name

        return False

    def __str__(self) -> str:
        if self.isTag:
            return f"#{self.mod}:{self.name}"

        return f"{self.mod}:{self.name}"


    def __repr__(self) -> str:
        return (
            "ResourceId(" +
                f"isTag={repr(self.isTag)}, " +
                f"mod={repr(self.mod)}, " +
                f"name={repr(self.name)}" +
            ")"
        )
