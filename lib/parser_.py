from lib2to3.pgen2.token import STRING
from rply import ParserGenerator
from lib.ast_ import *


pg = ParserGenerator(
    ['NUMBER', 'STRING', 'IDENTIFIER',
     'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE',
     'IS', 'PRINT', 'IF', 'THEN', 'ELSE', 'END',
     'FUNCTION', 'RETURN', 'AND', 'OR', 'LPAREN', 'RPAREN',
     'EQ', 'NEQ', 'LTE', 'GTE', 'LT', 'GT'],
    precedence=[
        ('right', ['IS']),
        ('left', ['AND', 'OR', 'EQ', 'NEQ', 'LTE', 'GTE', 'LT', 'GT']),
        ('left', ['PLUS', 'MINUS']),
        ('left', ['MULTIPLY', 'DIVIDE'])
    ]
)

@pg.production('block : block block')
def block_next(p):
    return Block([*p[0].getbodys(), *p[1].getbodys()])

@pg.production('block : stat')
@pg.production('block : laststat')
def block_next(p):
    return Block([p[0]])

@pg.production('stat : define')
@pg.production('stat : print')
@pg.production('stat : if')
def stat(p):
    return p[0]

@pg.production('laststat : RETURN expr')
def laststat(p):
    return Return(p[1])

@pg.production('define : IDENTIFIER IS expr')
def define(p):
    return Define(Identifier(p[0].getstr()), p[2])

@pg.production('print : PRINT expr')
def print(p):
    return Print(p[1])

@pg.production('if : IF expr THEN block ELSE elseif')
def if_(p):
    return If(p[1], p[3], p[5])

@pg.production('elseif : if')
@pg.production('elseif : block END')
def elseif_(p):
    return p[0]

@pg.production('expr : function')
def expr_function(p):
    return p[0]

@pg.production('expr : NUMBER')
@pg.production('expr : STRING')
def expr_num(p):
    if p[0].gettokentype() == 'NUMBER':
        return Number(p[0].getstr())
    elif p[0].gettokentype() == 'STRING':
        return String(p[0].getstr())
    else:
        raise AssertionError('expr Error')

@pg.production('expr : prexpr')
def expr_pr(p):
    return p[0]

@pg.production('function : FUNCTION LPAREN IDENTIFIER RPAREN block END')
def func(p):
    return Function(Identifier(p[2].getstr()), p[4])

@pg.production('prexpr : IDENTIFIER')
def prexpr_id(p):
    return Identifier(p[0].getstr())

@pg.production('prexpr : application')
def prexpr_application(p):
    return p[0]

@pg.production('application : prexpr LPAREN expr RPAREN')
def application(p):
    return Application(p[0], p[2])

@pg.production('prexpr : LPAREN expr RPAREN')
def prexpr_paren(p):
    return p[1]

@pg.production('expr : expr AND expr')
@pg.production('expr : expr OR expr')
@pg.production('expr : expr EQ expr')
@pg.production('expr : expr NEQ expr')
@pg.production('expr : expr LTE expr')
@pg.production('expr : expr GTE expr')
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
        'GT': Greaterthan,
        'LTE': LessthanEqual,
        'GTE': GreaterthanEqual,
        'EQ': Equal,
        'NEQ': NotEqual,
        'AND': And,
        'OR': Or
    }
    if p[1].gettokentype() in class_list:
        return class_list[p[1].gettokentype()](left, right)
    else:
        raise AssertionError('binop Error')

@pg.error
def error_handler(token):
    raise ValueError("Ran into a %s where it wasn't expected" % token.gettokentype())

parser = pg.build()
