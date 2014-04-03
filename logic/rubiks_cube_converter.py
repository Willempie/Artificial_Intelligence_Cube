from object_visual.v_rubiks_cube import VRubiksCube
from objects.cube.rubiks_cube import RubiksCube

class RubiksCubeConverter:

    @staticmethod
    def to_code_cube(input_cube):
        if isinstance(input_cube, RubiksCube):
            return input_cube


    @staticmethod
    def to_visual_cube(input_cube):
        if isinstance(input_cube, VRubiksCube):
            return input_cube