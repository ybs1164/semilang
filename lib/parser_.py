from rply import ParserGenerator


pg = ParserGenerator(
    ['NUMBER', 'EQUAL', 'IDENTIFIER'],
    precedence=[
    ]
)

@pg.production('define : IDENTIFIER EQUAL expr')
def define(p):
    return Define(p[0], p[2])

@pg.production('expr : NUMBER')
def expr(p):
    return Number(int(p[0].getstr()))

parser = pg.build()
