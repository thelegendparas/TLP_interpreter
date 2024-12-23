from abc import ABC, abstractmethod
from io import StringIO


class Node(ABC):
    @abstractmethod
    def token_literal(self) -> str:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class Statement(Node, ABC):
    @abstractmethod
    def statement_node(self):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class Expression(Node, ABC):
    @abstractmethod
    def expression_node(self):
        pass


class Program(Node):
    def __init__(self, statements=None):
        if statements is not None:
            self.statements = statements
        else:
            self.statements = []

    def token_literal(self) -> str:
        if len(self.statements) > 0:
            return self.statements[0].token_literal()
        else:
            return ""

    def __str__(self) -> str:
        out = StringIO()
        for statement in self.statements:
            out.write(str(statement))
        return out.getvalue()


class LetStatement(Statement):
    def __init__(self, token, name=None, value=None):
        self.token = token  # The token.LET token
        self.name = name  # An Identifier instance
        self.value = value  # An Expression instance

    def statement_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal  # Assuming the token has a "literal" attribute

    def __str__(self) -> str:
        out = StringIO()
        out.write(f"{self.token_literal()} ")
        out.write(str(self.name))
        out.write(" = ")
        if self.value is not None:
            out.write(str(self.value))
        out.write(";")
        return out.getvalue()


class Identifier(Expression):
    def __init__(self, token, value):
        self.token = token  # The token.IDENT token
        self.value = value  # The string value

    def expression_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal  # Assuming the token has a "literal" attribute

    def __str__(self) -> str:
        return str(self.value)


class ReturnStatement(Statement):
    def __init__(self, token, return_value=None):
        self.token = token  # The 'return' token
        self.return_value = return_value

    def statement_node(self):
        """Indicates that this is a statement node."""
        pass

    def token_literal(self) -> str:
        """Returns the literal value of the token."""
        return self.token.literal

    def __str__(self):
        out = StringIO()
        out.write(f"{self.token_literal()}")
        if self.return_value is not None:
            out.write(str(self.return_value))
        out.write(";")
        return out.getvalue()


class ExpressionStatement(Statement):
    def __init__(self, token, expression=None):
        self.token = token  # The first token of the expression
        self.expression = expression  # The expression instance

    def statement_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal  # Assuming the token has a 'literal' attribute

    def __str__(self):
        if self.expression is not None:
            return str(self.expression)
        return ""


class InfixExpression(Expression):
    """
    Represents an infix expression in the AST.
    Attributes:
        token: The infix token (eg , '+', '-', '*', etc.).
        left: The expression to the left of the operator.
        operator: The operator (eg , '+', '-', '*', etc.).
        right: The expression to the right of the operator
    """

    def __init__(self, token, left, operator, right=None):
        self.token = token
        self.left = left
        self.operator = operator
        self.right = right

    def expression_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal

    def __str__(self):
        """Return a string representation of the infix expression"""
        out = StringIO()
        out.write(f"({str(self.left)} {self.operator} {str(self.right)})")
        return out.getvalue()


class PrefixExpression(Expression):
    """
    Represents a prefix expression in the AST.

    Attributes:
        token: The prefix token (eg , '!', '-').
        operator: The operator (eg , '!', '-').
        right: The expression to the right of the operator.
    """

    def __init__(self, token, operator):
        self.token = token
        self.operator = operator
        self.right = None

    def expression_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal  # Assuming the token has a "literal" attribute

    def __str__(self) -> str:
        """Return a string representation of the prefix expression"""
        out = StringIO()
        out.write(f"({self.operator}{str(self.right)})")
        return out.getvalue()

class IntegerLiteral(Expression):

    def __init__(self, token, value):
        self.token = token
        self.value = value

    def expression_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal

    def __str__(self):
        return str(self.value)
