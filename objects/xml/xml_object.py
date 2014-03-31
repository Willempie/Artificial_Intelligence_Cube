import time
from objects.cube_step import Step
from object_visual.v_rubiks_cube import VCube
from objects.cube import Cube

class XmlObject:

    def __init__(self, author, size):

        self.author = author
        self.date = time.strftime("%H:%M:%S")
        self.size = size

        self.codes = []

    def set_start(self):
        return

    def set_search(self):
        return

    def set_result(self):
        return

    def add_code(self, code):
        if isinstance(code, Step):
            self.codes.append(code)
        else:
            raise ValueError("Input isn't an instance of Step")

    def set_code(self, codes):
        self.codes = codes

    def my_print(self):
        print("Author: " + self.author)
        print("Date  : " + self.date)
        print("Size  : " + self.size)

    def get_xml(self):
        return