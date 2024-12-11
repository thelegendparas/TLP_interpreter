#imports
from typing import Callable, Dict, List

from TLP_lexer import Lexer
from TLP_token import Token, TokenType
from TLP_AST import Program, Statement, LetStatement, ReturnStatement, Identifier, PrefixExpression, \
    ExpressionStatement, InfixExpression, IntegerLiteral

# Define prefixParseFn as a callable that returns an ast.Expression
prefixParseFn = Callable[[], 'Expression']

# Define infixParseFn as a callable that takes an ast.Expression and returns an ast.Expression
infixParseFn = Callable[['Expression'], 'Expression']

# precedence table for the different types of operators
LOWEST = 1
EQUALS = 2  # ==
LESSGREATER = 3  # > OR <
SUM = 4  # +
PRODUCT = 5  # *
PREFIX = 6  # -X or !X
CALL = 7  # myFunction(X)

# Precedence lookup table
precedences = {
    TokenType.EQ: EQUALS,
    TokenType.NOT_EQ: EQUALS,
    TokenType.LT: LESSGREATER,
    TokenType.GT: LESSGREATER,
    TokenType.PLUS: SUM,
    TokenType.MINUS: SUM,
    TokenType.SLASH: PRODUCT,
    TokenType.ASTERISK: PRODUCT,
    TokenType.LPAREN: CALL

}


class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer  # The Lexer instance
        self.cur_token = None
        self.peek_token = None

        self.prefixParseFns: Dict[TokenType, prefixParseFn] = {}  # Mapping of token types to prefix functions
        self.infixParseFns: Dict[TokenType, infixParseFn] = {}  # Mapping of token types to infix functions
        self.errors = []  # List to store parser errors

        # Read two tokens so cur_token and peek_token are both set
        self.next_token()
        self.next_token()

        # Register prefix functions for BANG and MINUS
        self.register_prefix(TokenType.BANG, self.parse_prefix_expression)
        self.register_prefix(TokenType.MINUS, self.parse_prefix_expression)
        self.register_prefix(TokenType.INT, self.parse_integer_literal)

        # Register infix parsers
        self.register_infix(TokenType.PLUS, self.parse_infix_expression)
        self.register_infix(TokenType.MINUS, self.parse_infix_expression)
        self.register_infix(TokenType.SLASH, self.parse_infix_expression)
        self.register_infix(TokenType.ASTERISK, self.parse_infix_expression)
        self.register_infix(TokenType.GT, self.parse_infix_expression)
        self.register_infix(TokenType.LT, self.parse_infix_expression)
        self.register_infix(TokenType.EQ, self.parse_infix_expression)
        self.register_infix(TokenType.NOT_EQ, self.parse_infix_expression)

    def get_errors(self):
        """Returns the list of parser errors."""
        return self.errors

    def peek_error(self, token_type):
        """Logs an error when the next token is not of the expected type"""
        msg = f"expected next token to be {token_type}, got {self.peek_token.type} instead"
        self.errors.append(msg)

    def next_token(self):
        """Advance Tokens: cur_token becomes peek_token and peek_token becomes the next token from the lexer"""
        self.cur_token = self.peek_token
        self.peek_token = self.lexer.next_token()

    def parse_program(self):
        program = Program()  # Create a new Program instance
        program.statements = []  # Initialize the statement list

        # loop until the current token type is EOF
        while self.cur_token.type != TokenType.EOF:
            stmt = self.parse_statement()  # Parse a Statement
            if stmt is not None:
                program.statements.append(stmt)  # Add the statement to the list
            self.next_token()  # Move to the next token

        return program  # Return the populated Program instance

    def parse_statement(self) -> Statement:
        """Parses a statement based on the current type of token type."""
        if self.cur_token.type == TokenType.LET:
            return self.parse_let_statement()  # Parse a let statement
        elif self.cur_token.type == TokenType.RETURN:
            return self.parse_return_statement()

        else:
            return self.parse_expression_statement()  # Handle general expressions

    def parse_expression_statement(self):
        stmt = ExpressionStatement(token=self.cur_token)
        stmt.expression = self.parse_expression(LOWEST)
        if self.peek_token_is(TokenType.SEMICOLON):
            self.next_token()
        return stmt

    def parse_let_statement(self):
        """Parses a 'Let' statement."""
        stmt = LetStatement(token=self.cur_token)  # Create a LetStatement object

        if not self.expect_peek(TokenType.IDENT):
            return None

        stmt.name = Identifier(token=self.cur_token, value=self.cur_token.literal)

        if not self.expect_peek(TokenType.ASSIGN):
            return None

        self.next_token() # Move to the expression
        stmt.value = self.parse_expression(LOWEST) # Parse the expression

        if self.peek_token_is(TokenType.SEMICOLON):
            self.next_token()

        return stmt

    def parse_return_statement(self):
        """Parses a return statement"""
        stmt = ReturnStatement(token=self.cur_token)
        self.next_token()

        stmt.return_value = self.parse_expression(LOWEST)

        if self.peek_token_is(TokenType.SEMICOLON):
            self.next_token()

        return stmt

    def cur_token_is(self, token_type):
        """Checks if the current token matches a given type."""
        return self.cur_token.type == token_type

    def peek_token_is(self, token_type):
        """Checks if the next(peek) token matches a given type"""
        return self.peek_token.type == token_type

    def expect_peek(self, token_type):
        """Advances the token if the next token matches the expected type, return False otherwise"""
        if self.peek_token_is(token_type):
            self.next_token()  # Advance to the next token
            return True
        else:
            self.peek_error(token_type)
            return False

    def register_prefix(self, token_type: TokenType, fn: prefixParseFn) -> None:
        """
        Registers a prefix parsing function for the given token type.

        :param token_type: The type of token  for which the prefix function is being registered.
        :param fn: The prefix parsing function to register
        """
        self.prefixParseFns[token_type] = fn

    def register_infix(self, token_type: TokenType, fn: infixParseFn) -> None:
        """
        Registers an infix parsing function for the given token type.

        :param token_type: The type of token for which the infix function is being registered.
        :param fn: The infix parsing function to register
        :return:
        """
        self.infixParseFns[token_type] = fn

    def no_prefix_parse_fn_error(self, token_type: TokenType):
        """Logs an error when no prefix parse function is found for a token type."""
        msg = f"no prefix parse function for {token_type} found"
        self.errors.append(msg)

    def peek_precedence(self):
        return precedences.get(self.peek_token.type, LOWEST)

    def cur_precedence(self):
        return precedences.get(self.cur_token.type, LOWEST)

    def parse_expression(self, precedence):
        """

        Parses an expression based on precedence

        :param precedence: The current precedence level
        :return: An Expression object or None if no prefix parse function is found
        """
        prefix = self.prefixParseFns.get(self.cur_token.type)
        if prefix is None:
            self.no_prefix_parse_fn_error(self.cur_token.type)
            return None

        left_exp = prefix()

        while not self.peek_token_is(TokenType.SEMICOLON) and precedence < self.peek_precedence():
            infix = self.infixParseFns.get(self.peek_token.type)
            if infix is None:
                return left_exp

            self.next_token()
            left_exp = infix(left_exp)

        return left_exp

    def parse_prefix_expression(self):
        """Parses a prefix expression."""
        expression = PrefixExpression(
            token=self.cur_token,
            operator=self.cur_token.literal
        )
        self.next_token()

        expression.right = self.parse_expression(PREFIX)  # Parse the right side of the expression
        return expression

    def parse_infix_expression(self, left):
        expression = InfixExpression(
            token=self.cur_token,
            operator=self.cur_token.literal,
            left=left
        )
        precedence = self.cur_precedence()
        self.next_token()
        expression.right = self.parse_expression(precedence)
        return expression

    def parse_integer_literal(self):
        try:
            value = int(self.cur_token.literal)
        except ValueError:
            msg = f"could not parse{self.cur_token.literal} as integer"
            self.errors.append(msg)
            return None
        return IntegerLiteral(token=self.cur_token, value=value)