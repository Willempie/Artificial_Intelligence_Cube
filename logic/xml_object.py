import xml.etree.ElementTree as ET
import time
from objects.cube.rubiks_cube import RubiksCube
from cube_step import Step
from helper import Helper

class XmlObject:

    def __init__(self, author="Secret", size="3", set_date=True):

        self._author = author
        if set_date:
            self._date = time.strftime("%Y-%m-%d %H:%M:%S")
        else:
            self._date = set_date
        self._size = size

        self._start_cube = None
        self._search_cube = None
        self._result_cube = None

        self._codes = []

    def set_start(self, rubikscube):
        self._start_cube = rubikscube

    def set_search(self, rubikscube):
        self._search_cube = rubikscube

    def set_result(self, rubikscube):
        self._result_cube = rubikscube

    def add_code(self, code):
        if isinstance(code, Step):
            self._codes.append(code)
        else:
            raise ValueError("Input isn't an instance of Step")

    def set_code(self, codes):
        self._codes = codes

    def my_print(self):
        print("Author: " + str(self._author))
        print("Date  : " + str(self._date))
        print("Size  : " + str(self._size))

    def _get_rubiks_cube_xml(self, type_cube, rubikscube):
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

    @staticmethod
    def _part_finder(type_cube, side, x, y):
        return "Cubes/"+type_cube+"/"+side+"/Part-"+str(x)+"-"+str(y)

    def _from_rubiks_cube_xml(self, type_cube, xml):
        rubikscube = RubiksCube(self._size)

        for x in Helper.CUBE_SIDES:
            side = [[None for k in xrange(self._size)] for i in xrange(self._size)]
            for y in range(rubikscube.get_size()):
                for z in range(rubikscube.get_size()):
                    side[y][z] = xml.find(self._part_finder(type_cube,x,y,z)).text
            rubikscube.set_side(x, side)

        return rubikscube

    def from_xml(self, xml):
        self._author = xml.find("Author").text
        self._date = xml.find("Date").text
        self._size = int(xml.find("Size").text)
        self.my_print()
        self._from_rubiks_cube_xml("Start", xml)
        #Todo fetch the steps


    def get_xml(self):
        if self._start_cube is None or \
            self._search_cube is None or \
            self._result_cube is None or \
            len(self._codes) is 0:
            raise ValueError("Not all needed values have been set")

        move = ET.Element('Move')

        author = ET.Element('Author')
        author.text = self._author
        move.append(author)

        date = ET.Element('Date')
        date.text = self._date
        move.append(date)

        size = ET.Element('Size')
        size.text = str(self._size)
        move.append(size)

        cubes = ET.Element('Cubes')
        cubes.append(self._get_rubiks_cube_xml("Start",self._start_cube))
        cubes.append(self._get_rubiks_cube_xml("Search",self._search_cube))
        cubes.append(self._get_rubiks_cube_xml("Result",self._result_cube))
        move.append(cubes)

        steps = ET.Element("Steps")
        for i in self._codes:
            steps.append(i.get_xml())
        move.append(steps)

        return move