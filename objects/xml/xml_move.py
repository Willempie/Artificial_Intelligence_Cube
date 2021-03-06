import xml.etree.ElementTree as ET
import time
from objects.cube.rubiks_cube import RubiksCube
from objects.xml import xml_step
from objects.xml.abstact_xml import AbstractXml
from objects.xml.xml_cube import XmlCube
from xml_step import Step
from helper import Helper


class XmlObject(AbstractXml):

    def __init__(self, author="Secret", size="3", set_date=True):

        self._author = author
        if set_date:
            self._date = time.strftime("%Y-%m-%d %H:%M:%S")
        else:
            self._date = set_date
        self._size = size

        self._start_cube = None
        self._start_cube_turn =None
        self._result_cube = None
        self._result_cube_turn =None

        self._codes = []

    def set_size(self, size):
        if size > 2:
            self._size = size

    def set_start(self, rubikscube, turn_cube=None):
        self._start_cube = rubikscube
        self._start_cube_turn = turn_cube

    def set_result(self, rubikscube, turn_cube=None):
        self._result_cube = rubikscube
        self._result_cube_turn = turn_cube

    def add_code(self, code):
        if isinstance(code, Step):
            self._codes.append(code)
        else:
            raise ValueError("Input isn't an instance of Step")

    def set_code(self, codes):
        self._codes = codes

    def from_xml(self, xml):
        self._author = xml.find("Author").text
        self._date = xml.find("Date").text
        self._size = int(xml.find("Size").text)

        self._start_cube = XmlCube.from_xml(xml.find("Cubes/Start"), self._size)
        self._result_cube = XmlCube.from_xml(xml.find("Cubes/Result"), self._size)


        for element in list(xml.find("Steps")):
            step = Step()
            step.from_xml(element)
            self._codes.append(step)

        #Todo fetch the steps

    def get_xml(self):
        if self._start_cube is None or \
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
        cubes.append(XmlCube.get_xml(self._start_cube, "Start"))

        if self._start_cube_turn is None:
            start_cube_turn = ET.Element("Start-Turn")
            start_cube_turn.text = "False"
            cubes.append(start_cube_turn)
        else:
            cubes.append(self._start_cube_turn("Start-Turn"))

        cubes.append(XmlCube.get_xml(self._result_cube, "Result"))

        if self._result_cube_turn is None:
            start_cube_turn = ET.Element("Result-Turn")
            start_cube_turn.text = "False"
            cubes.append(start_cube_turn)
        else:
            cubes.append(self._result_cube_turn("Result-Turn"))


        move.append(cubes)

        steps = ET.Element("Steps")
        for i in self._codes:
            steps.append(i.get_xml())
        move.append(steps)

        return move

