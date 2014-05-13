from helper import Helper


class PatternFinder:

    def __init__(self, cube_size):
        self.cube_size = cube_size
        self.base_cube = None
        self.match_cube = None

    def set_base_cube(self, cube):
        if cube.get_size() == self.cube_size:
            self.base_cube = cube
        else:
            raise Exception("Cube size doesn't match")

    def set_matching_cube(self, cube):
        if cube.get_size() == self.cube_size:
            self.match_cube = cube
        else:
            raise Exception("Cube size doesn't match")

    def _match(self):
        return False
        #if self.base_cube is None or self.match_cube is None:
        #    raise ValueError("Input doesn't match")
        #
        #for side in Helper.CUBE_SIDES:
        #    base_side = self.base_cube.get_side(side)
        #    match_side = self.match_cube.get_side(side)
        #    for x in range(self.cube_size):
        #        for y in range(self.cube_size):
        #            if base_side[x][y] != match_side[x][y]:
        #                return False
        return True

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





