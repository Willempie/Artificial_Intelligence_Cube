from b_rubiks_cube import BRubiksCube
from cube import Cube
from helper import Helper


class RubiksCube(BRubiksCube):

    def __init__(self, size=None, set_color=True):
        BRubiksCube.__init__(self)

        #Minimum size is 2
        if size is None or size < 2:
            self._dimension = 2
        else:
            self._dimension = size

        #Generate empty array
        self._array = [[[None
                         for k in xrange(self._dimension)]
                        for i in xrange(self._dimension)]
                       for j in xrange(self._dimension)]

       # generate all the cubes
        for x in xrange(self._dimension):
            for y in xrange(self._dimension):
                for z in xrange(self._dimension):
                    self._array[x][y][z] = Cube()

        self.reset_array(set_color)

    def reset_array(self, set_color):
        #Generate the sides, all 0 if set_color==False
        counter = 0
        for side in Helper.CUBE_SIDES:
            if set_color:
                self.set_side(side, counter)
                counter += 1
            else:
                self.set_side(side, counter)

    def get_size(self):
        return self._dimension

    def _rotate_array(self, xyz, index, direction):
        #Rotate the storage array depending on axis, index and direction

        #Generate temp storage
        storage = [[None for k in xrange(self._dimension)] for j in xrange(self._dimension)]

        #Fetch current slice
        for x in xrange(self._dimension):
            for y in xrange(self._dimension):
                if xyz == 'x':
                    storage[x][y] = self._array[index][x][y]
                if xyz == 'y':
                    storage[x][y] = self._array[y][index][x]
                if xyz == 'z':
                    storage[x][y] = self._array[x][y][index]

        #Rotate current slice
        if direction == -1:
            storage = zip(*storage)[::-1]
        if direction == 1:
            storage = zip(*storage[::-1])

        #Rotate current slice parts
        for x in xrange(self._dimension):
            for y in xrange(self._dimension):
                storage[x][y].turn(xyz, direction)

        #Write back the new slice
        for x in xrange(self._dimension):
            for y in xrange(self._dimension):
                if xyz == 'x':
                    self._array[index][x][y] = storage[x][y]
                if xyz == 'y':
                    self._array[y][index][x] = storage[x][y]
                if xyz == 'z':
                    self._array[x][y][index] = storage[x][y]

    def set_side(self, side, input_color):
        #Set side depending on the side and input_color
        for x in xrange(self._dimension):
            for y in xrange(self._dimension):
                if isinstance(input_color, list):
                    color = input_color[x][y]
                else:
                    color = input_color

                self.set_part(side, x, y, color)

    def set_part(self, side, x, y, color):
        #Set a single part on a cube depending on the side, x, y, color.
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

    def get_side(self, side):
        #Get a complete side from the RubiksCube depending on the side
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
        #Checks if the given side has only 1 color
        array = self.get_side(side)
        return Helper.array_2d_all_same(array, self._dimension)

    def contains(self, item):
        #Checks if the this RubiksCube contains the given item and returns the [side, x, y]
        for side in Helper.CUBE_SIDES:
            array = self.get_side(side)
            for x in range(self._dimension):
                for y in range(self._dimension):
                    if array[x][y] == item:
                        return [side, x, y]
        return False

    def solved(self):
        #Checks if this RubiksCube is solved
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
        self.set_side("Front", color)

    def get_front(self):
        return self.get_side("Front")

    def check_front(self):
        return self._check_side("Front")

    def set_back(self, color):
        self.set_side("Back", color)

    def get_back(self):
        return self.get_side("Back")

    def check_back(self):
        return self._check_side("Back")

    def set_top(self, color):
        self.set_side("Top", color)

    def get_top(self):
        return self.get_side("Top")

    def check_top(self):
        return  self._check_side("Top")

    def set_bottom(self, color):
        self.set_side("Bottom", color)

    def get_bottom(self):
        return self.get_side("Bottom")

    def check_bottom(self):
        return self._check_side("Bottom")

    def set_left(self, color):
        self.set_side("Left", color)

    def get_left(self):
        return self.get_side("Left")

    def check_left(self):
        return self._check_side("Left")

    def set_right(self, color):
        self.set_side("Right", color)

    def get_right(self):
        return self.get_side("Right")

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