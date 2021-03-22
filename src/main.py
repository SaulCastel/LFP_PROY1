import read
import generate
from menu import *

prod1 = []
prod2 = []
for i in range(1,6):
    id = f"pos_{i}"
    name = f"postre {i}"
    price = f"{10*i}.{5*i}"
    desc = f"postre no. {i}"
    item = Item(id,name,price,desc)
    prod1.append(item)
for i in range(1,6):
    id = f"cen_{i}"
    name = f"cena {i}"
    price = f"{10*i}.{5*i}"
    desc = f"cena no. {i}"
    item = Item(id,name,price,desc)
    prod2.append(item)
section1 = Section("Postres",prod1)
section2 = Section("Cenas",prod2)
sect = [section1,section2]
menuP = Menu("Prueba",sect)

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
        menu = read.readMenu(route)
    if option == "3":
        opt = input("> ¿Quieres poner un limite(y/n)?: ")
        if opt.lower() == "y":
            limit = input("\t> ¿Limite?: ")
            try:
                limit = float(limit)
                generate.genMen(menuP,limit)
            except:
                print("> Limite invalido...")
        elif opt.lower() == "n":
            generate.genMen(menuP)