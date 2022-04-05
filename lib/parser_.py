from .ast_ import *


def safe_append(list, value):
    if value is not None:
        list.append(value)
        return True
    return False


class Parser:
    def __init__(self, tokens):
        self.token_list = tokens
        self.index = 0
        self.length = len(tokens)

        self.ast = None
    
    def define(self):
        return

    def stat(self):
        self.define()
        return

    # <block> ::= <stat>+
    def block(self):
        stat_list = []
        while self.index < self.length:
            if not safe_append(stat_list, self.stat()):
                break
        
        return Block(stat_list)
    
    def run(self):
        return self.block()
