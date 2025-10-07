from mcpacker.emit.markdown.report import Report
from pytest import fixture


# Fixtures #########################################################################################

@fixture(name="report")
def createReport():
    return (
        Report("test", None)
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
    assert str(report) == "alphabravo\n  charlie\n    delta\n  echo"
