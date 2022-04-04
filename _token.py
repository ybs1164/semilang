
class Token:
    def __init__(self, type, value = ""):
        self.type = type
        self.value = value

    def __str__(self):
        if self.value == "":
            return f"type : {self.type}"
        else:
            return f"type : {self.type}, value : {self.value}"
    
    def __repr__(self):
        if self.value == "":
            return f"({self.type})"
        else:
            return f"({self.type}.{self.value})"
    
    def check_type(self, type):
        return type == self.type
    
    def get_value(self):
        return self.value