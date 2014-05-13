import xml.etree.ElementTree as ET
from os import listdir
from os import path

from objects.xml.xml_move import XmlObject
from objects.xml.xml_step import Step
from objects.cube.rubiks_cube import RubiksCube


class XmlParser:

    CONST_XML_LOCATION = "objects/xml"

    def __init__(self):
        self.get_files()

    def get_files(self):
        if path.exists(self.CONST_XML_LOCATION):
            self.xml_files = [f for f in listdir(self.CONST_XML_LOCATION)
                              if f.endswith('.xml')]

            if self.count_files() == 0:
                raise IOError("No Xml found in the directory")
        else:
            raise IOError("Xml directory not found")

    def count_files(self):
        return len(self.xml_files)

    def new_file(self, file, xml_object):
        tree = ET.ElementTree(xml_object.get_xml())
        tree.write(file, "utf-8", True)
        self.get_files()

    def read_file(self, file):
        tree = ET.parse(file)
        xml_object = XmlObject()
        xml_object.from_xml(tree)

#d = XmlObject("Gay", 3)
#d.set_start(RubiksCube(3))
#d.set_search(RubiksCube(3))
#d.set_result(RubiksCube(3))
#
#x = Step("y", 0, 1)
#y = Step("x", 0, -1)
#z = Step("x", 0, -1)
#
#d.add_code(x)
#d.add_code(y)
#d.add_code(z)
#
#xml_reader = XmlParser()
#print(xml_reader.xml_files)
##xml_reader.new_file("hello3",d)
#xml_reader.read_file("hello3")