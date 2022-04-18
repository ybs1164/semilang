from rply import ParserGenerator
from lib.ast_ import *


pg = ParserGenerator(
    ['NUMBER', 'IS', 'NEXTLINE', 'IDENTIFIER'],
    precedence=[
        ('right', ['IS'])
    ]
)

@pg.production('block : block stat')
def block_next(p):
    term = p[0].getbodys()
    term.append(p[1])
    return Block(term)

@pg.production('block : stat')
def block_next(p):
    return Block([p[0]])

@pg.production('stat : define NEXTLINE')
@pg.production('stat : define')
def stat(p):
    return p[0]

@pg.production('define : IDENTIFIER IS expr')
def define(p):
    return Define(Identifier(p[0].getstr()), p[2])

@pg.production('expr : NUMBER')
@pg.production('expr : IDENTIFIER')
def expr_num(p):
    if p[0].gettokentype() == 'NUMBER':
        return Number(int(p[0].getstr()))
    elif p[0].gettokentype() == 'IDENTIFIER':
        return Identifier(p[0].getstr())
    else:
        raise AssertionError('expr Error')

@pg.error
def error_handler(token):
    raise ValueError("Ran into a %s where it wasn't expected" % token.gettokentype())

parser = pg.build()
