from rply.token import BaseBox


class Number(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

class Ident(BaseBox):
    def __init__(self, name):
        self.name = name

    def eval(self):
        return self.name

class Define(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return Define(self.left, self.right.eval())

class Stat(BaseBox):
    def __init__(self, body):
        self.body = body

    def eval(self):
        return self.body.eval()

class Block(BaseBox):
    def __init__(self, bodys):
        self.bodys = bodys

    def eval(self):
        return [body.eval() for body in self.bodys]
