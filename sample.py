import xml.etree.ElementTree as ET

# Get the XML file data
stream = open('sample.xml', 'r')

# Parse the date into an ElementTree object
xml = ET.parse(stream)

# Get the 'root' Edlemtn object from the ElementTree
root = xml.getroot()

# Iterate through each fhild of the root Element
for e in root:
    # Print the 'Id' attribute of the Element object
    print(e.get("Id"))

    # Print the string field version of the element
    print(ET.tostring(e))
    print( )
