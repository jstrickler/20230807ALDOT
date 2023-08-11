import lxml.etree as et

FILE_NAME = "DATA/solar.xml"

doc = et.parse(FILE_NAME)

print(f"doc: {doc}")

root = doc.getroot()
print(f"root: {root}")

print(f"root.tag: {root.tag}")

for planet in root.findall(".//planet"):
    print(planet.get("planetname"))
    for moon in planet.findall("moon"):
        print(f"    {moon.text}")