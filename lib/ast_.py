from rply.token import BaseBox


class Number(BaseBox):
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f'{self.value}'

    def getast(self):
        return Number(self.value)

class String(BaseBox):
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f'{self.value}'

    def getast(self):
        return String(self.value)

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

class And(BinaryOperator):
    def __repr__(self):
        return f'And ({repr(self.left.getast())}, {repr(self.right.getast())})'
    
    def getast(self):
        return And(self.left.getast(), self.right.getast())

class Or(BinaryOperator):
    def __repr__(self):
        return f'Or ({repr(self.left.getast())}, {repr(self.right.getast())})'
    
    def getast(self):
        return Or(self.left.getast(), self.right.getast())

class Equal(BinaryOperator):
    def __repr__(self):
        return f'Equal ({repr(self.left.getast())}, {repr(self.right.getast())})'
    
    def getast(self):
        return Equal(self.left.getast(), self.right.getast())

class NotEqual(BinaryOperator):
    def __repr__(self):
        return f'NotEqual ({repr(self.left.getast())}, {repr(self.right.getast())})'
    
    def getast(self):
        return NotEqual(self.left.getast(), self.right.getast())

class LessthanEqual(BinaryOperator):
    def __repr__(self):
        return f'LessthanEqual ({repr(self.left.getast())}, {repr(self.right.getast())})'
    
    def getast(self):
        return LessthanEqual(self.left.getast(), self.right.getast())

class GreaterthanEqual(BinaryOperator):
    def __repr__(self):
        return f'GreaterthanEqual ({repr(self.left.getast())}, {repr(self.right.getast())})'
    
    def getast(self):
        return GreaterthanEqual(self.left.getast(), self.right.getast())

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

class Application(BaseBox):
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments
    
    def __repr__(self):
        return f'{repr(self.name)} ({repr(self.arguments)})'
    
    def getast(self):
        return Application(self.name.getast(), self.arguments.getast())

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
        return Print(self.value.getast())

class Return(BaseBox):
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f'Return ({repr(self.value.getast())})'

    def getast(self):
        return Return(self.value.getast())

class Function(BaseBox):
    def __init__(self, arguments, block):
        self.arguments = arguments
        self.block = block
    
    def __repr__(self):
        return f'Function ({repr(self.arguments.getast())}, {repr(self.block)})'
    
    def getast(self):
        return Function(self.arguments.getast(), self.block.getast())

class Define(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f'Define ({repr(self.left)}, {repr(self.right.getast())})'

    def getast(self):
        return Define(self.left, self.right.getast())

class Block(BaseBox):
    def __init__(self, bodys):
        self.bodys = bodys
    
    def __repr__(self):
        return '\n'.join([f'{body.getast()}' for body in self.bodys])

    def getbodys(self):
        return self.bodys

    def getast(self):
        return Block([body.getast() for body in self.bodys])
