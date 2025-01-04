from token import Token
from typing import List
from tokentype import TokenType
from lox import Lox

# our mapping of keywords
keywords = {
    "and": Token.AND,
    "class": Token.CLASS,
    "else": Token.ELSE,
    "false": Token.FALSE,
    "for": Token.FOR,
    "fun": Token.FUN,
    "if": Token.IF,
    "nil": Token.NIL,
    "or": Token.OR,
    "print": Token.PRINT,
    "return": Token.RETURN,
    "super": Token.SUPER,
    "this": Token.THIS,
    "true": Token.TRUE,
    "var": Token.VAR,
    "while": Token.WHILE,
}


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
            case "!":
                if self.match("="):
                    self.addToken(Token.BANG_EQUAL)
                else:
                    self.addToken(Token.BANG)
            case "=":
                if self.match("="):
                    self.addToken(Token.EQUAL_EQUAL)
                else:
                    self.addToken(Token.EQUAL)
            case "<":
                if self.match("<"):
                    self.addToken(Token.LESS_EQUAL)
                else:
                    self.addToken(Token.LESS)
            case ">":
                if self.match(">"):
                    self.addToken(Token.GREATER_EQUAL)
                else:
                    self.addToken(Token.GREATER)
            case "/":
                # bigger lexeme as commnets begin with / also
                if self.match("/"):
                    while self.peek() != "\n" and not self.isAtEnd():
                        self.advance()
                else:
                    self.addToken(Token.SLASH)
            # case ' ':
            # case '\r':
            # case '\t':
            # ignore whitespace
            case "\n":
                self.line += 1
            case '"':
                self.string()
            case _:
                if self.isDigit(c):
                    self.number()
                elif self.isAlpha(c):
                    self.identifier()
                else:
                    Lox.error(self.line, "Unexpected character.")

    def advance(self):
        self.current += 1
        return self.source[self.current]

    def addToken(self, type: TokenType, literal: object = None):
        text = self.source[self.start, self.current]
        self.tokens.append(Token(type, text, literal, self.line))

    def match(self, expected: str):
        if self.isAtEnd():
            return False
        if self.source[self.current] != expected:
            return False

        self.current += 1
        return True

    def peek(self):
        if self.isAtEnd():
            return "\0"
        return self.source[self.current]

    def string(self):
        while self.peek() != '"' and not self.isAtEnd():
            if self.peek() == "\n":
                self.line += 1
            self.advance()

        if self.isAtEnd():
            Lox.error(self.line, "Unterminated string.")
            return

        self.advance()

        ## trim surrounding quotes
        value = self.source[self.start + 1, self.current - 1]
        self.addToken(Token.STRING, value)

    def isDigit(self, c: str):
        return c >= "0" and c <= "9"

    def number(self):
        while self.isDigit(self.peek()):
            self.advance()

        # looking for a fractional part
        if self.peek() == "." and self.isDigit(self.peekNext()):
            # consume .
            self.advance()

        while self.isDigit(self.peek()):
            self.advance()

        self.addToken(float(self.source[self.start, self.current]))

    def peekNext(self):
        if (self.current + 1) >= len(self.source):
            return "\0"
        return self.source[self.current + 1]

    def identifier(self):
        while self.isAlphanumeric(self.peek()):
            self.advance()

        text = self.source[self.start, self.current]
        type = keywords.get(text)
        if not type:  # for none case
            type = Token.IDENTIFIER
        self.addToken(type)

    def isAlpha(self, c):
        return (c >= "a" and c <= "z") or (c >= "A" and c <= "Z") and (c == "_")

    def isAlpanumeric(self, c):
        return self.isAlpha(c) or self.isDigit(c)
