import xml.etree.ElementTree as ET
from abstact_xml import AbstractXml


class XmlTurnCube(AbstractXml):

    def __init__(self, turn_cube):
        self._dimension = turn_cube.get_size()
        self._array = [[[False
                         for k in xrange(self._dimension)]
                        for i in xrange(self._dimension)]
                       for j in xrange(self._dimension)]

    def from_xml(self, xml_object, size):
        self._dimension = size

        for x in range(self._dimension):
            for y in range(self._dimension):
                for z in range(self._dimension):
                    self._array[x][y][z] = bool(xml_object.find("Part-"+str(x)+"-"+str(y)+"-"+str(z)))

    def get_xml(self, node_name="TurnCube"):
        element = ET.Element(node_name)

        for x in range(self._dimension):
            for y in range(self._dimension):
                for z in range(self._dimension):
                    part = ET.Element("Part-"+str(x)+"-"+str(y)+"-"+str(z))
                    part.text = str(self._array[x][y][z])
                    element.append(part)
        return element
