import xml.etree.ElementTree as ET
"""Funció per retornar un xml amb nom: exerciciA.xml que contindrà 5 alumnes i les seves dades """
def creaxml():

    root = ET.Element('students')
    child = ET.SubElement(root, 'student')
    child1 = ET.SubElement(root, 'student')
    child2 = ET.SubElement(root, 'student')
    child3 = ET.SubElement(root, 'student')
    child4 = ET.SubElement(root, 'student')

    """-----PRIMER STUDENT-----"""
    name = ET.SubElement(child, 'name')
    surname = ET.SubElement(child, 'surname')
    email = ET.SubElement(child, 'email')
    dni = ET.SubElement(child, 'child')

    name.text = "Harpreet"
    surname.text = "Kaur"
    email.text = "hkaur22@jaumebalmes.net"
    dni.text = "12345678H"

    element = root[0]
    element.set('pais', 'India')
    """-----FINAL-----"""

    """-----SEGON STUDENT-----"""
    name1 = ET.SubElement(child1, 'name')
    surname1 = ET.SubElement(child1, 'surname')
    email1 = ET.SubElement(child1, 'email')
    dni1 = ET.SubElement(child1, 'child')

    name1.text = "Laia"
    surname1.text = "Rodriguez"
    email1.text = "lrodriguez22@jaumebalmes.net"
    dni1.text = "3456789L"

    element1 = root[1]
    element1.set('pais', 'Catalunya')

    """-----FINAL-----"""

    """-----TERCER STUDENT-----"""

    name2 = ET.SubElement(child2, 'name')
    surname2 = ET.SubElement(child2, 'surname')
    email2 = ET.SubElement(child2, 'email')
    dni2 = ET.SubElement(child2, 'child')

    name2.text = "David"
    surname2.text = "Arguelles"
    email2.text = "darguelles22@jaumebalmes.net"
    dni2.text = "98765432D"

    element2 = root[2]
    element2.set('pais', 'Norueg')

    """-----FINAL-----"""

    """-----QUART STUDENT-----"""

    name3 = ET.SubElement(child3, 'name')
    surname3 = ET.SubElement(child3, 'surname')
    email3 = ET.SubElement(child3, 'email')
    dni3 = ET.SubElement(child3, 'child')

    name3.text = "Alex"
    surname3.text = "Navarro"
    email3.text = "anavarro@jaumebalmes.net"
    dni3.text = "45678987A"

    element3 = root[3]
    element3.set('pais', 'Catalunya')

    """-----FINAL-----"""

    """-----CINQUÈ STUDENT-----"""

    name4 = ET.SubElement(child4, 'name')
    surname4 = ET.SubElement(child4, 'surname')
    email4 = ET.SubElement(child4, 'email')
    dni4 = ET.SubElement(child4, 'child')

    name4.text = "Patricia"
    surname4.text = "Valencia"
    email4.text = "pvalenci22@jaumebalmes.net"
    dni4.text = "56543234P"

    element4 = root[4]
    element4.set('pais', 'Peruana')
    """-----FINAL-----"""


    ET.indent(root)  #.indent per identar el codi
    ET.dump(root)

    tree = ET.ElementTree(root)
    tree.write("exerciciA.xml")
