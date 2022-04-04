import _ast as ast

class Parser:
    def __init__(self, tokens):
        self.token_list = tokens
        self.index = 0
        self.length = len(tokens)

        self.ast = ast.Define()
    
    def define(self):
        pass
    
    def run(self):
        pass