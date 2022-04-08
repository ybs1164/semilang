from rply import LexerGenerator

lg = LexerGenerator()

lg.add('NUMBER', r'\d+')
lg.add('PLUS', r'\+')
lg.add('MINUS', r'-')


l = lg.build()
for token in l.lex('1+1-1'):
    print(token)


