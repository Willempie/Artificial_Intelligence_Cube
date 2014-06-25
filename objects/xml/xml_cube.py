import xml.etree.ElementTree as ET
from logic.rubiks_cube_converter import RubiksCubeConverter
from helper import Helper
from objects.cube.rubiks_cube import RubiksCube
from objects.xml.abstact_xml import AbstractXml


class XmlCube(AbstractXml):

    @staticmethod
    def from_xml(xml_object, size):
        rubikscube = RubiksCube(size)

        for x in Helper.CUBE_SIDES:
            side = [[None for k in xrange(size)] for i in xrange(size)]
            for y in range(rubikscube.get_size()):
                for z in range(rubikscube.get_size()):
                    value = xml_object.find(x+"/Part-"+str(y)+"-"+str(z)).text
                    if value == str(None):
                        side[y][z] = None
                    else:
                        side[y][z] = int(value)
            rubikscube.set_side(x, side)
        return rubikscube


    @staticmethod
    def get_xml(rubikscube, type_cube="Cube"):
        rubikscube = RubiksCubeConverter.to_code_cube(rubikscube)

        element = ET.Element(type_cube)
        for x in Helper.CUBE_SIDES:
            side = ET.Element(x)
            rubiks_cube_side = rubikscube.get_side(x)
            for y in range(rubikscube.get_size()):
                for z in range(rubikscube.get_size()):
                    cube = ET.Element("Part-"+str(y)+"-"+str(z))
                    cube.text = str(rubiks_cube_side[y][z])
                    side.append(cube)
            element.append(side)
        return element