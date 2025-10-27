from mcpacker.format.json import JsonBlob

import json as BaseJson


# Constants ########################################################################################

INDENT = "    "


# Functions ########################################################################################

def loads(text:str) -> JsonBlob:
    return BaseJson.loads(text)

def dumps(blob:JsonBlob):
    return BaseJson.dumps(blob, indent=INDENT)
