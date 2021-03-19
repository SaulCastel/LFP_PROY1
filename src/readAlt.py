import reserved as res
from table import *
from txtTools import toArray

def readM(route):
    file = open("menu.txt")
    lines = file.readlines()
    errors = []
    text = []
    for line in lines:
        for char in line:
            text.append(char)
    row = 0
    col = 0 
    char = text.pop(0)
    error:Error = None
    # LEER "restaurante"
    input = ""
    while char != "\n":
        if char != " ":
            input += char
        if input == "restaurante":
            # LEER "="
            input = ""
            while char != "\n":
                if char != " ":
                    input += char
                if input == "=":
                    # LEER nombre
                    char = text.pop(0)
                    col += 1
                    while char != "\n":
                        input += char
                        char = text.pop(0)
                    if not res.cadena.search(input):
                        desc = "Se esperaba cadena"
                        error = Error(row,col,input,desc)
                    break
                char = text.pop(0)
                col += 1
            else:
                desc = 'Se esperaba "="'
                error = Error(row,col,input,desc)
            break
        char = text.pop(0)
        col += 1
    else:
        desc = 'Se esperaba "restaurante"'
        error = Error(row,col,input,desc)
    errors.append(error)
    # TABLA
    print("> ERRORES")
    for elem in errors:
        print(elem.show())

def readMenu(route):
    file = open("menu.txt")
    lines = file.readlines()
    text = []
    for line in lines:
        for char in line:
            text.append(char)
    mName = ""
    errors = []
    # LEYENDO "restaurante"
    row = 0
    col = 0 
    input = ""
    char = text.pop(0)
    while char != "\n":
        if input == "restaurante":
            res.states["start"] = True
            input = ""
        elif char == "=":
            res.states["assign"] = True
            break
        elif char != " ":
            input += char
        char = text.pop(0)
        col += 1
    else:
        row += 1
    if not res.states["start"]:
        desc = 'Se esperaba "restaurante"'
        error = Error(row, col, input, desc)
        errors.append(error)
    # SIGNO "="
    if not res.states["assign"]:
        desc = 'Se esperaba "="'
        error = Error(row,col,input,desc)
        errors.append(error)
    # LEYENDO NOMBRE
    rest = None
    if row > 0:
        input += char
        rest = toArray(input)
    else:
        rest = text
    char = rest.pop(0)
    col += 1
    while char != "\n":
        if char == "'":
            char = rest.pop(0)
            col += 1
            while char != "\n":
                if char == "'":
                    res.states["name"] = True
                    break
                else:
                    char = rest.pop(0)
                    col += 1
            else:
                break
        char = rest.pop(0)
        col += 1
    if not res.states["name"]:
        desc = 'no se pudo asignar nombre'
        error = Error(row,col,input,desc)
        errors.append(error)
    # IMPRIMIR "TABLAS"
    print("> ERRORES")
    for error in errors:
        print(error.show())
            
readM("")            