from visual import *
from helper import Helper
from logic.rubiks_cube_converter import RubiksCubeConverter
from objects.cube.rubiks_cube import RubiksCube
import copy

class PatternFinder:

    def __init__(self, cube_size):
        self.cube_size = cube_size
        self.base_cube = None
        self.base_turn_cube = None
        self.match_cube = None
        self.match_turn_cube = None

    def set_base_cube(self, cube):
        if cube.get_size() == self.cube_size:
            self.base_cube = RubiksCubeConverter.to_code_cube(cube)
        else:
            raise Exception("Cube size doesn't match")

    def set_base_turn_cube(self, turn_cube):
        if turn_cube is not None:
            self.base_turn_cube = turn_cube

    def set_matching_cube(self, cube):
        if cube.get_size() == self.cube_size:
            self.match_cube = RubiksCubeConverter.to_code_cube(cube)
        else:
            raise Exception("Cube size doesn't match")

    def set_match_turn_cube(self, turn_cube):
        if turn_cube is not None:
            self.base_match_cube = turn_cube

    def _generate_cubes(self):
        storage_side = []

        for x in range(6):
            storage_side.append(copy.deepcopy(self.base_cube))

        storage_side[1].turn("x", -1, 1)

        storage_side[2].turn("x", -1, 1)
        storage_side[2].turn("x", -1, 1)

        storage_side[3].turn("x", -1, -1)

        storage_side[4].turn("z", -1, 1)

        storage_side[5].turn("z", -1, -1)

        storage_turned_side = []
        for x in range(6):
            for y in range(3):
                storage_turned_side.append(copy.deepcopy(storage_side[x]))

        storage_turned_side[0].turn("y",-1,1)
        storage_turned_side[1].turn("y",-1,1)
        storage_turned_side[1].turn("y",-1,1)
        storage_turned_side[2].turn("y",-1,-1)

        storage_turned_side[3].turn("z",-1,1)
        storage_turned_side[4].turn("z",-1,1)
        storage_turned_side[4].turn("z",-1,1)
        storage_turned_side[5].turn("z",-1,-1)

        storage_turned_side[6].turn("y",-1,1)
        storage_turned_side[7].turn("y",-1,1)
        storage_turned_side[7].turn("y",-1,1)
        storage_turned_side[8].turn("y",-1,-1)

        storage_turned_side[9].turn("z",-1,1)
        storage_turned_side[10].turn("z",-1,1)
        storage_turned_side[10].turn("z",-1,1)
        storage_turned_side[11].turn("z",-1,-1)

        storage_turned_side[12].turn("x",-1,1)
        storage_turned_side[13].turn("x",-1,1)
        storage_turned_side[13].turn("x",-1,1)
        storage_turned_side[14].turn("x",-1,-1)

        storage_turned_side[15].turn("x",-1,1)
        storage_turned_side[16].turn("x",-1,1)
        storage_turned_side[16].turn("x",-1,1)
        storage_turned_side[17].turn("x",-1,-1)

        return storage_side + storage_turned_side

    def _match(self):
        #return False
        if self.base_cube is None or self.match_cube is None:
            raise ValueError("Input doesn't match")

        for cube in self._generate_cubes():
            for color in range(6):
                result = self.match_cube.is_match(self._next_set(cube, color))

                if result:
                    return True

        return False

    def _next_set(self, current_cube, set_num):
        local_cube = copy.deepcopy(current_cube)

        for side in Helper.CUBE_SIDES:
            current_side = local_cube.get_side(side)

            for x in range(self.cube_size):
                for y in range(self.cube_size):
                    if current_side[x][y] is not None:
                        current_side[x][y] = (current_side[x][y] + set_num) % 6

            local_cube.set_side(side, current_side)

        return local_cube

    #def _next_set(self, current_set, set_num):
    #    for x in range(self.cube_size):
    #        for y in range(self.cube_size):
    #            if current_set[x][y] is not None:
    #                current_set[x][y] = (current_set[x][y] + set_num) % 6
    #    return current_set

#main = PatternFinder(3)
#
#cube1 = RubiksCube(3)
#cube1.turn_x(0,1)
#cube1.turn_x(2,1)
#cube1.turn_z(0,1)
#cube1.turn_z(1,1)
#cube1.turn_x(0,-1)
#cube1.turn_x(2,-1)
#
#cube2 = RubiksCube(3, False)
#
#color = 2
#cube2.set_front([[color, None, None],[color, color, None],[color, None, None]])
#cube2.set_left([[color+1, color+1, color+1],[None, color+1, None],[None, None, None]])
#
#main.set_base_cube(cube1)
#main.set_matching_cube(cube2)
#
#print main._match()
#
#a = RubiksCubeConverter.to_visual_cube(cube1)
#b = RubiksCubeConverter.to_visual_cube(cube2)