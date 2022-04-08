from lib.lexer_ import l
from lib.parser_ import Parser


example_code = "a = 1"

tokens = l.lex(example_code)

for token in tokens:
    print(token)

