import reserved
from txtTools import *

def readMenu():
    text = []
    file = open("menu.txt")
    # INICIO
    line = file.readline()
    array = toArray(line)
    input = ""
    char = ""
    while len(array) > 0:
        char = array.pop(0)
        if char == "=":
            text.append(input)
            text.append(char)
            text.append(toStr(array))
            break
        else:
            input += char
    if len(array) == 0:
        text.append(toStr(array))
    # LOOP
    line = file.readline()
    while line != "":
        array = toArray(line)
        input = ""
        char = ""
        # SECCION
        if array[0] == "'":
            while len(array) > 0:
                char = array.pop(0)
                if char == ":":
                    text.append(input)
                    text.append(char)
                    text.append(toStr(array))
                    break
                else:
                    input += char
        # ITEM
        else:
            text.append(array.pop(0))
            while len(array) > 0:
                char = array.pop(0)
                if char == "]":
                    text.append(input)
                    text.append(char)
                    text.append(toStr(array))
                    break
                elif char == ";":
                    text.append(input)
                    text.append(char)
                    input = ""
                else:
                    input += char
        line = file.readline()
        print(line)
    
    for i in range(len(text)):
        print(i, f"->{text[i]}<-")

readMenu()