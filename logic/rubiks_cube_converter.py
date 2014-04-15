from object_visual.v_rubiks_cube import VRubiksCube
from objects.cube.rubiks_cube import RubiksCube
from helper import Helper

class RubiksCubeConverter:

    @staticmethod
    def to_code_cube(input_cube):
        if isinstance(input_cube, RubiksCube):
            return input_cube

        x = VRubiksCube()
        cube = RubiksCube(x.get_size(), False)
        for side in Helper.CUBE_SIDES:
            cube.set_side()

    @staticmethod
    def to_visual_cube(input_cube):
        if isinstance(input_cube, VRubiksCube):
            return input_cube