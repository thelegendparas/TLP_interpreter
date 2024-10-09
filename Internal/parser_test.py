import unittest
from TLP_lexer import Lexer
from TLP_parser import Parser
from TLP_AST import LetStatement,ReturnStatement , Statement, Program


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

        # Check for parsing errors
        self.check_parser_errors(parser)

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

    def test_return_statements(self):
        input_data = """
        return 5;
        return 10;
        return 141412431;
        """

        lexer = Lexer(input_data)
        parser = Parser(lexer)
        program = parser.parse_program()

        # Check for parsing errors
        self.check_parser_errors(parser)

        if len(program.statements) != 3:
            self.fail(f"program.statements does not contain 3 statements. got={len(program.statements)}")

        for stmt in program.statements:
            if not isinstance(stmt, ReturnStatement):
                self.fail(f"stmt not ReturnStatement. got={type(stmt)}")
                continue

            if stmt.token_literal() != "return":
                self.fail(f"return_stmt.token_literal not 'return', got {stmt.token_literal()}")

    def check_parser_errors(self, parser):
        """Check for errors in the parser and fail the test if any are found."""
        errors = parser.errors
        if len(errors) == 0:
            return  # no errors

        for msg in errors:
            self.fail(f"Parser error: {msg}")

        self.fail(f"Parser has {len(errors)} errors")

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
