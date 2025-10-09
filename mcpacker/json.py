from json   import dump
from json   import dumps
from json   import load
from json   import loads
from typing import TypeAlias


# Type Support #####################################################################################

JsonBlob:TypeAlias = dict[str, "JsonBlob"] | list["JsonBlob"] | str | int | float | bool | None


# Functions ########################################################################################

def removeNoneValues(blob:JsonBlob) -> JsonBlob:
    if not isinstance(blob, dict): return blob

    for key in list(blob.keys()):
        if blob[key] == None:
            del blob[key]
        else:
            removeNoneValues(blob[key])

    return blob
