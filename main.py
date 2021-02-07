from reader import Reader
from parsing import *

string = input('Type an expression to parse: ')
reader = Reader(string)
reader.Calculate()