from rply import LexerGenerator

lexer = LexerGenerator()

lexer.add('NUMBER', r'\d+')
lexer.add('EQUAL', r'=')
lexer.add('IDENTIFIER', r'[\w^\d][\w]*')


lexer.ignore(r'\s+')

l = lexer.build()
