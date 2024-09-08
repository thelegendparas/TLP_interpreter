# Imports
from dataclasses import dataclass


# Why do this?
# The TokenType class doesn't add any new behavior to a string.
# It’s simply a way to make the code clearer. When we use TokenType,
# It tells us that this string is meant to represent the "type" of a token (like "keyword", "identifier", etc.).
class TokenType(str):
    pass


# @dataclass: This decorator automatically generates the __init__, __repr__,
# and other common methods (like __eq__) for the Token class.
@dataclass
class Token:
    type: TokenType
    literal: str


# There will be only a limited number of defined token types in our language

# Special Tokens
ILLEGAL = "ILLEGAL"  # ILLEGAL signifies a token/character we don’t know about
EOF = "EOF"  # EOF stands for “end of file”

# Identifiers and literals
IDENT = "IDENT"  # e.g., add, foobar, x, y, ...
INT = "INT"

# Operators
ASSIGN = "="
PLUS = "+"

# Delimiters
COMMA = ","
SEMICOLON = ";"
LPAREN = "("
RPAREN = ")"
LBRACE = "{"
RBRACE = "}"

# Keywords
FUNCTION = "FUNCTION"
LET = "LET"


