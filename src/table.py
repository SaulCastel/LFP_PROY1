class Error:
    def __init__(self, row:int, col:int, string:str, desc:str) -> None:
        self.row = row
        self.col = col
        self.string = string
        self.desc = desc
    
    def show(self)->str:
        return f'{self.row}, {self.col}, "{self.string}", {self.desc}'

class Token(Error):
    pass