from reader import Reader
from parsing import *
from interpreter import Interpreter

print('\npy-simple-parser. You can always type exit to finish execution\n')
while True:
    string = input('Type an expression to parse: ')
    if string == 'exit':
      break
    reader = Reader(string)
    tokens = reader.CreateTokens()
    parser = Parser(tokens)
    tree = parser.Parse()
    interpreter = Interpreter()
    res = interpreter.Calc(tree)

    print(f'''
    Tokens: {list(Reader(string).CreateTokens())}
    Tree: {tree}
    Result: {res}
    ''')

exit(1)