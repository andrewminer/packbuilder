from typing import Protocol


# Type Support #####################################################################################

type JsonBlob = dict[str, "JsonBlob"] | list["JsonBlob"] | str | int | float | bool | None

class JsonBlobSource(Protocol):

    def asJsonBlob(self) -> JsonBlob:...


# Functions ########################################################################################

def removeNoneValues(blob:JsonBlob) -> JsonBlob:
    if isinstance(blob, dict):
        for key in list(blob.keys()):
            if blob[key] == None:
                del blob[key]
            else:
                blob[key] = removeNoneValues(blob[key])

    if isinstance(blob, list):
        result:list[JsonBlob] = []
        for value in blob:
            if value != None:
                result.append(removeNoneValues(value))

        return result

    return blob

def removeEmptyObjects(blob:JsonBlob) -> JsonBlob:
    if isinstance(blob, dict):
        for key in list(blob.keys()):
            value = blob[key]
            if isinstance(value, dict):
                if len(value) == 0:
                    del blob[key]
                else:
                    blob[key] = removeEmptyObjects(value)

        return blob

    if isinstance(blob, list):
        result:list[JsonBlob] = []
        for value in blob:
            if isinstance(value, dict):
                if len(value) > 0:
                    result.append(removeEmptyObjects(value))

        return result

    return blob
