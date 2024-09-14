#imports
from dataclasses import dataclass, field
from token import TokenType, Token


@dataclass
class Lexer:
    input: str
    position: int = 0
    read_position: int = 0
    ch: str = field(default="", init=False)

    def read_char(self):
        if self.read_position >= len(self.input):
            self.ch = '\0'
        else:
            self.ch = self.input[self.read_position]

        # incrementing all the string pointers
        self.position = self.read_position
        self.read_position += 1

    def next_token(self):
        tok = None

        if self.ch == '=':
            tok = new_token(TokenType.ASSIGN, self.ch)
        elif self.ch == ';':
            tok = new_token(TokenType.SEMICOLON, self.ch)
        elif self.ch == '(':
            tok = new_token(TokenType.LPAREN, self.ch)
        elif self.ch == ')':
            tok = new_token(TokenType.RPAREN, self.ch)
        elif self.ch == ',':
            tok = new_token(TokenType.COMMA, self.ch)
        elif self.ch == '+':
            tok = new_token(TokenType.PLUS, self.ch)
        elif self.ch == '{':
            tok = new_token(TokenType.LBRACE, self.ch)
        elif self.ch == '}':
            tok = new_token(TokenType.RBRACE, self.ch)
        elif self.ch == '\0':  # End of input
            tok = Token(type=TokenType.EOF, literal="")

        self.read_char()  # Move to the next character
        return tok

    @classmethod
    # the new() function creates an instance of Lexer
    # calls read_char() to initialize ch, position, and read_position, and then returns the instance.
    def new(cls, input_str):
        lexer_instance = Lexer(input_str)
        lexer_instance.read_char()
        return lexer_instance


def new_token(token_type, ch):
    return Token(type=token_type, literal=ch)
