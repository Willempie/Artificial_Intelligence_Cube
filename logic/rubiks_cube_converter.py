from object_visual.v_rubiks_cube import VRubiksCube
from objects.cube.rubiks_cube import RubiksCube
from helper import Helper

class RubiksCubeConverter:

    @staticmethod
    def to_code_cube(input_cube):
        if isinstance(input_cube, RubiksCube):
            return input_cube

        x = VRubiksCube()

        color_array = []

        cube = RubiksCube(x.get_size(), False)
        for side in Helper.CUBE_SIDES:
            current_side = x.get_side(side)
            for x in range(x.get_size()):
                for y in range(x.get_size()):
                    current_color = current_side[x][y].color
                    if current_color not in color_array:
                        color_array.append(current_color)
                    current_side[x][y] = color_array.index(current_color)
            cube.set_side(side, current_side)

    @staticmethod
    def to_visual_cube(input_cube):
        if isinstance(input_cube, VRubiksCube):
            return input_cube