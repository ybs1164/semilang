from lib.lexer_ import lexer
from lib.parser_ import parser


example_code = "a = 1"

tokens = lexer.lex(example_code)

for token in tokens:
    print(token)

ast = parser.parse(tokens)

print(ast)
