from visual import *
from b_fps import BFps
from b_v_cube import BVCube
from objects.cube.rubiks_cube import RubiksCube
from v_cube import VCube
from helper import Helper

class VRubiksCube(RubiksCube, BVCube, BFps):

    def __init__(self, cube_size=2, block_size=None, start_pos=None, block_color=None, set_colors=True):
        RubiksCube.__init__(self, cube_size, False)
        BVCube.__init__(self, start_pos, cube_size)
        BFps.__init__(self)

        if block_size is None or block_size < 2:
            self._block_size = 2
        else:
            self._block_size = block_size

        if block_color is None:
            self._block_color = color.gray(0.4)
        else:
            self._block_color = block_color

        start_point = self._dimension*self._block_size/2
        start_vector = self._pos - vector(start_point, start_point, start_point)
        half_block = vector(self._block_size/2, self._block_size/2, self._block_size/2)

        # generate all the cubes
        for x in xrange(self._dimension):
            for y in xrange(self._dimension):
                for z in xrange(self._dimension):
                    current_vector = vector(self._block_size*x, self._block_size*y, self._block_size*z)
                    current_block_pos = start_vector + half_block + current_vector

                    self._array[x][y][z] = VCube(current_block_pos,self._block_color,self._block_size*2)

        self.reset_array(set_colors)

    def reset_array(self, set_colors):
        # set side colors
        for side in Helper.CUBE_SIDES:
            if set_colors:
                self.set_side(side, Helper.CUBE_COLOR[Helper.CUBE_SIDES.index(side)], True)
            else:
                self.set_side(side, color.black, True)

    def set_part(self, side, x, y, color, create_mode=False):
        if create_mode:
            RubiksCube.set_part(self, side, x, y, color)
        else:
            if side == "Front":
                self._array[x][y][self._dimension-1].get_front().color = color
            if side == "Back":
                self._array[x][y][0].get_back().color = color
            if side == "Top":
                self._array[x][self._dimension-1][y].get_top().color = color
            if side == "Bottom":
                self._array[x][0][y].get_bottom().color = color
            if side == "Left":
                self._array[0][x][y].get_left().color = color
            if side == "Right":
                self._array[self._dimension-1][x][y].get_right().color = color

    def set_side(self, side, input_color, create_mode=False):
        for x in xrange(self._dimension):
            for y in xrange(self._dimension):
                if isinstance(input_color, list):
                    color = input_color[x][y]
                else:
                    color = input_color

                self.set_part(side, x, y, color, create_mode)

    def set_cube_color(self, cube_color):
        for x in xrange(self._dimension):
            for y in xrange(self._dimension):
                for z in xrange(self._dimension):
                    self._array[x][y][z].set_color(cube_color)

    def execute_steps(self, step_list):
        for step in step_list:
            self.turn(step.axis, step.rows, step.direction)

    def turn(self, xyz, index, direction):
        if xyz == 'x':
            self.turn_x(index, direction)
        if xyz == 'y':
            self.turn_y(index, direction)
        if xyz == 'z':
            self.turn_z(index, direction)

    def turn_x(self, index, direction):
        for r in xrange(self.fps):
            rate(self.rate)
            for x in xrange(self._dimension):
                for y in xrange(self._dimension):
                    if index >= 0:
                        self._array[index][x][y].rotate(self.degrees90/self.fps,
                                                        vector(direction*-1, 0, 0),
                                                        self._pos)
                    else:
                        for rows in range(self._dimension):
                            self._array[rows][x][y].rotate(self.degrees90/self.fps,
                                                            vector(direction*-1, 0, 0),
                                                            self._pos)
        if index >= 0:
            RubiksCube.turn_x(self, index, direction)
        else:
            for rows in range(self._dimension):
                RubiksCube.turn_x(self, rows, direction)

    def turn_y(self, index, direction):
        for r in xrange(self.fps):
            rate(self.rate)
            for x in xrange(self._dimension):
                for y in xrange(self._dimension):
                    if index >= 0:
                        self._array[x][index][y].rotate(self.degrees90/self.fps,
                                                        vector(0, direction*-1, 0),
                                                        self._pos)
                    else:
                        for rows in range(self._dimension):
                            self._array[x][rows][y].rotate(self.degrees90/self.fps,
                                                            vector(0, direction*-1, 0),
                                                            self._pos)
        if index >= 0:
            RubiksCube.turn_y(self, index, direction)
        else:
            for rows in range(self._dimension):
                RubiksCube.turn_y(self, rows, direction)

    def turn_z(self, index, direction):
        for r in xrange(self.fps):
            rate(self.rate)
            for x in xrange(self._dimension):
                for y in xrange(self._dimension):
                    if index >= 0:
                        self._array[x][y][index].rotate(self.degrees90/self.fps,
                                                        vector(0, 0, direction*-1),
                                                        self._pos)
                    else:
                        for rows in range(self._dimension):
                            self._array[x][y][rows].rotate(self.degrees90/self.fps,
                                                            vector(0, 0, direction*-1),
                                                            self._pos)
        if index >= 0:
            RubiksCube.turn_z(self, index, direction)
        else:
            for rows in range(self._dimension):
                RubiksCube.turn_z(self, rows, direction)