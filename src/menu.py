class Item:
    def __init__(self, id:str, name:str, price:str,desc:str) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.desc = desc

class Section:
    def __init__(self, name:str) -> None:
        self.name = name
        self.items = []

    def newItem(self,item:Item):
        self.items.append(item)

class Menu:
    def __init__(self, name:str) -> None:
        self.name = name
        self.sect = []

    def newSect(self,sec:Section):
        self.sect.append(sec)