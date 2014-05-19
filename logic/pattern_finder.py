from visual import *
from helper import Helper
from logic.rubiks_cube_converter import RubiksCubeConverter
from objects.cube.rubiks_cube import RubiksCube


class PatternFinder:

    def __init__(self, cube_size):
        self.cube_size = cube_size
        self.base_cube = None
        self.base_turn_cube = None
        self.match_cube = None
        self.match_turn_cube = None

    def set_base_cube(self, cube):
        if cube.get_size() == self.cube_size:
            self.base_cube = cube
        else:
            raise Exception("Cube size doesn't match")

    def set_base_turn_cube(self, turn_cube):
        if turn_cube is not None:
            self.base_turn_cube = turn_cube

    def set_matching_cube(self, cube):
        if cube.get_size() == self.cube_size:
            self.match_cube = cube
        else:
            raise Exception("Cube size doesn't match")

    def set_match_turn_cube(self, turn_cube):
        if turn_cube is not None:
            self.base_match_cube = turn_cube

    def _match(self):
        #return False
        if self.base_cube is None or self.match_cube is None:
            raise ValueError("Input doesn't match")

        for color in range(6):
            storage = []

            for side in Helper.CUBE_SIDES:
                base_side = self.base_cube.get_side(side)
                match_side = self._next_set(self.match_cube.get_side(side), color)

                storage.append(self._match_side(base_side, match_side))

            print storage
            if all(storage):
                return True

        return False

    def _match_side(self, side_a, side_b):
        for x in range(self.cube_size):
            for y in range(self.cube_size):
                if side_b[x][y] is None:
                    continue

                if side_a[x][y] != side_b[x][y]:
                    return False
        return True

    def _next_set(self, current_set, set_num):
        for x in range(self.cube_size):
            for y in range(self.cube_size):
                if current_set[x][y] is not None:
                    current_set[x][y] = ( current_set[x][y] + set_num ) % 6
        return current_set

    def _turn_cube(self):
        if self._match():
            return True

        for side in range(5):
            if side == 0:
                self._turn_step("y", "x")
            elif side == 1:
                self._turn_step("y", "z")
            elif side == 2:
                self._turn_step("y", "x")
            elif side == 3:
                self._turn_step("z", "y")
            elif side == 4:
                self.base_cube.turn("z", -1, 1)
                self._turn_step("z", "y")
        return False

    def _turn_step(self, axis, next_axis):
        self.base_cube.turn(axis, -1, 1)

        if self._match():
            return True

        for x in range(3):
            self.base_cube.turn(next_axis, -1, 1)

            if self._match():
                return True



main = PatternFinder(3)

cube1 = RubiksCube(3)
cube1.turn_x(0,1)
cube1.turn_x(2,1)
cube1.turn_z(0,1)
cube1.turn_z(1,1)
cube1.turn_x(0,-1)
cube1.turn_x(2,-1)

cube2 = RubiksCube(3, False)

color = 2
cube2.set_front([[color, None, None],[color, color, None],[color, None, None]])
cube2.set_left([[color+1, color+1, color+1],[None, color+1, None],[None, None, None]])

main.set_base_cube(cube1)
main.set_matching_cube(cube2)

print main._match()

a = RubiksCubeConverter.to_visual_cube(cube1)
b = RubiksCubeConverter.to_visual_cube(cube2)