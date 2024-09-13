import unittest
from token import ASSIGN, PLUS, LPAREN, RPAREN, LBRACE, RBRACE, COMMA, SEMICOLON, EOF
from lexer import Lexer


class TestLexer(unittest.TestCase):

    def test_next_token(self):
        input_string = "=+(){},;"

        # list of expected tokens and their literal values
        tests = [
            (ASSIGN, "="),
            (PLUS, "+"),
            (LPAREN, "("),
            (RPAREN, ")"),
            (LBRACE, "{"),
            (RPAREN, "}"),
            (COMMA, ","),
            (SEMICOLON, ";"),
            (EOF, "")
            ]

        # Create a new Lexer with the input string
        lexer = Lexer(input_string)

        for i, (expected_type, expected_literal) in enumerate(tests):
            # Get the next token from the lexer
            token = lexer.next_token()

            #check if the literal value matches the expected literal
            self.assertEqual(token.type, expected_type,
                             f"tests[{i}] - tokentype wrong. expected={expected_type}, got={token.type}")

            self.assertEqual(token.literal, expected_literal,
                             f"tests[{i}] - literal wrong. expected={expected_literal}, got={token.literal}")


if __name__ == '__main__':
    unittest.main()
