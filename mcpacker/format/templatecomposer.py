from collections.abc import Mapping
from mcpacker.format.composer import Composer


# Class ############################################################################################

class TemplateComposer(Composer):

    def __init__(self, template:str):
        self._template = template
        self._text:str|None = None

    def __str__(self) -> str:
        if not self._text: raise RuntimeError("must call compose before str")
        return self._text

    def doCompose(self):
        self._text = self._template.format(**self.gatherData())

    def gatherData(self) -> Mapping[str,str]:
        raise NotImplementedError()
