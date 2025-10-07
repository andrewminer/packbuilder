from tungston.generator.markdown.report import Report

import shutil
import os

# Class ############################################################################################

class ReportWriter:

    def __init__(self, reports:list[Report]):
        self._reports = reports

    def write(self, reportDirPath:str):
        if os.path.exists(reportDirPath):
            shutil.rmtree(reportDirPath)

        os.makedirs(reportDirPath, exist_ok=True)

        for report in self._reports:
            report.build()

            path = os.path.join(reportDirPath, report.name)
            with open(path, "w") as file:
                file.write(str(report))
