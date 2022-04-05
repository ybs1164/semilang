
class Define:
    def __init__(self, name, body):
        self.type = "define"
        self.name = name
        self.body = body
    
    def __str__(self):
        return f'{self.name} = {self.body}'

class Block:
    def __init__(self, stats):
        self.type = "block"
        self.stat_list = stats
    
    def __str__(self):
        block_str = ""
        for stat in self.stat_list:
            "".join((block_str, str(stat)))

        return block_str

class Stat:
    def __init__(self, stat):
        self.type = "stat"
        self.body = stat
    
    def __str__(self):
        return str(self.body)