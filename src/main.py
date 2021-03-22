from order import Order
import read
import generate
from menu import *

menu:Menu = None
orden:Order = None
messages = [
    "1. Cargar menu",
    "2. Cargar orden",
    "3. Generar Menu",
    "4. Generar factura",
    "5. Generar arbol",
    "6. Salir"
]
print("\n\t  LENGUAJES FORMALES Y DE PROGRAMACION, B+")
print("\t\tSAUL CASTELLANOS, 201801178")
while True:
    print()
    for m in messages:
        print(m)
    option = input("> Escoge una opción: ")
    print()
    if option == "6":
        break
    if option == "1":
        route = read.ChooseFile()
        menu = read.read(route,"menu")
        if menu is None:
            print("> El menu tuvo errores")
    elif option == "2":
        route = read.ChooseFile()
        orden = read.read(route,"orden")
        if orden is None:
            print("> La orden tuvo errores")
    elif option == "3":
        if menu is not None:
            opt = input("> ¿Quieres poner un limite(y/n)?: ")
            if opt.lower() == "y":
                limit = input("\t> ¿Limite?: ")
                try:
                    limit = float(limit)
                    generate.genMen(menu,limit)
                except:
                    print("> Limite invalido...")
            elif opt.lower() == "n":
                generate.genMen(menu)
        else:
            print("> No hay un menu cargado")
    elif option == "4":
        if orden is not None:
            for elem in orden.elements:
                id = elem.id
                elem.id = menu.getItem(id)
            orden.restName(menu.name)
            generate.genOrder(orden)
        else:
            print("> No hay una orden cargada")