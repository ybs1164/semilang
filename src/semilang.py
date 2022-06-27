# pretty_errors can be turned off by commenting
import pretty_errors

from lib.lexer_ import lexer
from lib.parser_ import parser
from lib.trans_ import code

import argparse
from os import system
import pathlib

def start():

  me = "./semilang"

  argparser = argparse.ArgumentParser(description="Semilang transcompiler")
  argparser.add_argument('-s',
                      type=str,
                      help=me + " ... -s foo.semi ; 컴파일 할 대상을 결정합니다",
                      default=''.join([str(pathlib.Path().resolve()), "/cases/if_1.semi"])
                      )
  argparser.add_argument('-S',
                      type=bool,
                      help=me + " -S ... ; 트랜스 컴파일 한 .c 파일을 쓸지 결정합니다",
                      action=argparse.BooleanOptionalAction
                      )
  argparser.set_defaults(S=False)
  argparser.add_argument('-o',
                      type=str,
                      help=me + " ... -o bar ; 컴파일한 실행 가능한 프로그램의 위치를 결정합니다",
                      default="",
                      action=argparse.BooleanOptionalAction
                      )

  args = argparser.parse_args()
  file_dir = args.s

  input_file = open(file_dir, 'r')
  create_c_file: bool = args.S
  output_file_path = args.o

  tokens = lexer.lex('\n'.join(input_file.readlines()))
  input_file.close()

  ast = parser.parse(tokens)

  # TODO: parse -v(verbose) option
  print(ast.getast())

  generated_c_code = code(ast)
  generated_c_path = ''.join([str(pathlib.Path().resolve()), '/test.c'])

  print(generated_c_code)

  # due to the asynchronous of file.write() method,
  # we should wait til the writing process is done.
  # file.close() method might be the solution,
  # and it's called implicitly at the end of the with statement.
  with open(generated_c_path, 'w') as file:
    file.write(generated_c_code)

  if output_file_path:
    system('cc ' + generated_c_path + ' -o ' + output_file_path)
  else:
    system('cc -o semi.out ' + generated_c_path)

  if not create_c_file:
    system('rm -f ' + generated_c_path)