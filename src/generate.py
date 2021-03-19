from menu import *
import xml.etree.ElementTree as ET

prod1 = []
prod2 = []
for i in range(1,6):
    id = f"pos_{i}"
    name = f"postre {i}"
    price = f"{10*i}.{5*i}"
    desc = f"postre no. {1}"
    item = Item(id,name,price,desc)
    prod1.append(item)
for i in range(1,6):
    id = f"cen_{i}"
    name = f"cena {i}"
    price = f"{10*i}.{5*i}"
    desc = f"cena no. {1}"
    item = Item(id,name,price,desc)
    prod2.append(item)
section1 = Section("Postres",prod1)
section2 = Section("Cenas",prod2)
sect = [section1,section2]
menu = Menu("Prueba",sect)

def genMen(menu:Menu):
    # Etiquetas iniciales
    file = open("pages/menu.html","w")
    file.write("<!DOCTYPE html>\n")
    root = ET.Element("html")
    head = ET.Element("head")
    title = ET.Element("title")
    name:str = menu.name
    title.text = f"{name}"
    args = {
        "rel" :"stylesheet",
        "href" :"styles/menu.css"
    }
    css = ET.Element("link",args)
    head.append(title)
    head.append(css)
    body = ET.Element("body")
    # Llenar el body
    box = ET.Element("div",{"class":"box"})
    for i in range(4):
        corte = ET.Element("div",{"class":f"corte _{i}"})
        corte.text = " "
        box.append(corte)
    boxTitle = ET.Element("div",{"class":"title"})
    rest = ET.Element("h1")
    rest.text = f"{name.upper()}"
    boxTitle.append(rest)
    box.append(boxTitle)
    # Agregar etiquetas secciones
    for section in menu.sect:
        sect = ET.Element("div",{"class":"section"})
        sectTitle = ET.Element("h2",{"class":"sectTitle"})
        sectTitle.text = section.name
        sect.append(sectTitle)
        # Agregar items en secciones
        for item in section.items:
            elem = ET.Element("div",{"class":"item"})
            info = ET.Element("div",{"class":"info"})
            prod = ET.Element("h3")
            price = ET.Element("h3")
            prod.text = f"{item.name}"
            price.text = f"Q{item.price}"
            points = ET.Element("div",{"class":"points"})
            points.text = " "
            desc = ET.Element("h5",{"class":"desc"})
            desc.text = f"{item.desc}"
            info.append(prod)
            info.append(points)
            info.append(price)
            elem.append(info)
            elem.append(desc)
            sect.append(elem)
        box.append(sect)
    body.append(box)            
    # Finalizando HTML
    root.append(head)
    root.append(body)
    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ", level=0)
    tree.write(file_or_filename=file,encoding="unicode",short_empty_elements=True)
    file.close()

genMen(menu)