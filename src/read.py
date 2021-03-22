from txtTools import *
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from menu import *
from table import *
import generate as gen
import reserved as res

def ChooseFile():
    Tk().withdraw()
    return askopenfilename()

def readMenu(route)->Menu:
    file = open(route)
    content = file.read()
    text = toArray(content)
    tokens = []
    errors = []
    char:str = ""
    row = 0
    col = -1
    state = 0
    lex:str = ""
    word = False
    while len(text) > 0:
        if state != 6:
            char = text.pop(0)
            col += 1
        if state == 0:
            if char == " " or char == "" or char == "\t":
                continue
            elif char.islower():
                lex += char
                state = 1
            elif char.isdigit():
                lex += char
                state = 2
            elif char == "'":
                lex += char
                state = 5
            elif char == "[" or char == "]" or char == ":" or char == ";" or char == "=" or char=="%":
                tokens.append(Token(row,col,char,"Simbolo"))
            elif char == "\n":
                pass
            else:
                errors.append(Error(row,col,char,"Caracter desconocido"))
                lex = ""
                state = 0
        elif state == 1:
            if char.islower() or char.isdigit() or char == "_":
                lex += char
            elif char == " " or char == ";" or char == "=" or char == "\n" or char == "\t":
                if lex == "restaurante":
                    if not word:
                        token = Token(row,col,lex,"Palabra reservada")
                        word = True
                    else:
                        errors.append(Error(row,col,lex,"Solo pueder haber un 'restaurante'"))
                        lex = ""
                        state = 0
                else:
                    token = Token(row,col,lex,"Indentificador")
                tokens.append(token)
                lex = ""
                state = 0
            else:
                lex += char
                errors.append(Error(row,col,lex,"Identificador invalido"))
                lex = ""
                state = 0
        elif state == 2:
            if char.isdigit():
                lex += char
            elif char == ".":
                lex += char
                state = 3
            elif char == " " or char == ";" or char == "=" or char == "\n" or char == "\t":
                tokens.append(Token(row,col,lex,"Numero"))
                lex = ""
                state = 0
            else:
                lex += char
                errors.append(Error(row,col,lex,"Numero invalido"))
                lex = ""
                state = 0
        elif state == 3:
            if char.isdigit():
                lex += char
            elif char == "%":
                lex += char
                state = 4
            elif char == " " or char == ";" or char == "=" or char == "\n" or char == "\t":
                tokens.append(Token(row,col,lex,"Numero"))
                lex = ""
                state = 0
            else:
                lex += char
                errors.append(Error(row,col,lex,"Numero invalido"))
                lex = ""
                state = 0
        elif state == 4:
            tokens.append(Token(row,col,lex,"Numero"))
            lex = ""
            state = 0
        elif state == 5:
            if char == "'":
                lex += char
                state = 6
            else:
                if char != "\n":
                    lex += char
                else:
                    errors.append(Error(row,col,lex,"Cadena invalida"))
                    lex = ""
                    state = 0
        elif state == 6:
            tokens.append(Token(row,col,lex,"Cadena"))
            lex = ""
            state = 0
        if char == "\n":
            row += 1
            col = 0
            state = 0
            lex = ""
    if len(tokens) > 0:
        gen.genTable(tokens,"Tokens")
    if len(errors) > 0:
        gen.genTable(errors,"Errores")
        return None
    else:
        return createMenu(tokens)

def createMenu(tokens:list)-> Menu:
    menu:Menu = None
    sec:Section = None
    id = ""
    name = ""
    price = ""
    desc = ""
    state = 0
    while len(tokens) > 0:
        string = tokens.pop(0).string
        if state == 0:
            if res.cadena.match(string):
                menu = Menu(ridAps(string))
                state = 1
        elif state == 1:
            if res.cadena.match(string):
                sec = Section(ridAps(string))
                menu.newSect(sec)
            elif string == "[":
                state = 2
            elif string == "]":
                sec.newItem(Item(id,name,price,desc))
        elif state == 2:
            if res.id.match(string):
                id = string
                state = 3
        elif state == 3:
            if res.cadena.match(string):
                name = ridAps(string)
                state = 4
        elif state == 4:
            if res.numero.match(string):
                price:str = string
                if price.endswith("."):
                    price += "00"
                state = 5
        elif state == 5:
            if res.cadena.match(string):
                desc = ridAps(string)
                state = 1
    return menu