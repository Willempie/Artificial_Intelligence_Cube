import xml.etree.ElementTree as ET
from os import listdir
from os import path

class XmlParser:

    _CONST_XML_LOCATION = "../../xml"

    def __init__(self):

        if path.exists(self._CONST_XML_LOCATION):
            self.xml_files = [f for f in listdir(self._CONST_XML_LOCATION)
                              if f.endswith('.xml')]

            if self.count_files() == 0:
                raise IOError("No Xml found in the directory")
        else:
            raise IOError("Xml directory not found")

    def count_files(self):
        return len(self.xml_files)

    def new_xml(self):
        step = ET.Element('Step')

        author = ET.Element('Author')
        date = ET.Element('Date')
        size = ET.Element('Size')


        cubes = ET.Element('Cubes')
        start = ET.Element('Start')
        search = ET.Element('Search')
        result = ET.Element('Result')

        step.append(author)
        step.append(date)
        step.append(size)
        step.append(cubes)
        cubes.append(start)
        cubes.append(search)
        cubes.append(result)

    def new_file(self, name):
        step = ET.Element('Step')

        author = ET.Element('Author')
        date = ET.Element('Date')
        size = ET.Element('Size')


        cubes = ET.Element('Cubes')
        start = ET.Element('Start')
        search = ET.Element('Search')
        result = ET.Element('Result')

        step.append(author)
        step.append(date)
        step.append(size)
        step.append(cubes)
        cubes.append(start)
        cubes.append(search)
        cubes.append(result)

        ET.dump(step)

        tree = ET.ElementTree(step)


        #tree.write(self._CONST_XML_LOCATION+name+'.xml')

        return

xml_reader = XmlParser()
print(xml_reader.xml_files)
xml_reader.new_file('hello')