from rply.token import BaseBox


class Number(BaseBox):
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f'{self.value}'

    def getast(self):
        return Number(self.value)

class Identifier(BaseBox):
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f'{self.name}'

    def getast(self):
        return Identifier(self.name)

class BinaryOperator(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Lessthan(BinaryOperator):
    def __repr__(self):
        return f'Lessthan ({repr(self.left.getast())}, {repr(self.right.getast())})'
    
    def getast(self):
        return Lessthan(self.left.getast(), self.right.getast())

class Greaterthan(BinaryOperator):
    def __repr__(self):
        return f'Greaterthan ({repr(self.left.getast())}, {repr(self.right.getast())})'
    
    def getast(self):
        return Greaterthan(self.left.getast(), self.right.getast())

class Add(BinaryOperator):
    def __repr__(self):
        return f'Add ({repr(self.left.getast())}, {repr(self.right.getast())})'

    def getast(self):
        return Add(self.left.getast(), self.right.getast())

class Sub(BinaryOperator):
    def __repr__(self):
        return f'Sub ({repr(self.left.getast())}, {repr(self.right.getast())})'

    def getast(self):
        return Sub(self.left.getast(), self.right.getast())

class Mul(BinaryOperator):
    def __repr__(self):
        return f'Mul ({repr(self.left.getast())}, {repr(self.right.getast())})'

    def getast(self):
        return Mul(self.left.getast(), self.right.getast())

class Div(BinaryOperator):
    def __repr__(self):
        return f'Div ({repr(self.left.getast())}, {repr(self.right.getast())})'

    def getast(self):
        return Div(self.left.getast(), self.right.getast())

class If(BaseBox):
    def __init__(self, expr, block, other):
        self.expr = expr
        self.block = block
        self.other = other
    
    def __repr__(self):
        return f'If ({repr(self.expr)}, {repr(self.block)}, {repr(self.other)})'
    
    def getast(self):
        return If(self.expr.getast(), self.block.getast(), self.other.getast())

class Print(BaseBox):
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f'Print ({repr(self.value)})'

    def getast(self):
        return Print(self.value)

class Define(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f'Define ({repr(self.left)}, {repr(self.right.getast())})'

    def getast(self):
        return Define(self.left, self.right.getast())

class Stat(BaseBox):
    def __init__(self, body):
        self.body = body

    def getast(self):
        return self.body.getast()

class Block(BaseBox):
    def __init__(self, bodys):
        self.bodys = bodys

    def getbodys(self):
        return self.bodys

    def getast(self):
        return [body.getast() for body in self.bodys]
