from TLP_lexer import Lexer
from TLP_token import Token, TokenType
from TLP_AST import Program, Statement, LetStatement, Identifier


class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer  # The Lexer instance
        self.cur_token = None
        self.peek_token = None

        # Read two tokens so cur_token and peek_token are both set
        self.next_token()
        self.next_token()

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

        else:
            return None  # Return None if the token type is not recognised

    def parse_let_statement(self):
        """Parses a 'Let' statement."""
        stmt = LetStatement(token=self.cur_token)  # Create a LetStatement object

        if not self.expect_peek(TokenType.IDENT):
            return None

        stmt.name = Identifier(token=self.cur_token, value=self.cur_token.literal)

        if not self.expect_peek(TokenType.ASSIGN):
            return None

        # TODO: Skipping the expressions until we encounter a semicolon
        while not self.cur_token_is(TokenType.SEMICOLON) and not self.cur_token_is(TokenType.EOF):
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
            self.next_token() # Advance to the next token
            return True
        else:
            return False

