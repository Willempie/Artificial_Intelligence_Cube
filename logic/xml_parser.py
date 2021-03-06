import xml.etree.ElementTree as ET
from os import listdir
from os import path
from objects.xml.xml_move import XmlObject


class XmlParser:

    CONST_XML_LOCATION = "objects/xml"

    def __init__(self):
        self.get_files()

    def get_files(self):
        if path.exists(self.CONST_XML_LOCATION):
            pass
        elif path.exists("../"+self.CONST_XML_LOCATION):
            self.CONST_XML_LOCATION = "../"+self.CONST_XML_LOCATION
        else:
            raise IOError("Xml directory not found")

        self.xml_files = [f for f in listdir(self.CONST_XML_LOCATION)
                          if f.endswith('.xml')]

        if self.count_files() == 0:
            raise IOError("No Xml found in the directory")

    def count_files(self):
        return len(self.xml_files)

    def new_file(self, file, xml_object, use_default_dir=False):
        tree = ET.ElementTree(xml_object.get_xml())
        if use_default_dir:
            tree.write(self.CONST_XML_LOCATION+"/"+file, "utf-8", True)
        else:
            tree.write(file, "utf-8", True)

        self.get_files()

    def read_file(self, file, use_default_dir=False):
        if use_default_dir:
            tree = ET.parse(self.CONST_XML_LOCATION+"/"+file)
        else:
            tree = ET.parse(file)

        xml_object = XmlObject()
        xml_object.from_xml(tree)
        return xml_object