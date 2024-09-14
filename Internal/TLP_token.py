# Imports
from enum import Enum
from dataclasses import dataclass


class TokenType(Enum):
    ASSIGN = "ASSIGN"
    SEMICOLON = "SEMICOLON"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    COMMA = "COMMA"
    PLUS = "PLUS"
    LBRACE = "LBRACE"
    RBRACE = "RBRACE"
    EOF = "EOF"
    ILLEGAL = "ILLEGAL"
    IDENT = "IDENT"
    INT = "INT"
    FUNCTION = "FUNCTION"
    LET = "LET"


@dataclass
class Token:
    type: TokenType
    literal: str


# Dictionary to store the keywords
keywords = {
    "fn": TokenType.FUNCTION,
    "let": TokenType.LET,
}

def lookup_ident(ident: str) -> TokenType:
    """
    If the identifier is found in the dictionary, returns the corresponding token type.
    If not, returns INDENT as the default token type.
    """
    return keywords.get(ident, TokenType.IDENT)