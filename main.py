from _lexer import Lexer
from _parser import Parser


example_code = "a = 1"

tokens = Lexer(example_code).run()
print(tokens)

ast = Parser(tokens)
