# Imports
import unittest
from TLP_token import Token, TokenType
from TLP_AST import Program, LetStatement, Identifier

class TestProgram(unittest.TestCase):
    def test_string(self):
        # Create tokens for the let statement
        let_token = Token(type=TokenType.LET, literal="let")
        my_var_token = Token(type=TokenType.IDENT, literal="myVar")
        another_var_token = Token(type=TokenType.IDENT, literal="anotherVar")

        # Create identifiers for 'myVar' and 'anotherVar'
        name = Identifier(token=my_var_token, value="myVar")
        value = Identifier(token=another_var_token, value="anotherVar")

        # Create the let statement and program
        let_statement = LetStatement(token=let_token, name=name, value= value)
        program = Program(statements=[let_statement])

        # Assert that the program string is correct
        expected_output = "let myVar = anotherVar;"
        self.assertEqual(str(program), expected_output, f"program.string() wrong. got = {str(program)}")

if __name__ == "__main__":
    unittest.main()