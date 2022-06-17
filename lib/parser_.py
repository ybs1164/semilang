from rply import ParserGenerator
from lib.ast_ import *


pg = ParserGenerator(
    ['NUMBER', 'IS', 'NEXTLINE', 'IDENTIFIER',
     'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE'],
    precedence=[
        ('right', ['IS']),
        ('left', ['PLUS', 'MINUS']),
        ('left', ['MULTIPLY', 'DIVIDE'])
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
        return Number(p[0].getstr())
    elif p[0].gettokentype() == 'IDENTIFIER':
        return Identifier(p[0].getstr())
    else:
        raise AssertionError('expr Error')

@pg.production('binop : PLUS')
@pg.production('binop : MINUS')
@pg.production('binop : MULTIPLY')
@pg.production('binop : DIVIDE')
def binop(p):
    return p[0]

@pg.production('expr : expr binop expr')
def expr_binop(p):
    left = p[0]
    right = p[2]
    if p[1].gettokentype() == 'PLUS':
        return Add(left, right)
    elif p[1].gettokentype() == 'MINUS':
        return Sub(left, right)
    elif p[1].gettokentype() == 'MULTIPLY':
        return Mul(left, right)
    elif p[1].gettokentype() == 'DIVIDE':
        return Div(left, right)
    else:
        raise AssertionError('binop Error')

@pg.error
def error_handler(token):
    raise ValueError("Ran into a %s where it wasn't expected" % token.gettokentype())

parser = pg.build()
