from rply.token import BaseBox


class Number(BaseBox):
    def __init__(self, value):
        self.value = value

    def getast(self):
        return self.value

class Identifier(BaseBox):
    def __init__(self, name):
        self.name = name

    def getast(self):
        return self.name

class Define(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right

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
