from visual import *
from object_visual.v_cube import VCube
from object_visual.v_cube_block import VCubeBlock
from my_visual.my_cube import MyCube
from objects.cube import Cube
from objects.cube_block import CubeBlock


class MyDisplay(display):

    def __init__(self):
        display.__init__(self)
        '''
        #initialize gui
        w = window(width=2*(self.L+window.dwidth), height=self.L+window.dheight+window.menuheight, menus=True,
                   title='Artificial Intelligence Cube')

        #display for the cube
        display(window=w, x=self.d, y=self.d, width=self.L-2*self.d, height=self.L-2*self.d, forward=-vector(0, 1, 2))
        '''
        self.lights = [1]
        self.ambient = color.gray(1)
        self.background = color.gray(0.2)




        self.lights = []
        self.ambient = color.gray(1)
        self.background = color.gray(0.2)

        self.current_key = None
        self.action = False

        self.cube = VCube(3)

        self.bind('keydown', self.keyInput)
        self.bind('keyup', self.keyRelease)

    def keyInput(self, evt):
        s = evt.key
        if evt.ctrl:
            direction = -1
        else:
            direction = 1

        if self.current_key is None and self.action is False:
            self.current_key = s
            rate(self.cube.fps)
            if s == 'x':
                self.cube.turn_x(random.randint(0, 3), direction)
            if s == 'y':
                self.cube.turn_y(random.randint(0, 3), direction)
            if s == 'z':
                self.cube.turn_z(random.randint(0, 3), direction)
            rate(self.cube.fps)
        else:
            return

    def keyRelease(self, evt):
        self.current_key = None




