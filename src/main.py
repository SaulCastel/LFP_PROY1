import read

messages = [
    "1. Cargar menu",
    "2. Cargar orden",
    "3. Generar Menu",
    "4. Generar factura",
    "5. Generar árbol",
    "6. Salir"
]
print("\n\t  LENGUAJES FORMALES Y DE PROGRAMACION, B+")
print("\t\tSAUL CASTELLANOS, 201801178\n")
while True:
    for m in messages:
        print(m)
    option = input("> Escoge una opción: ")
    print()
    if option == "6":
        break
    if option == "1":
        route = read.ChooseFile()