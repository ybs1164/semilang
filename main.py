from lexer import Lexer

example_code = "a = 1"

tokens = Lexer(example_code).run()

for i in tokens:
    print(str(i))