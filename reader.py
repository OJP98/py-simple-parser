from tokens import Token, TokenType


DIGITS = '0123456789'
SYMBOLS = '+-*/'


class Reader:
    def __init__(self, string: str):
        self.string = iter(string.replace(' ', ''))
        self.Next()

    def Next(self):
        try:
            self.curr_char = next(self.string)
        except StopIteration:
            self.curr_char = None

    def CreateTokens(self):
        while self.curr_char != None:
            if self.curr_char in DIGITS:
                yield self.CreateNumber()
            elif self.curr_char == '+':
                self.Next()
                yield Token(TokenType.PLUS, '+')
            elif self.curr_char == '-':
                self.Next()
                yield Token(TokenType.MINUS, '-')
            elif self.curr_char == '*':
                self.Next()
                yield Token(TokenType.MULTIPLY, '*')
            elif self.curr_char == '/':
                self.Next()
                yield Token(TokenType.DIVISION, '/')
            elif self.curr_char == '(':
                self.Next()
                yield Token(TokenType.LPAR)
            elif self.curr_char == ')':
                self.Next()
                yield Token(TokenType.RPAR)
            else:
                raise Exception(f"Invalid character: '{self.current_char}'")

    def CreateNumber(self):
        number = self.curr_char
        self.Next()

        while self.curr_char != None and self.curr_char in DIGITS:
            number += self.curr_char
            self.Next()

        return Token(TokenType.NUMBER, int(number))

    def Calculate(self, tokens):
        ops, result = [], []
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
