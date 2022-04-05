from .token_ import Token


# string concat
def append_str(str1, str2):
    return "".join((str1, str2))


# lexer
class Lexer:
    def __init__(self, str):
        self.str = str
        self.index = 0
        self.length = len(str)

        self.token_list = []

    def current(self):
        if self.index < self.length:
            return self.str[self.index]
        else:
            return ""
        
    def next(self):
        temp_char = self.current()
        self.index = self.index + 1
        return temp_char
    
    def identifier_token(self):
        temp_str = ""
        if not self.current().isalpha():
            return None
        
        while self.current().isalpha():
            temp_str = append_str(temp_str, self.next())
        
        return Token("identifier", temp_str)

    def number_token(self):
        temp_str = ""

        if not (self.current() >= '1' and self.current() <= '9'):
            return None
        temp_str = append_str(temp_str, self.next())
        
        while self.current() >= '0' and self.current() <= '9':
            temp_str = append_str(temp_str, self.next())
        
        return Token("number", temp_str)
    
    def letter_token(self):
        token_list = {
            "=" : Token("equal")
        }
        token = token_list[self.next()]
        return token

    def run(self):
        while self.index < self.length:
            def safe_append(list, value):
                if value is not None:
                    list.append(value)
                    return True
                return False
            
            if self.current().isspace():
                self.next()
                continue
            
            if safe_append(self.token_list, self.identifier_token()):
                continue
            
            if safe_append(self.token_list, self.number_token()):
                continue
            
            safe_append(self.token_list, self.letter_token())
            
        return self.token_list

