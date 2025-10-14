from pytest import fixture
from mcpacker.format.tokenizer import Tokenizer

import textwrap

# Fixtures #########################################################################################

@fixture(name="basicJsonTokens")
def createBasicJson():
    yield Tokenizer(textwrap.dedent("""
        {
            "alpha": {
                "foxtrot": {
                    "bravo": "cha\\"rlie",
                    "delta": 12.123,
                    "echo": [
                        1, 2, 3
                    ]
                }
            },
            "golf hotel": {
                "juliette": false
            }
        }
    """).strip()).all()

@fixture(name="basicTomlTokens")
def createBasicToml():
    yield Tokenizer(textwrap.dedent("""
        [alpha.foxtrot]
        bravo = "cha\\"rlie"
        # comment
        delta = 12.123
        echo = [
            1, 2, 3
        ]

        ["golf hotel"]
        india = { juliette = false }
    """).strip()).all()

# Tests ############################################################################################

def test_basicJson(basicJsonTokens):
    assert list(str(t) for t in basicJsonTokens) == [
        'Token{name: open-brace, text: "{", line: 0}}',
        'Token{name: quoted-text, text: "alpha", line: 1}}',
        'Token{name: colon, text: ":", line: 1}}',
        'Token{name: open-brace, text: "{", line: 1}}',
        'Token{name: quoted-text, text: "foxtrot", line: 2}}',
        'Token{name: colon, text: ":", line: 2}}',
        'Token{name: open-brace, text: "{", line: 2}}',
        'Token{name: quoted-text, text: "bravo", line: 3}}',
        'Token{name: colon, text: ":", line: 3}}',
        'Token{name: quoted-text, text: "cha"rlie", line: 3}}',
        'Token{name: comma, text: ",", line: 3}}',
        'Token{name: quoted-text, text: "delta", line: 4}}',
        'Token{name: colon, text: ":", line: 4}}',
        'Token{name: float, text: "12.123", line: 4}}',
        'Token{name: comma, text: ",", line: 4}}',
        'Token{name: quoted-text, text: "echo", line: 5}}',
        'Token{name: colon, text: ":", line: 5}}',
        'Token{name: open-bracket, text: "[", line: 5}}',
        'Token{name: float, text: "1", line: 6}}',
        'Token{name: comma, text: ",", line: 6}}',
        'Token{name: float, text: "2", line: 6}}',
        'Token{name: comma, text: ",", line: 6}}',
        'Token{name: float, text: "3", line: 6}}',
        'Token{name: close-bracket, text: "]", line: 7}}',
        'Token{name: close-brace, text: "}", line: 8}}',
        'Token{name: close-brace, text: "}", line: 9}}',
        'Token{name: comma, text: ",", line: 9}}',
        'Token{name: quoted-text, text: "golf hotel", line: 10}}',
        'Token{name: colon, text: ":", line: 10}}',
        'Token{name: open-brace, text: "{", line: 10}}',
        'Token{name: quoted-text, text: "juliette", line: 11}}',
        'Token{name: colon, text: ":", line: 11}}',
        'Token{name: bool, text: "false", line: 11}}',
        'Token{name: close-brace, text: "}", line: 12}}',
        'Token{name: close-brace, text: "}", line: 13}}',
    ]

def test_basicToml(basicTomlTokens):
    assert list(str(t) for t in basicTomlTokens) == [
        'Token{name: open-bracket, text: "[", line: 0}}',
        'Token{name: identifier, text: "alpha", line: 0}}',
        'Token{name: period, text: ".", line: 0}}',
        'Token{name: identifier, text: "foxtrot", line: 0}}',
        'Token{name: close-bracket, text: "]", line: 0}}',
        'Token{name: identifier, text: "bravo", line: 1}}',
        'Token{name: equal, text: "=", line: 1}}',
        'Token{name: quoted-text, text: "cha"rlie", line: 1}}',
        'Token{name: comment, text: "comment", line: 2}}',
        'Token{name: identifier, text: "delta", line: 3}}',
        'Token{name: equal, text: "=", line: 3}}',
        'Token{name: float, text: "12.123", line: 3}}',
        'Token{name: identifier, text: "echo", line: 4}}',
        'Token{name: equal, text: "=", line: 4}}',
        'Token{name: open-bracket, text: "[", line: 4}}',
        'Token{name: float, text: "1", line: 5}}',
        'Token{name: comma, text: ",", line: 5}}',
        'Token{name: float, text: "2", line: 5}}',
        'Token{name: comma, text: ",", line: 5}}',
        'Token{name: float, text: "3", line: 5}}',
        'Token{name: close-bracket, text: "]", line: 6}}',
        'Token{name: open-bracket, text: "[", line: 8}}',
        'Token{name: quoted-text, text: "golf hotel", line: 8}}',
        'Token{name: close-bracket, text: "]", line: 8}}',
        'Token{name: identifier, text: "india", line: 9}}',
        'Token{name: equal, text: "=", line: 9}}',
        'Token{name: open-brace, text: "{", line: 9}}',
        'Token{name: identifier, text: "juliette", line: 9}}',
        'Token{name: equal, text: "=", line: 9}}',
        'Token{name: bool, text: "false", line: 9}}',
        'Token{name: close-brace, text: "}", line: 9}}',
    ]
