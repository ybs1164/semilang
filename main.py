from lib.lexer_ import Lexer
from lib.parser_ import Parser


example_code = "a = 1"

tokens = Lexer(example_code).run()
print(tokens)

ast = Parser(tokens)
