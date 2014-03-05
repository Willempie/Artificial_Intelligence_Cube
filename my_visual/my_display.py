from visual import *
from my_cube import MyCube
from my_box import MyBox


class MyDisplay(display):

    def __init__(self):
        display.__init__(self)
        self.lights = []
        self.ambient = color.gray(1)

        my_cube = MyCube(3, 2)
        #x.set_cube_color(color.magenta)


        my_cube.turn_z(1, 1)
        my_cube.turn_y(1, 1)
        my_cube.turn_x(1, 1)

        my_cube.turn_y(1, -1)
        my_cube.turn_z(1, -1)

        my_cube.turn_x(1, -1)





