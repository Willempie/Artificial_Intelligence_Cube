from visual import *
from b_fps import BFps
from b_v_cube import BVCube
from objects.cube.rubiks_cube import RubiksCube
from v_cube import VCube


class VRubiksCube(RubiksCube, BVCube, BFps):

    def __init__(self, cube_size=2, block_size=None, start_pos=None, block_color=None):
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

        self.reset_array()

    def reset_array(self):
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

        # set side colors
        for x in xrange(self._dimension):
            for y in xrange(self._dimension):
                self._array[0][x][y].set_left(color.blue)
                self._array[self._dimension-1][x][y].set_right(color.green)

                self._array[x][0][y].set_bottom(color.orange)
                self._array[x][self._dimension-1][y].set_top(color.red)

                self._array[x][y][0].set_back(color.yellow)
                self._array[x][y][self._dimension-1].set_front(color.white)


    def set_cube_color(self, cube_color):
        for x in xrange(self._dimension):
            for y in xrange(self._dimension):
                for z in xrange(self._dimension):
                    self._array[x][y][z].set_color(cube_color)

    def turn_x(self, index, direction):
        for r in xrange(self.fps):
            rate(self.rate)
            for x in xrange(self._dimension):
                for y in xrange(self._dimension):
                    self._array[index][x][y].rotate(self.degrees90/self.fps,
                                                    vector(direction*-1, 0, 0),
                                                    self._pos)
        RubiksCube.turn_x(self, index, direction)

    def turn_y(self, index, direction):
        for r in xrange(self.fps):
            rate(self.rate)
            for x in xrange(self._dimension):
                for y in xrange(self._dimension):
                    self._array[x][index][y].rotate(self.degrees90/self.fps,
                                                    vector(0, direction*-1, 0),
                                                    self._pos)
        RubiksCube.turn_y(self, index, direction)

    def turn_z(self, index, direction):
        for r in xrange(self.fps):
            rate(self.rate)
            for x in xrange(self._dimension):
                for y in xrange(self._dimension):
                    self._array[x][y][index].rotate(self.degrees90/self.fps,
                                                    vector(0, 0, direction*-1),
                                                    self._pos)
        RubiksCube.turn_z(self, index, direction)