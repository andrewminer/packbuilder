from pytest import fixture
from tungston.generator.markdown.report import Report


# Fixtures #########################################################################################

@fixture(name="emptyReport")
def createEmptyReport():
    return Report()

@fixture(name="report")
def createReport():
    return (
        Report(None)
            .text("alpha")
            .line("bravo")
            .indent()
            .line("charlie")
            .indent()
            .line("delta")
            .outdent()
            .line("echo")
    )

# Tests ############################################################################################

def test_repr(report):
    assert repr(report) == "Report{lines: 4 lines, lineBuffer: 1 chunks, indent: 1}"

def test_str(report):
    assert str(report) == "alphabravo\n    charlie\n        delta\n    echo"
