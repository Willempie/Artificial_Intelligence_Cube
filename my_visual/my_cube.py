from visual import *
from my_box import MyBox


class MyCube:

    __cube_size = None
    __block_size = None
    __block_color = None
    __center = None
    __array = None

    __fps = 24
    __angle = pi / 2

    def __init__(self, cube_size=None, block_size=None, start_pos=None, block_color=None):

        if cube_size is None or cube_size < 2:
            self.__cube_size = 2
        else:
            self.__cube_size = cube_size

        if block_size is None or block_size <= 1:
            self.__block_size = 2
        else:
            self.__block_size = block_size

        if start_pos is None:
            self.__center = vector(0, 0, 0)
        else:
            self.__center = start_pos

        if block_color is None:
            self.__block_color = color.gray(0.4)
        else:
            self.__block_color = block_color

        self.__array = [[[None
                          for k in xrange(self.__cube_size)]
                         for i in xrange(self.__cube_size)]
                        for j in xrange(self.__cube_size)]

        start_point = self.__cube_size*self.__block_size/2
        start_vector = self.__center - vector(start_point, start_point, start_point)
        half_block = vector(self.__block_size/2, self.__block_size/2, self.__block_size/2)
        print(start_vector)
        print(half_block)

        # generate all the cubes
        for x in xrange(self.__cube_size):
            for y in xrange(self.__cube_size):
                for z in xrange(self.__cube_size):
                    current_vector = vector(self.__block_size*x, self.__block_size*y, self.__block_size*z)
                    current_block_pos = start_vector + half_block + current_vector

                    my_box = MyBox(current_block_pos,self.__block_color,self.__block_size*2)
                    self.__array[x][y][z] = my_box

        # set side colors
        for x in xrange(self.__cube_size):
            for y in xrange(self.__cube_size):
                self.__array[0][x][y].set_left(color.blue)
                self.__array[self.__cube_size-1][x][y].set_right(color.green)

                self.__array[x][0][y].set_bottom(color.orange)
                self.__array[x][self.__cube_size-1][y].set_top(color.red)

                self.__array[x][y][0].set_back(color.yellow)
                self.__array[x][y][self.__cube_size-1].set_front(color.white)

    def set_fps(self, fps):
        if fps > 0:
            self.__fps = fps

    def set_cube_color(self, cube_color):
        for x in xrange(self.__cube_size):
            for y in xrange(self.__cube_size):
                for z in xrange(self.__cube_size):
                    self.__array[x][y][z].color = cube_color

    def turn_x(self, index, direction):
        for r in xrange(self.__fps):
            rate(self.__fps)
            for x in xrange(self.__cube_size):
                for y in xrange(self.__cube_size):
                    self.__array[index][x][y].rotate(self.__angle/self.__fps,
                                                     vector(direction*-1, 0, 0),
                                                     self.__center)
        self.turn_x_array(index, direction*-1)

    def turn_y(self, index, direction):
        for r in xrange(self.__fps):
            rate(self.__fps)
            for x in xrange(self.__cube_size):
                for y in xrange(self.__cube_size):
                    self.__array[x][index][y].rotate(self.__angle/self.__fps,
                                                     vector(0, direction*-1, 0),
                                                     self.__center)
        self.turn_y_array(index, direction)

    def turn_z(self, index, direction):
        for r in xrange(self.__fps):
            rate(self.__fps)
            for x in xrange(self.__cube_size):
                for y in xrange(self.__cube_size):
                    self.__array[x][y][index].rotate(self.__angle/self.__fps,
                                                     vector(0, 0, direction*-1),
                                                     self.__center)
        self.turn_z_array(index, direction)

    def turn_x_array(self, index, direction):
        storage = [[None for k in xrange(self.__cube_size)] for j in xrange(self.__cube_size)]
        for x in xrange(self.__cube_size):
            for y in xrange(self.__cube_size):
                storage[x][y] = self.__array[index][x][y]

        storage = zip(*storage[::direction])

        for x in xrange(self.__cube_size):
            for y in xrange(self.__cube_size):
                self.__array[index][x][y] = storage[x][y]

    def turn_y_array(self, index, direction):
        storage = [[None for k in xrange(self.__cube_size)] for j in xrange(self.__cube_size)]
        for x in xrange(self.__cube_size):
            for y in xrange(self.__cube_size):
                storage[x][y] = self.__array[x][index][y]

        storage = zip(*storage[::direction])

        for x in xrange(self.__cube_size):
            for y in xrange(self.__cube_size):
                self.__array[x][index][y] = storage[x][y]

    def turn_z_array(self, index, direction):
        storage = [[None for k in xrange(self.__cube_size)] for j in xrange(self.__cube_size)]
        for x in xrange(self.__cube_size):
            for y in xrange(self.__cube_size):
                storage[x][y] = self.__array[x][y][index]

        storage = zip(*storage[::direction])

        for x in xrange(self.__cube_size):
            for y in xrange(self.__cube_size):
                self.__array[x][y][index] = storage[x][y]
        '''
        front = self._front.get_row_x(index)
        top = self.__top.get_row_x(index)
        back = self.__back.get_row_x(index)
        bottom = self.__bottom.get_row_x(index)

        if direction == self.CONST_DIRECTION[3]: #right
            self._front.set_row_x(index, bottom)
            self.__top.set_row_x(index, front)
            self.__back.set_row_x(index, top)
            self.__bottom.set_row_x(index, back)

            if index == 0:
                self.__right = zip(*self.__right[::-1])
            elif index == self.__size-1:
                self.__left = zip(*self.__left[::1])

        elif direction == self.CONST_DIRECTION[2]: #left
            self._front.set_row_x(index, top)
            self.__top.set_row_x(index, back)
            self.__back.set_row_x(index, bottom)
            self.__bottom.set_row_x(index, front)

        '''