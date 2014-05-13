from logic.handling.files import HandleFiles
from logic.pattern_finder import PatternFinder


class StepHandling():

    def __init__(self, window):
        self._window = window
        self.current_cube = None

        self.pattern = PatternFinder(3)
        self.pattern.set_base_cube(self._window.cube)

    def start_cube(self, event):
        self.pattern._turn_cube()

    def result_cube(self, event):
        self._window.cube.turn_x(-1, 1)


    def cube(self, event):
        print self.pattern._match()