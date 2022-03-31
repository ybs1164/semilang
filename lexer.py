def append_str(str1, str2):
    return "".join((str1, str2))

class Lexer():
    def __init__(self, str):
        self.str = ""
        self.index = 0
        self.length = len(str)

        self.token_list = []

    def current(self):
        return self.str[self.index]
    
    def next(self):
        temp_char = self.current()
        self.index = self.index + 1
        return temp_char

    def number(self):
        temp_str = ""

        if not (self.current() >= '1' and self.current() <= '9'):
            return None
        temp_str = append_str(temp_str, self.next())
        
        while self.current() >= '0' and self.current() <= '9':
            temp_str = append_str(temp_str, self.next())
        
        # todo : return Token
        return temp_str

    def run(self):
        # todo : token lexer
        return self.token_list

