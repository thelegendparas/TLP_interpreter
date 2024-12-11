import unittest
from TLP_lexer import Lexer
from TLP_parser import Parser
from TLP_AST import LetStatement, ReturnStatement, Statement, Program, InfixExpression, ExpressionStatement


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

    def test_parsing_infix_expressions(self):
        infix_tests = [
            {"input": "5 + 5;", "leftValue": 5, "operator": "+", "rightValue": 5},
            {"input": "5 - 5;", "leftValue": 5, "operator": "-", "rightValue": 5},
            {"input": "5 * 5;", "leftValue": 5, "operator": "*", "rightValue": 5},
            {"input": "5 / 5;", "leftValue": 5, "operator": "/", "rightValue": 5},
            {"input": "5 > 5;", "leftValue": 5, "operator": ">", "rightValue": 5},
            {"input": "5 < 5;", "leftValue": 5, "operator": "<", "rightValue": 5},
            {"input": "5 == 5;", "leftValue": 5, "operator": "==", "rightValue": 5},
            {"input": "5 != 5;", "leftValue": 5, "operator": "!=", "rightValue": 5},
        ]

        for tt in infix_tests:
            lexer = Lexer(tt["input"]) # Create the lexer with input string
            parser = Parser(lexer) # Initialise parser with lexer
            program = parser.parse_program() # Parse the program
            self.check_parser_errors(parser) # Check for any parser errors

            # Check if program contains exactly one statement
            self.assertEqual(len(program.statements), 1, f"program.statements does not contain 1 statement. got={len(program.statements)}")

            stmt = program.statements[0]

            # Check if the statement is an ExpressionStatement
            self.assertIsInstance(stmt, ExpressionStatement, f"program.statements[0] is not ExpressionStatement. got={type(stmt)}")

            # Check if the expression is an infix statement
            exp = stmt.expression
            self.assertIsInstance(exp, InfixExpression, f"stmt.expression is not InfixExpression. got={type(stmt)}")

            # Check if the left side of the expression is an integer literal and matches the expected value
            self.validate_integer_literal(exp.left, tt["leftValue"])

            # Check if the operator is correct
            self.assertEqual(exp.operator, tt["operator"], f"exp.operator is not '{tt['operator']}'. got={exp.operator}")

            # Check if the right side of the expression is an integer literal and matches the expected value
            self.validate_integer_literal(exp.right, tt["rightValue"])

    def check_parser_errors(self, parser):
        """Check for errors in the parser and fail the test if any are found."""
        errors = parser.get_errors() if callable(parser.get_errors) else parser.get_errors
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

    def validate_integer_literal(self, exp, expected_value):
        # This function checks if the expression is an integer literal and matches the expected value
        self.assertEqual(exp.value, expected_value, f"exp.value is not {expected_value}. got={exp.value}")
        self.assertEqual(exp.token_literal(), str(expected_value), f"exp.token_literal is not {expected_value}. got={exp.token_literal()}")


if __name__ == '__main__':
    unittest.main()
