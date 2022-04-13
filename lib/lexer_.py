from rply import LexerGenerator

lg = LexerGenerator()

lg.add('NUMBER', r'\d+')
lg.add('EQUAL', r'=')
lg.add('IDENTIFIER', r'[\w^\d][\w]*')


lg.ignore(r'\s+')

lexer = lg.build()
