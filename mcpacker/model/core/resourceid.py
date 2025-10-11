from collections.abc import Callable


# Class ############################################################################################

class ResourceId:

    @staticmethod
    def alterName(text:str, doTransform:Callable[[str],str]) -> str:
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

    def __str__(self) -> str:
        if not self.isTag:
            return f"{self.mod}:{self.name}"

        return f"#{self.mod}:{self.name}"

    def __repr__(self) -> str:
        return "".join([str(p) for p in [
            "ResourceId{",
                "isTag: ", ("True" if self.isTag else "False"), ", ",
                "mod: ", self.mod, ", ",
                "name: ", self.name,
            "}"
        ]])
