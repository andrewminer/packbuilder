from mcpacker.format.toml.model import TomlDocument
from mcpacker.format.toml.parser import TomlParser
from mcpacker.format.toml.composer import TomlComposer


# Class ############################################################################################

def dumps(document:TomlDocument) -> str:
    return str(TomlComposer(document).compose())

def loads(text:str) -> TomlDocument:
    return TomlParser(text).parse()
