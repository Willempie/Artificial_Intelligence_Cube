import xml.etree.ElementTree as ET

class Step:

    def __init__(self, axis, rows, direction):
        if axis.lower() in ['x','y','z']:
            self.axis = axis.lower()

        if rows == 'All' or rows == -1:
            self.rows = [-1]
        else:
            self.rows = rows

        if direction in [-1, 1]:
            self.direction = direction

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

