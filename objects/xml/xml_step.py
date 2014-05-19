import xml.etree.ElementTree as ET
from abstact_xml import AbstractXml


class Step(AbstractXml):

    def __init__(self, axis=None, rows=None, direction=None):
        if axis is None or axis in ['x','y','z']:
            self.axis = axis

        self.rows = rows

        if direction is None or direction in [-1, 1]:
            self.direction = direction

    def from_xml(self, xml_object):
        self.axis = xml_object.find("Axis").text
        self.rows = xml_object.find("Row").text
        self.direction = xml_object.find("Direction").text

    def get_xml(self):
        element = ET.Element("Step")

        axis = ET.Element("Axis")
        axis.text = self.axis

        row = ET.Element("Row")
        row.text = str(self.rows)

        direction = ET.Element("Direction")
        direction.text = str(self.direction)

        element.append(axis)
        element.append(row)
        element.append(direction)

        return element

