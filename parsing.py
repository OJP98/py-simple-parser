from tokens import TokenType
from nodes import *


class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.Next()

    def Next(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def NewNumber(self):
        number = self.current_token

        if number.type == TokenType.LPAR:
            self.Next()
            result = self.Operation()
            if self.current_token.type != TokenType.RPAR:
                raise Exception('No right parenthesis for expression!')
            self.Next()
            return result

        if number.type == TokenType.NUMBER:
            self.Next()
            return Number(number.value)

    def NewTerm(self):
        result = self.NewNumber()

        while self.current_token != None and (self.current_token.type == TokenType.MULTIPLY or self.current_token.type == TokenType.DIVISION):
            ttype = self.current_token.type
            if ttype == TokenType.DIVISION:
                self.Next()
                result = Division(result, self.NewNumber())
            elif ttype == TokenType.MULTIPLY:
                self.Next()
                result = Multiplication(result, self.NewNumber())

        return result

    def Operation(self):
        result = self.NewTerm()

        while self.current_token != None and (self.current_token.type == TokenType.PLUS or self.current_token.type == TokenType.MINUS):
            ttype = self.current_token.type
            if ttype == TokenType.PLUS:
                self.Next()
                result = Addition(result, self.NewTerm())
            elif ttype == TokenType.MINUS:
                self.Next()
                result = Substraction(result, self.NewTerm())

        return result

    def Parse(self):
        if self.current_token == None:
            return None

        res = self.Operation()

        return res

