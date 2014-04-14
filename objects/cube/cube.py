from b_cube import BCube
from helper import Helper

class Cube(BCube):

    def __init__(self):
        BCube.__init__(self)

        self._front = None
        self._back = None
        self._top = None
        self._bottom = None
        self._left = None
        self._right = None

    def set_side(self, side, item):
        if side in Helper.CUBE_SIDES:
            getattr(self, "set_"+side.lower())(item)

    def get_side(self, side):
        if side in Helper.CUBE_SIDES:
            return getattr(self, "get_"+side.lower())()

    def contains(self, item):
        for side in Helper.CUBE_SIDES:
            if item == self.get_side(side):
                return True
        return False

    def set_front(self, color):
        self._front = color

    def get_front(self):
        return self._front

    def set_back(self, color):
        self._back = color

    def get_back(self):
        return self._back

    def set_top(self, color):
        self._top = color

    def get_top(self):
        return self._top

    def set_bottom(self, color):
        self._bottom = color

    def get_bottom(self):
        return self._bottom

    def set_left(self, color):
        self._left = color

    def get_left(self):
        return self._left

    def set_right(self, color):
        self._right = color

    def get_right(self):
        return self._right

    def turn_x(self, direction):
        storage_front = self._front
        storage_top = self._top
        storage_back = self._back
        storage_bottom = self._bottom

        if direction == 1:
            self._front = storage_bottom
            self._top = storage_front
            self._back = storage_top
            self._bottom = storage_back
        elif direction == -1:
            self._front = storage_top
            self._top = storage_back
            self._back = storage_bottom
            self._bottom = storage_front

    def turn_y(self, direction):
        storage_left = self._left
        storage_back = self._back
        storage_right = self._right
        storage_front = self._front

        if direction == 1:
            self._left = storage_front
            self._back = storage_left
            self._right = storage_back
            self._front = storage_right
        elif direction == -1:
            self._left = storage_back
            self._back = storage_right
            self._right = storage_front
            self._front = storage_left

    def turn_z(self, direction):
        storage_top = self._top
        storage_right = self._right
        storage_bottom = self._bottom
        storage_left = self._left

        if direction == 1:
            self._top = storage_left
            self._right = storage_top
            self._bottom = storage_right
            self._left = storage_bottom
        elif direction == -1:
            self._top = storage_right
            self._right = storage_bottom
            self._bottom = storage_left
            self._left = storage_top

    def my_print(self):
        print("Top    "+str(self._top))
        print("Bottom "+str(self._bottom))
        print("Left   "+str(self._left))
        print("Right  "+str(self._right))
        print("Front  "+str(self._front))
        print("Back   "+str(self._back))