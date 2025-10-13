import subprocess

####################################################################################################

def test_typeCompliance():
    command = [
        "./.venv/bin/mypy",
        "--check-untyped-defs",
        "--python-version", "3.13",
        "--show-error-codes",
        "mcpacker"
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)

    returncode = result.returncode
    assert returncode == 0


