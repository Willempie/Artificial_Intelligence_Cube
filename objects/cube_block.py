class CubeBlock:

    def __init__(self):
        self._front = None
        self._back = None
        self._top = None
        self._bottom = None
        self._left = None
        self._right = None

    def set_front(self, color):
        self._front = color

    def set_back(self, color):
        self._back = color

    def set_top(self, color):
        self._top = color

    def set_bottom(self, color):
        self._bottom = color

    def set_left(self, color):
        self._left = color

    def set_right(self, color):
        self._right = color

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
