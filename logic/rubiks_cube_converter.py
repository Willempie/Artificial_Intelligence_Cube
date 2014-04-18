from visual import *
from object_visual.v_rubiks_cube import VRubiksCube
from objects.cube.rubiks_cube import RubiksCube
from helper import Helper


class RubiksCubeConverter:

    @staticmethod
    def to_code_cube(input_cube):
        if input_cube.__class__ == RubiksCube().__class__:
            return input_cube

        cube = RubiksCube(input_cube.get_size(), False)
        for side in Helper.CUBE_SIDES:
            current_side = input_cube.get_side(side)
            for x in range(input_cube.get_size()):
                for y in range(input_cube.get_size()):
                    if current_side[x][y].color in Helper.CUBE_COLOR:
                        current_side[x][y] = Helper.CUBE_COLOR.index(current_side[x][y].color)
                    else:
                        current_side[x][y] = 12 #dummy value

            cube.set_side(side, current_side)

        return cube

    @staticmethod
    def to_visual_cube(input_cube):
        if input_cube.__class__ == VRubiksCube().__class__:
            return input_cube

        cube = VRubiksCube(input_cube.get_size(),None, None, None, False)
        for side in Helper.CUBE_SIDES:
            current_side = input_cube.get_side(side)
            for x in range(input_cube.get_size()):
                for y in range(input_cube.get_size()):
                    if current_side[x][y] < len(Helper.CUBE_COLOR):
                        current_side[x][y] = Helper.CUBE_COLOR[current_side[x][y]]
                    else:
                        current_side[x][y] = color.gray(0.6) #dummy value

            cube.set_side(side, current_side)

        return cube