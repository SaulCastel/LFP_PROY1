from menu import *

class Element():
    def __init__(self,num:int,id) -> None:
        self.num = num
        self.id = id

class Order:
    def __init__(self, name:str,nit:str,add:str,perc:str) -> None:
        self.name = name
        self.nit = nit
        self.add = add
        self.perc = perc
        self.elements = []
    
    def newElem(self,elem:Element):
        self.elements.append(elem)

    def restName(self,name:str):
        self.rest = name