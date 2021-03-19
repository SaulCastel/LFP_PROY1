class menu:
    def __init__(self, name:str, items:list) -> None:
        self.name = name
        self.items = items
        self.ids = []
        for section in self.items:
            self.ids.extend(section.getIds())

class section:
    def __init__(self, name:str, items:list) -> None:
        self.name = name
        self.items = items

    def getIds(self) -> list:
        ids = []
        for item in self.items:
            ids.append(item.id)
        return ids


class item:
    def __init__(self, id:str, name:str, price:str,desc:str) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.desc = desc