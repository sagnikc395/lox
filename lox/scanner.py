from token import Token
from typing import List
from tokentype import TokenType


class Scanner:
    tokens: List[Token]
    current: int = 0
    start: int = 0
    line: int = 1

    def __init__(self, source: str):
        self.source = source

    def scanTokens(self):
        while not self.isAtEnd():
            Scanner.start = Scanner.current
            self.scan_token()

        Scanner.tokens.append(Token(Token.EOF, "", None, Scanner.line))
        return Scanner.tokens

    def scan_token(self):
        pass

    def isAtEnd(self):
        return Scanner.current >= len(self.source)

    def scanToken(self):
        c = self.advance()
        match c:
            case "(":
                self.addToken(Token.LEFT_PAREN)
            case ")":
                self.addToken(Token.RIGHT_PAREN)
            case "{":
                self.addToken(Token.LEFT_BRACE)
            case "}":
                self.addToken(Token.RIGHT_BRACE)
            case ",":
                self.addToken(Token.COMMA)
            case ".":
                self.addToken(Token.DOT)
            case "-":
                self.addToken(Token.MINUS)
            case "+":
                self.addToken(Token.PLUS)
            case ";":
                self.addToken(Token.SEMICOLON)
            case "*":
                self.addToken(Token.STAR)

    def advance(self):
        self.current += 1
        return self.source[self.current]

    def addToken(self, type: TokenType, literal: object = None):
        text = self.source[self.start, self.current]
        self.tokens.append(Token(type, text, literal, self.line))
