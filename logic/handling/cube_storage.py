from object_visual.v_rubiks_cube import VRubiksCube
from visual import *


class CubeStorage:

    def __init__(self, cube_size):
        self.cube_size = cube_size

        self.current_cube = None

        self._start_cube = VRubiksCube(self.cube_size, None, None, None, False)
        self._start_cube.set_front(color.red)
        self._start_cube.set_cube_visible(False)
        #self.start_turn_cube =
        self._result_cube = VRubiksCube(self.cube_size)
        self._result_cube.set_cube_visible(False)
        #self.result_turn_cube =
        self._code_cube = VRubiksCube(self.cube_size)
        self._code_cube.set_cube_visible(False)

    def _turn_invisible(self):
        if self.current_cube is not None:
            self.current_cube.set_cube_visible(False)

    def switch_to_start(self):
        self._turn_invisible()
        self.current_cube = self._start_cube
        self.current_cube.set_cube_visible(True)

    def switch_to_result(self):
        self._turn_invisible()
        self.current_cube = self._result_cube
        self.current_cube.set_cube_visible(True)

    def switch_to_code(self):
        self._turn_invisible()
        self.current_cube = self._code_cube
        self.current_cube.set_cube_visible(True)