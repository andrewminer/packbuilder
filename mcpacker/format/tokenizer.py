from collections.abc import Generator
from collections.abc import Iterable
from typing import Any


# Helper Classes ###################################################################################

class Token:

    def __init__(self, name:str, text:str, line:int):
        self.name = name
        self.line = line
        self.text = text

    def __repr__(self) -> str:
        return (
            f"Token{{" +
                f"name: {self.name}, " +
                f"text: \"{self.text}\", " +
                f"line: {self.line}" +
            "}}"
        )

class TokenizationError(Exception):

    def __init__(self, message:str, line:int):
        self.message = message
        self.line = line

    def __str__(self) -> str:
        return f"TokenizationError:{self.line}: {self.message}"


# Constants ########################################################################################

DIGIT_SET = "0123456789"
IDENTIFIER_SET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
SIGN_SET = "-+"


# Class ############################################################################################

class Tokenizer:

    def __init__(
        self,
        text:str,
        skipWhitespace:bool=True,
        comment:str="#",
        escape:str="\\",
        quotes:str="'\"",
    ):
        self._comment = comment
        self._current = 0
        self._line = 0
        self._escape = escape
        self._quotes = quotes
        self._returnedTokens:list[Token] = []
        self._skipWhitespace = skipWhitespace
        self._text = text

    def all(self) -> Iterable[Token]:
        result = []
        while self.peek().name != "eof":
            result.append(self.next())

        return result

    def isFinished(self) -> bool:
        return self._current >= len(self._text)

    def next(self) -> Token:
        while True:
            if self._returnedTokens:
                token = self._returnedTokens.pop()
                return token

            if self.isFinished():
                token = Token("eof", "", self._line)
                return token

            token = (
                # order matters here: some tokens are subsets of other tokens, and must appear
                # later in the list to avoid mistakes (e.g., bool/indentifier, float/int)
                self._scanLetterSequence("open-paren", "(") or
                self._scanLetterSequence("close-paren", ")") or
                self._scanLetterSequence("open-brace", "{") or
                self._scanLetterSequence("close-brace", "}") or
                self._scanLetterSequence("open-bracket", "[") or
                self._scanLetterSequence("close-bracket", "]") or
                self._scanLetterSequence("period", ".") or
                self._scanLetterSequence("comma", ",") or
                self._scanLetterSequence("equal", "=") or
                self._scanLetterSequence("colon", ":") or
                self._scanLetterSequence("bool", "false") or
                self._scanLetterSequence("bool", "true") or
                self._scanLetterSet("whitespace", " \t") or
                self._scanLetterSet("newline", "\r\n") or
                self._scanFloat() or
                self._scanBase10Int() or
                self._scanIdentifier() or
                self._scanQuotedText() or
                self._scanLineComment() or
                self._scanOther()
            )

            if (token.name in ["whitespace", "newline"]) and self._skipWhitespace:
                continue

            return token

    def peek(self) -> Token:
        token = self.next()
        self.reject(token)

        return token

    def reject(self, token:Token):
        self._returnedTokens.append(token)

    # Private Methods ##########################################################

    def _currentChar(self) -> str:
        if self._current >= len(self._text): return ""
        return self._text[self._current]

    def _nextLetter(self) -> int:
        if self._current < len(self._text):
            if self._currentChar() == "\n":
                self._line += 1
            self._current += 1

        return self._current

    def _scanBase10Int(self) -> Token|None:
        start = self._current
        char = self._currentChar()
        if char in SIGN_SET:
            self._nextLetter() # skip sign
            char = self._currentChar()

        if char not in DIGIT_SET: return None

        while self._currentChar() in DIGIT_SET:
            self._nextLetter()

        return Token("int", self._text[start:self._current], self._line)

    def _scanFloat(self) -> Token|None:
        start = self._current
        char = self._currentChar()
        if char in SIGN_SET:
            self._nextLetter() # skip sign
            char = self._currentChar()

        if char not in DIGIT_SET: return None

        while self._currentChar() in DIGIT_SET:
            self._nextLetter()

        if self._currentChar() != ".":
            return Token("float", self._text[start:self._current], self._line)

        self._nextLetter() # skip '.'

        while self._currentChar() in DIGIT_SET:
            self._nextLetter()

        if self._currentChar() != "e":
            return Token("float", self._text[start:self._current], self._line)

        self._nextLetter() # skip 'e'
        if char in SIGN_SET:
            self._nextLetter() # skip sign
            char = self._currentChar()

        while self._currentChar() in DIGIT_SET:
            self._nextLetter()

        return Token("float", self._text[start:self._current], self._line)

    def _scanIdentifier(self) -> Token|None:
        if self._currentChar() not in IDENTIFIER_SET: return None
        start = self._current

        while self._currentChar() in IDENTIFIER_SET:
            self._nextLetter()

        return Token("identifier", self._text[start:self._current], self._line)

    def _scanLetterSequence(self, name:str, text:str) -> Token|None:
        start = self._current
        for char in text:
            if self._currentChar() != char:
                self._current = start
                return None

            self._nextLetter()

        return Token(name, self._text[start:self._current], self._line)

    def _scanLetterSet(self, name:str, letters:str) -> Token|None:
        if self._currentChar() not in letters: return None

        start = self._current
        while self._currentChar() in letters:
            self._nextLetter()

        return Token(name, self._text[start:self._current], self._line)

    def _scanLineComment(self) -> Token|None:
        if self._currentChar() != self._comment: return None
        self._nextLetter() # skip comment char
        while self._currentChar() in " \t":
            self._nextLetter()

        start = self._current
        while self._currentChar() != "\n":
            self._nextLetter()

        return Token("comment", self._text[start:self._current], self._line)

    def _scanOther(self) -> Token:
        start = self._current
        self._nextLetter()
        return Token("other", self._text[start:self._current], self._line)

    def _scanQuotedText(self) -> Token|None:
        startChar = self._currentChar()
        if startChar not in self._quotes: return None

        self._nextLetter() # skip starting quote
        start = self._current

        chars:list[str] = []
        while True:
            char = self._currentChar()
            if char == self._escape:
                self._nextLetter() # skip escape char
                chars.append(self._currentChar())
                self._nextLetter() # skip following char
                char = self._currentChar()

            if char == "":
                raise TokenizationError(f"Expected {startChar}, but found end of text", self._line)

            if char == startChar:
                token = Token("quoted-text", "".join(chars), self._line)
                self._nextLetter() # skip final quote
                return token

            chars.append(char)

            self._nextLetter()
