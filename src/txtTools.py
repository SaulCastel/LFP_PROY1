def toArray(str:str)->list:
    '''
    Recibe un string y lo retorna como array
    '''
    array = []
    for char in str:
        array.append(char)
    return array

def toStr(array:list)->str:
    '''
    Recibe un array y lo retorna como string
    '''
    string = ""
    for char in array:
        string += char
    return string

def ridAps(string:str)->str:
    '''
    Quita las comillas de una cadena
    '''
    return string.replace("'","")