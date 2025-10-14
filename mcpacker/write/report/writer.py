from mcpacker.model.modpack import ModPack
from mcpacker.format.report.composer import ReportComposer
from mcpacker.write.writer import Writer
from pathlib import Path
from typing import Self


# Class ############################################################################################

class ReportWriter(Writer):

    def __init__(
        self,
        pack:ModPack,
        composerClass:type[ReportComposer],
        outputDir:Path,
        name:str|Path
    ):
        super().__init__(pack, outputDir)
        self.composerClass = composerClass
        self.name = Path(name)

    def doWrite(self) -> Self:
        path = self.locator.mcp_reports() / self.name
        self.resetOutputFile(path)

        composer = self.composerClass(self.pack)
        with path.open("w") as file:
            file.write(str(composer.compose()))

        return self
