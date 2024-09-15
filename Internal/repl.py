#imports
import sys
from TLP_lexer import Lexer
from TLP_token import TokenType

PROMPT = ">> "


def start():
    while True:
        try:
            # print the prompt and read input
            line = input(PROMPT)

            # Create lexer with the input line
            lexer = Lexer(line)

            # iterate over the tokens until EOF is encountered
            tok = lexer.next_token()
            while tok.type != TokenType.EOF:
                print(f"{tok}")
                tok = lexer.next_token()

        except (EOFError, KeyboardInterrupt):
            # handle EOF or keyboard interrupt gracefully
            print("\nExiting. . .")
            break


if __name__ == "__main__":
    start()
