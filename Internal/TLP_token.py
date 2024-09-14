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

