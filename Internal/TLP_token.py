# Imports
from enum import Enum
from dataclasses import dataclass


class TokenType(Enum):
    ASSIGN = "="
    PLUS = "+"
    MINUS = "-"
    BANG = "!"
    ASTERISK = "*"
    SLASH = "/"
    EQ = "=="
    NOT_EQ = "!="

    SEMICOLON = ";"
    LPAREN = "{"
    RPAREN = "}"
    COMMA = ","
    LBRACE = "("
    RBRACE = ")"
    LT = "<"
    GT = ">"

    EOF = "\0"

    ILLEGAL = "ILLEGAL"
    INT = "INT"

    IDENT = "IDENT"
    FUNCTION = "fn"
    LET = "let"
    IF = "if"
    TRUE = "true"
    FALSE = "false"
    ELSE = "else"
    RETURN = "return"


@dataclass
class Token:
    type: TokenType
    literal: str


# Dictionary to store the keywords
keywords = {
    "fn": TokenType.FUNCTION,
    "let": TokenType.LET,
    "if": TokenType.IF,
    "return": TokenType.RETURN,
    "true": TokenType.TRUE,
    "false": TokenType.FALSE,
    "else": TokenType.ELSE

}


def lookup_ident(ident: str) -> TokenType:
    """
    If the identifier is found in the dictionary, returns the corresponding token type.
    If not, returns INDENT as the default token type.
    """
    return keywords.get(ident, TokenType.IDENT)
