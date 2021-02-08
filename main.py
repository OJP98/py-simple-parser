from reader import Reader
from parsing import *

string = input('Type an expression to parse: ')
reader = Reader(string)
tokens = reader.GenerateTokens()
parser = Parser(tokens)
tree = parser.Parse()
print(tree)

