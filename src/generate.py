import webbrowser
from menu import *
import xml.etree.ElementTree as ET

from order import Order

def genMen(menu:Menu,limit=None):
    # Etiquetas iniciales
    file = open("pages/menu.html","w")
    file.write("<!DOCTYPE html>\n")
    root = ET.Element("html")
    head = ET.Element("head")
    title = ET.Element("title")
    name:str = menu.name
    title.text = f"{name}"
    fontArgs = {
        "rel" :"stylesheet",
        "href" :"https://fonts.googleapis.com/css?family=Merienda" 
    }
    font = ET.Element("link",fontArgs)
    cssArgs = {
        "rel" :"stylesheet",
        "href" :"styles/menu.css"
    }
    css = ET.Element("link",cssArgs)
    head.append(title)
    head.append(font)
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
            if limit == None:
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
            else:
                compare = item.price    
                if not (float(compare) > limit):
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
    ET.indent(tree, space="\t", level=0)
    tree.write(file_or_filename=file,encoding="unicode",short_empty_elements=True)
    file.close()
    webbrowser.open_new_tab(f"pages/menu.html")

def genOrder(orden:Order):
    file = open("pages/factura.html","w")
    file.write("<!DOCTYPE html>\n")
    root = ET.Element("html")
    head = ET.Element("head")
    title = ET.Element("title")
    title.text = "factura"
    head.append(title)
    body = ET.Element("body")
    rest = ET.Element("h1")
    rest.text = orden.rest
    body.append(rest)
    name = ET.Element("h1")
    name.text = orden.name
    body.append(name)
    nit = ET.Element("h1")
    nit.text = orden.nit
    body.append(nit)
    add = ET.Element("h1")
    add.text = orden.add
    body.append(add)
    for elem in orden.elements:
        row = ET.Element("h2")
        row.text = f"{elem.num} - {elem.id.name} - Q{elem.id.price} - Q{float(elem.id.price)*elem.num}"
        body.append(row)
    root.append(head)
    root.append(body)
    tree = ET.ElementTree(root)
    ET.indent(tree, space="\t", level=0)
    tree.write(file_or_filename=file,encoding="unicode",short_empty_elements=True)
    file.close()
    webbrowser.open_new_tab(f"pages/factura.html")

def genTable(entries:list,type:str):
    file = open(f"pages/{type}.html","w")
    file.write("<!DOCTYPE html>\n")
    root = ET.Element("html")
    head = ET.Element("head")
    title = ET.Element("title")
    title.text = type
    cssArgs = {
        "rel" :"stylesheet",
        "href" :"styles/tablas.css"
    }
    css = ET.Element("link",cssArgs)
    head.append(title)
    head.append(css)
    body = ET.Element("body")
    # Llenando el body
    table = ET.Element("table")
    header = ET.Element("tr")
    c0 = ET.Element("th")
    c0.text = "no."
    header.append(c0)
    c3 = ET.Element("th")
    c3.text = type
    header.append(c3)
    c1 = ET.Element("th")
    c1.text = "Fila"
    header.append(c1)
    c2 = ET.Element("th")
    c2.text = "Columna"
    header.append(c2)
    c4 = ET.Element("th")
    c4.text = "Descripcion"
    header.append(c4)
    table.append(header)
    index = 0
    for entry in entries:
        index += 1
        row = ET.Element("tr")
        d0 = ET.Element("td")
        d0.text = str(index)
        row.append(d0)
        d3 = ET.Element("td")
        d3.text = str(entry.string)
        row.append(d3)
        d1 = ET.Element("td")
        d1.text = str(entry.row)
        row.append(d1)
        d2 = ET.Element("td")
        d2.text = str(entry.col)
        row.append(d2)
        d4 = ET.Element("td")
        d4.text = str(entry.desc)
        row.append(d4)
        table.append(row)  
    body.append(table)
    root.append(head)
    root.append(body)
    tree = ET.ElementTree(root)
    ET.indent(tree, space="\t", level=0)
    tree.write(file_or_filename=file,encoding="unicode",short_empty_elements=True)
    file.close()
    webbrowser.open_new_tab(f"pages/{type}.html")