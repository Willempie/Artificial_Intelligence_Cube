from visual import *
from my_cube import MyCube
from my_box import MyBox


class MyDisplay(display):
    L = 320  # length for window
    d = 20

    def __init__(self):
        display.__init__(self)

        #initialize gui
        w = window(width=2*(self.L+window.dwidth), height=self.L+window.dheight+window.menuheight, menus=True,
                   title='Artificial Intelligence Cube')

        #display for the cube
        display(window=w, x=self.d, y=self.d, width=self.L-2*self.d, height=self.L-2*self.d, forward=-vector(0, 1, 2))

        self.lights = [1]
        self.ambient = color.gray(1)

        my_cube = MyCube(3, 2)
        #x.set_cube_color(color.magenta)


        my_cube.turn_z(1, 1)
        my_cube.turn_y(1, 1)
        my_cube.turn_x(1, 1)

        my_cube.turn_y(1, -1)
        my_cube.turn_z(1, -1)

        my_cube.turn_x(1, -1)





