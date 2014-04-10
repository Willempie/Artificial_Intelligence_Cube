from b_rubiks_cube import BRubiksCube
from cube import Cube
from helper import Helper


class RubiksCube(BRubiksCube):

    def __init__(self, size=None, reset_array=True):
        BRubiksCube.__init__(self)

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
                    self._array[x][y][z] = Cube()

        self.set_left(1)
        self.set_right(2)
        self.set_bottom(3)
        self.set_top(4)
        self.set_back(5)
        self.set_front(6)

    def get_size(self):
        return self._dimension

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

    def _set_side(self, side, input_color):
        for x in xrange(self._dimension):
            for y in xrange(self._dimension):
                if isinstance(input_color, list):
                    color = input_color[x][y]
                else:
                    color = input_color

                if side == "Front":
                    self._array[x][y][self._dimension-1].set_front(color)
                if side == "Back":
                    self._array[x][y][0].set_back(color)
                if side == "Top":
                    self._array[x][self._dimension-1][y].set_top(color)
                if side == "Bottom":
                    self._array[x][0][y].set_bottom(color)
                if side == "Left":
                    self._array[0][x][y].set_left(color)
                if side == "Right":
                    self._array[self._dimension-1][x][y].set_right(color)

    def _get_side(self, side):
        array = [[None for k in xrange(self._dimension)] for i in xrange(self._dimension)]

        for x in xrange(self._dimension):
            for y in xrange(self._dimension):
                if side == "Front":
                    array[x][y] = self._array[x][y][self._dimension-1].get_front()
                if side == "Back":
                    array[x][y] = self._array[x][y][0].get_back()
                if side == "Top":
                    array[x][y] = self._array[x][self._dimension-1][y].get_top()
                if side == "Bottom":
                    array[x][y] = self._array[x][0][y].get_bottom()
                if side == "Left":
                    array[x][y] = self._array[0][x][y].get_left()
                if side == "Right":
                    array[x][y] = self._array[self._dimension-1][x][y].get_right()
        return array

    def _check_side(self, side):
        if side == "Front":
            array = self.get_front()
        if side == "Back":
            array = self.get_back()
        if side == "Top":
            array = self.get_top()
        if side == "Bottom":
            array = self.get_bottom()
        if side == "Left":
            array = self.get_left()
        if side == "Right":
            array = self.get_right()

        return Helper.array_2d_all_same(array, self._dimension)

    def solved(self):
        return self.check_top() and \
               self.check_bottom() and \
               self.check_front() and \
               self.check_back() and \
               self.check_left() and \
               self.check_right()

    def turn_x(self, index, direction):
        self._rotate_array('x', index, direction)

    def turn_y(self, index, direction):
        self._rotate_array('y', index, direction)

    def turn_z(self, index, direction):
        self._rotate_array('z', index, direction)

    def set_front(self, color):
        self._set_side("Front", color)

    def get_front(self):
        return self._get_side("Front")

    def check_front(self):
        return self._check_side("Front")

    def set_back(self, color):
        self._set_side("Back", color)

    def get_back(self):
        return self._get_side("Back")

    def check_back(self):
        return self._check_side("Back")

    def set_top(self, color):
        self._set_side("Top", color)

    def get_top(self):
        return self._get_side("Top")

    def check_top(self):
        return  self._check_side("Top")

    def set_bottom(self, color):
        self._set_side("Bottom", color)

    def get_bottom(self):
        return self._get_side("Bottom")

    def check_bottom(self):
        return self._check_side("Bottom")

    def set_left(self, color):
        self._set_side("Left", color)

    def get_left(self):
        return self._get_side("Left")

    def check_left(self):
        return self._check_side("Left")

    def set_right(self, color):
        self._set_side("Right", color)

    def get_right(self):
        return self._get_side("Right")

    def check_right(self):
        return self._check_side("Right")

    def my_print(self):
        print("Front")
        print(self.get_front())
        print("Back")
        print(self.get_back())
        print("Top")
        print(self.get_top())
        print("Bottom")
        print(self.get_bottom())
        print("Left")
        print(self.get_left())
        print("Right")
        print(self.get_right())