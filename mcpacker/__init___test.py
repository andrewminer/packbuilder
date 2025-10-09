import subprocess

####################################################################################################

def test_typeCompliance():
    command = [
        "mypy",
        #"--allow-untyped-defs",
        #"--follow-imports", "skip",
        #"--ignore-missing-imports",
        #"--no-check-untyped-defs",
        "--python-version", "3.10",
        "--show-error-codes",
        "mcpacker"
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)

    returncode = result.returncode
    assert returncode == 0


