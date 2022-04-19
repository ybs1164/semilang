from lib.lexer_ import lexer
from lib.parser_ import parser


example_code = '''
a is 1
b is a + 1
'''

tokens = lexer.lex(example_code)

# print(list(lexer.lex(example_code)))

ast = parser.parse(tokens)

print(ast)
