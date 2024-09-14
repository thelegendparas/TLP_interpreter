import unittest
from TLP_token import TokenType, Token
from TLP_lexer import Lexer


class TestLexer(unittest.TestCase):

    def test_next_token(self):
        input_string = """let five = 5;
            let ten = 10;
            let add = fn(x, y) {
            x + y;
            };
            let result = add(five, ten);
            """

        tests = [
            (TokenType.LET, "let"),
            (TokenType.IDENT, "five"),
            (TokenType.ASSIGN, "="),
            (TokenType.INT, "5"),
            (TokenType.SEMICOLON, ";"),
            (TokenType.LET, "let"),
            (TokenType.IDENT, "ten"),
            (TokenType.ASSIGN, "="),
            (TokenType.INT, "10"),
            (TokenType.SEMICOLON, ";"),
            (TokenType.LET, "let"),
            (TokenType.IDENT, "add"),
            (TokenType.ASSIGN, "="),
            (TokenType.FUNCTION, "fn"),
            (TokenType.LPAREN, "("),
            (TokenType.IDENT, "x"),
            (TokenType.COMMA, ","),
            (TokenType.IDENT, "y"),
            (TokenType.RPAREN, ")"),
            (TokenType.LBRACE, "{"),
            (TokenType.IDENT, "x"),
            (TokenType.PLUS, "+"),
            (TokenType.IDENT, "y"),
            (TokenType.SEMICOLON, ";"),
            (TokenType.RBRACE, "}"),
            (TokenType.SEMICOLON, ";"),
            (TokenType.LET, "let"),
            (TokenType.IDENT, "result"),
            (TokenType.ASSIGN, "="),
            (TokenType.IDENT, "add"),
            (TokenType.LPAREN, "("),
            (TokenType.IDENT, "five"),
            (TokenType.COMMA, ","),
            (TokenType.IDENT, "ten"),
            (TokenType.RPAREN, ")"),
            (TokenType.SEMICOLON, ";"),
            (TokenType.EOF, ""),
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
