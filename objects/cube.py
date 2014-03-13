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

    def turn_x(self, index, direction):
        storage = [[None for k in xrange(self._dimension)] for j in xrange(self._dimension)]
        for x in xrange(self._dimension):
            for y in xrange(self._dimension):
                storage[x][y] = self._array[index][x][y]

        storage = zip(*storage[::direction])

        for x in xrange(self._dimension):
            for y in xrange(self._dimension):
                storage[x][y].turn_x(direction)
                self._array[index][x][y] = storage[x][y]

    def turn_y(self, index, direction):
        storage = [[None for k in xrange(self._dimension)] for j in xrange(self._dimension)]
        for x in xrange(self._dimension):
            for y in xrange(self._dimension):
                storage[x][y] = self._array[x][index][y]

        storage = zip(*storage[::direction])

        for x in xrange(self._dimension):
            for y in xrange(self._dimension):
                storage[x][y].turn_y(direction)
                self._array[x][index][y] = storage[x][y]

    def turn_z(self, index, direction):
        storage = [[None for k in xrange(self._dimension)] for j in xrange(self._dimension)]
        for x in xrange(self._dimension):
            for y in xrange(self._dimension):
                storage[x][y] = self._array[x][y][index]

        storage = zip(*storage[::direction])

        for x in xrange(self._dimension):
            for y in xrange(self._dimension):
                storage[x][y].turn_z(direction)
                self._array[x][y][index] = storage[x][y]

    def my_print(self):
        storage_left = [[None for k in xrange(self._dimension)] for j in xrange(self._dimension)]
        storage_right = [[None for k in xrange(self._dimension)] for j in xrange(self._dimension)]
        storage_top = [[None for k in xrange(self._dimension)] for j in xrange(self._dimension)]
        storage_bottom = [[None for k in xrange(self._dimension)] for j in xrange(self._dimension)]
        storage_front = [[None for k in xrange(self._dimension)] for j in xrange(self._dimension)]
        storage_back = [[None for k in xrange(self._dimension)] for j in xrange(self._dimension)]

        for x in xrange(self._dimension):
            for y in xrange(self._dimension):
                storage_left[x][y] = self._array[0][x][y]._left
                storage_right[x][y] = self._array[self._dimension-1][x][y]._right

                storage_bottom[x][y] = self._array[x][0][y]._bottom
                storage_top[x][y] = self._array[x][self._dimension-1][y]._top

                storage_back[x][y] = self._array[x][y][0]._back
                storage_front[x][y] = self._array[x][y][self._dimension-1]._front

        for x in xrange(self._dimension):
            print(storage_left[x])
        print("")
        for x in xrange(self._dimension):
            print(storage_right[x])
        print("")
        for x in xrange(self._dimension):
            print(storage_bottom[x])
        print("")
        for x in xrange(self._dimension):
            print(storage_top[x])
        print("")
        for x in xrange(self._dimension):
            print(storage_back[x])
        print("")
        for x in xrange(self._dimension):
            print(storage_front[x])
        print("")


