from numpy import random
from visual_common.create_display import rate


class KeyboardHandler():

    __display = None
    __cube = None

    __x_key = "x"
    __y_key = "y"
    __z_key = "z"

    __direction = 1

    def __init__(self, display, cube):
        self.__display = display
        self.__cube = cube

    def set_direction(self, event):
        if event.ctrl:
            self.__direction = -1
        else:
            self.__direction = 1

    def on_key_down(self, event):
        key = event.key

        self.set_direction(event)  # set direction

        rate(self.__cube.fps)
        if key == self.__x_key:
            self.__cube.turn_x(random.randint(0, 3), self.__direction)
        elif key == self.__y_key:
            self.__cube.turn_y(random.randint(0, 3), self.__direction)
        elif key == self.__z_key:
            self.__cube.turn_z(random.randint(0, 3), self.__direction)
        rate(self.__cube.fps)