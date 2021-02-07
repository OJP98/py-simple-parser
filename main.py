from algebra import Reader

string = input('Type an expression to parse: ')
reader = Reader(string)
reader.Calculate()
