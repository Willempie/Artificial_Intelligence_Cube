from cube_block import CubeBlock


class Cube:

    def __init__(self, size=None, reset_array=True):

        if size is None or size < 2:
            self._dimension = 2
        else:
            self._dimension = size

        self._array = [[[None
                         for k in xrange(self._dimension)]
                        for i in xrange(self._dimension)]
                       for j in xrange(self._dimension)]

        if reset_array:
            self.reset_array()

    def reset_array(self):
        # generate all the cubes
        for x in xrange(self._dimension):
            for y in xrange(self._dimension):
                for z in xrange(self._dimension):
                    self._array[x][y][z] = CubeBlock()

        # set side colors
        for x in xrange(self._dimension):
            for y in xrange(self._dimension):
                self._array[0][x][y].set_left(1)
                self._array[self._dimension-1][x][y].set_right(2)

                self._array[x][0][y].set_bottom(3)
                self._array[x][self._dimension-1][y].set_top(4)

                self._array[x][y][0].set_back(5)
                self._array[x][y][self._dimension-1].set_front(6)

    def _rotate_array(self, xyz, index, direction):
        storage = [[None for k in xrange(self._dimension)] for j in xrange(self._dimension)]

        for x in xrange(self._dimension):
            for y in xrange(self._dimension):
                if xyz == 'x':
                    storage[x][y] = self._array[index][x][y]
                if xyz == 'y':
                    storage[x][y] = self._array[y][index][x]
                if xyz == 'z':
                    storage[x][y] = self._array[x][y][index]

        if direction == -1:
            storage = zip(*storage)[::-1]
        if direction == 1:
            storage = zip(*storage[::-1])

        for x in xrange(self._dimension):
            for y in xrange(self._dimension):
                if xyz == 'x':
                    self._array[index][x][y] = storage[x][y]
                if xyz == 'y':
                    self._array[y][index][x] = storage[x][y]
                if xyz == 'z':
                    self._array[x][y][index] = storage[x][y]

    def turn_x(self, index, direction):
        self._rotate_array('x', index, direction)

    def turn_y(self, index, direction):
        self._rotate_array('y', index, direction)

    def turn_z(self, index, direction):
        self._rotate_array('z', index, direction)

    def my_print(self):
        return
