import unittest
from TLP_lexer import Lexer
from TLP_parser import Parser
from TLP_AST import LetStatement, Statement, Program


class TestParser(unittest.TestCase):
    def test_let_statements(self):
        input_data = """
        let x = 5;
        let y = 10;
        let foobar = 838383
        """

        lexer = Lexer(input_data)  # Intialize the lexer with the input data
        parser = Parser(lexer)  # Initialize the parser with lexer
        program = parser.parse_program()  # parse the program

        # Check if the program is not None
        if program is None:
            self.fail("parse_program() returned None")

        # check if the program contains 3 statements
        self.assertEqual(len(program.statements), 3,
                         f"program.statements does not contain 3 statements. got={len(program.statements)}")

        tests = [
            {"expectedIdentifier": "x"},
            {"expectedIdentifier": "y"},
            {"expectedIdentifier": "foobar"},
        ]

        for i, test in enumerate(tests):
            stmt = program.statements[i]
            if not self.validate_let_statement(stmt, test["expectedIdentifier"]):
                return

    def validate_let_statement(self, stmt, expected_name):
        if stmt.token_literal() != "let":
            self.fail(f"s.token_literal not 'let'. got={stmt.token_literal()}")

        if not isinstance(stmt, LetStatement):
            self.fail(f"s not ast.LetStatement. got={type(stmt)}")

        if stmt.name.value != expected_name:
            self.fail(f"let_stmt.name.value not '{expected_name}'. got={stmt.name.value}")

        if stmt.name.token.literal != expected_name:
            self.fail(f"s.name not '{expected_name}'. got={stmt.name}")

        return True


if __name__ == '__main__':
    unittest.main()
