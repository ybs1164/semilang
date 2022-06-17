from lib.lexer_ import lexer
from lib.parser_ import parser


example_code = '''
a is 1
b is 2 + 1 * 3
'''

example_code_2 = '''
a is 1
if a > 10 then
    print 1*2
else
    print 1+2
end
'''

tokens = lexer.lex(example_code)

print(list(lexer.lex(example_code)))

ast = parser.parse(tokens)

print(ast.getast())
