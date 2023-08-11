import lxml.etree as et

FILE_NAME = "DATA/knights.txt"

root = et.Element("knights")

with open(FILE_NAME) as file_in:
    for raw_line in file_in:
        line = raw_line.rstrip() # remove \n
        name, title, color, quest, comment = line.split(':')  # split line into fields
        knight = et.SubElement(root, "knight", title=title)
        name_element = et.SubElement(knight, "name")
        name_element.text = name
        et.SubElement(knight, "color").text = color
        et.SubElement(knight, "quest").text = quest
        et.SubElement(knight, "comment").text = comment

xml_string = et.tostring(root, pretty_print=True, xml_declaration=True).decode()
print(xml_string)

xml_doc = et.ElementTree(root)
xml_doc.write("knights.xml", pretty_print=True, xml_declaration=True)

