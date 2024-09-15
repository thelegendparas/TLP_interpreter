#imports
from TLP_token import TokenType, Token, lookup_ident
from dataclasses import field


class Lexer:
    def __init__(self, input_string):
        self.input: str = input_string
        self.position: int = 0
        self.read_position: int = 0
        self.ch: str = field(default="", init=False)
        self.read_char()  # Initialise the first character

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

        # skip whitespace before processing the token
        self.skip_whitespace()

        # Identify if the current character is part of an identifier (Letter)
        if self.is_letter(self.ch):  # checks if current character is a letter
            literal = self.read_identifier()
            tok_type = lookup_ident(literal)
            return Token(type=tok_type, literal=literal)
        elif self.isDigit(self.ch):  # checks if current character is a digit
            tok_literal = self.readNumber()
            return Token(type=TokenType.INT, literal=tok_literal)

        if self.ch == '=':
            if self.peek_char() == "=":
                ch = self.ch
                self.read_char()
                tok = Token(type=TokenType.EQ, literal=ch + self.ch)
            else:
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
        elif self.ch == "-":
            tok = new_token(TokenType.MINUS, self.ch)
        elif self.ch == '{':
            tok = new_token(TokenType.LBRACE, self.ch)
        elif self.ch == '}':
            tok = new_token(TokenType.RBRACE, self.ch)
        elif self.ch == "!":
            if self.peek_char() == "=":
                ch = self.ch
                self.read_char()
                tok = Token(type=TokenType.NOT_EQ, literal=ch + self.ch)
            else:
                tok = new_token(TokenType.BANG, self.ch)
        elif self.ch == "/":
            tok = new_token(TokenType.SLASH, self.ch)
        elif self.ch == "*":
            tok = new_token(TokenType.ASTERISK, self.ch)
        elif self.ch == "<":
            tok = new_token(TokenType.LT, self.ch)
        elif self.ch == ">":
            tok = new_token(TokenType.GT, self.ch)
        elif self.ch == '\0':  # End of input
            tok = Token(type=TokenType.EOF, literal="")
        else:
            # Handle illegal characters
            tok = Token(type=TokenType.ILLEGAL, literal=self.ch)

        self.read_char()  # Move to the next character

        print(f"Next Token: {tok}")

        return tok

    def read_identifier(self):
        position = self.position
        while self.is_letter(self.ch):  # Continue reading while it's a letter
            self.read_char()
        return self.input[position:self.position]

    def readNumber(self):
        position = self.position
        while self.isDigit(self.ch):  # Continue reading while it's a number
            self.read_char()
        return self.input[position:self.position]

    def skip_whitespace(self):
        # Skips whitespaces like ' '  ,  '\t'  , '\n' ,  '\r'
        while self.ch in [' ', '\t', '\n', '\r']:
            self.read_char()

    def peek_char(self) -> str:
        if self.read_position >= len(self.input):
            return '\0'  # Null character to indicate end of target
        else:
            return self.input[self.read_position]

    @staticmethod
    def is_letter(ch):
        return "a" <= ch <= "z" or "A" <= ch <= "Z" or ch == "_"

    @staticmethod
    def isDigit(ch):
        return "0" <= ch <= "9"

    # This function returns True when ch is an english-letter and False when it is a non-letter

    @classmethod
    # the new() function creates an instance of Lexer
    # calls read_char() to initialize ch, position, and read_position, and then returns the instance.
    def new(cls, input_str):
        lexer_instance = Lexer(input_str)
        return lexer_instance


# Function to create a new token
def new_token(token_type, ch):
    return Token(type=token_type, literal=ch)
