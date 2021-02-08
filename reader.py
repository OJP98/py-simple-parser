from tokens import Token, TokenType


DIGITS = '0123456789'
SYMBOLS = '+-*/'


class Reader:
    def __init__(self, string: str):
        self.string = iter(string.replace(' ', ''))
        self.Next()

    def Next(self):
        try:
            self.current_char = next(self.string)
        except StopIteration:
            self.current_char = None

    def CreateTokens(self):
        while self.current_char != None:
            if self.current_char in DIGITS:
                yield self.GenerateNumber()
            elif self.current_char == '+':
                self.Next()
                yield Token(TokenType.PLUS, '+')
            elif self.current_char == '-':
                self.Next()
                yield Token(TokenType.MINUS, '-')
            elif self.current_char == '*':
                self.Next()
                yield Token(TokenType.MULTIPLY, '*')
            elif self.current_char == '/':
                self.Next()
                yield Token(TokenType.DIVISION, '/')
            elif self.current_char == '(':
                self.Next()
                yield Token(TokenType.LPAR)
            elif self.current_char == ')':
                self.Next()
                yield Token(TokenType.RPAR)
            else:
                raise Exception(f"Invalid character: '{self.current_char}'")

    def GenerateNumber(self):
        number = self.current_char
        self.Next()

        while self.current_char != None and self.current_char in DIGITS:
            number += self.current_char
            self.Next()

        return Token(TokenType.NUMBER, int(number))

    def Calculate(self, tokens):
        ops, result = [], [], []
        for token in tokens:
            if token.type == TokenType.NUMBER:
                result.append(token)
            elif token.value in SYMBOLS:
                while ops and token.precedence < ops[-1].precedence:
                    last = ops.pop()
                    result.append(last)
                ops.append(token)

        ops.reverse()
        result += ops
        print(result)
