from rply import LexerGenerator


lg = LexerGenerator()


lg.add('IS', r'is')
lg.add('IDENTIFIER', r'[a-zA-Z_][\w]*')
lg.add('NEXTLINE', r'\n+')
lg.add('NUMBER', r'\d+')


lg.ignore(r'\s+')

lexer = lg.build()
