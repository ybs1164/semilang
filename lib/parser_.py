from rply import ParserGenerator
from lib.ast_ import *


pg = ParserGenerator(
    ['NUMBER', 'IDENTIFIER',
     'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE',
     'IS', 'PRINT', 'IF', 'THEN', 'ELSE', 'END',
     'LT', 'GT'],
    precedence=[
        ('right', ['IS', 'PRINT', 'IF']),
        ('left', ['LT', 'GT']),
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

@pg.production('stat : define')
@pg.production('stat : print')
@pg.production('stat : if')
def stat(p):
    return p[0]

@pg.production('define : IDENTIFIER IS expr')
def define(p):
    return Define(Identifier(p[0].getstr()), p[2])

@pg.production('print : PRINT expr')
def print(p):
    return Print(p[1])

@pg.production('if : IF expr THEN block elseif')
def if_(p):
    return If(p[1], p[3], p[4])

@pg.production('elseif : ELSE if')
@pg.production('elseif : ELSE block END')
def elseif_(p):
    return p[1]

@pg.production('expr : NUMBER')
@pg.production('expr : IDENTIFIER')
def expr_num(p):
    if p[0].gettokentype() == 'NUMBER':
        return Number(p[0].getstr())
    elif p[0].gettokentype() == 'IDENTIFIER':
        return Identifier(p[0].getstr())
    else:
        raise AssertionError('expr Error')

@pg.production('expr : expr LT expr')
@pg.production('expr : expr GT expr')
@pg.production('expr : expr PLUS expr')
@pg.production('expr : expr MINUS expr')
@pg.production('expr : expr MULTIPLY expr')
@pg.production('expr : expr DIVIDE expr')
def expr_binop(p):
    left = p[0]
    right = p[2]
    class_list = {
        'PLUS': Add,
        'MINUS': Sub,
        'MULTIPLY': Mul,
        'DIVIDE': Div,
        'LT': Lessthan,
        'GT': Greaterthan
    }
    if p[1].gettokentype() in class_list:
        return class_list[p[1].gettokentype()](left, right)
    else:
        raise AssertionError('binop Error')

@pg.error
def error_handler(token):
    raise ValueError("Ran into a %s where it wasn't expected" % token.gettokentype())

parser = pg.build()
