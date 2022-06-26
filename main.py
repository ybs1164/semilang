from lib.lexer_ import lexer
from lib.parser_ import parser

from lib.trans_ import code

import pathlib

file_dir = "/cases/if_1.semi"

input_file = open(''.join([str(pathlib.Path().resolve()), file_dir]), 'r')
tokens = lexer.lex('\n'.join(input_file.readlines()))
input_file.close()

ast = parser.parse(tokens)

print(ast.getast())

print(code(ast))

file = open(''.join([str(pathlib.Path().resolve()), '/test.c']), 'w')
file.write(code(ast))
file.close()