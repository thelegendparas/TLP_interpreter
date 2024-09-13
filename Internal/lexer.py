#imports
from dataclasses import dataclass, field

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

        if self.ch == "="



    def new_token(token_type, ch):


    @classmethod
    # the new() function creates an instance of Lexer
    # calls read_char() to initialize ch, position, and read_position, and then returns the instance.
    def new(cls, input_str):
        lexer_instance = Lexer(input_str)
        lexer_instance.read_char()
        return lexer_instance

