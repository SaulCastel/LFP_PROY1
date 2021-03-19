class Menu:
    def __init__(self, name:str, sect:list) -> None:
        self.name = name
        self.sect = sect
        self.items = []
        for section in self.sect:
            for item in section.items:
                self.items.append(item)

    def getItem(self, index):
        return self.items[index]    

class Section:
    def __init__(self, name:str, items:list) -> None:
        self.name = name
        self.items = items

class Item:
    def __init__(self, id:str, name:str, price:str,desc:str) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.desc = desc