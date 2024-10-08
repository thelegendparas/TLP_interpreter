from abc import ABC, abstractmethod


class Node(ABC):
    @abstractmethod
    def token_literal(self) -> str:
        pass


class Statement(Node, ABC):
    @abstractmethod
    def statement_node(self):
        pass


class Expression(Node, ABC):
    @abstractmethod
    def expression_node(self):
        pass


class Program(Node):
    def __init__(self):
        self.statements = []

    def token_literal(self) -> str:
        if len(self.statements) > 0:
            return self.statements[0].token_literal()
        else:
            return ""


class LetStatement(Statement):
    def __init__(self, token, name=None, value=None):
        self.token = token  # The token.LET token
        self.name = name  # An Identifier instance
        self.value = value  # An Expression instance

    def statement_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal  # Assuming the token has a "literal" attribute


class Identifier(Expression):
    def __init__(self, token, value):
        self.token = token  # The token.IDENT token
        self.value = value  # The string value

    def expression_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal  # Assuming the token has a "literal" attribute
