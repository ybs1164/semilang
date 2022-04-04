
class Define:
    def __init__(self, name, body):
        self.type = "define"
        self.name = name
        self.body = body
    
    def __str__(self):
        return f'{self.name} = {self.body}'
