from visual import *
from object_visual.v_cube import VCube
from my_visual.my_cube import MyCube
from objects.cube import Cube
from objects.cube_block import CubeBlock


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
        self.background = color.gray(0.2)

        #hello = VCubeBlock()
        #hello.set_front(color.black)

        size = 2
        #x = MyCube(size,2)
        #x = VCube(size, 2)
        x = Cube(3)
        x.my_print()
        x.turn_z(0,1)
        print("")
        x.my_print()

        '''
        while True:
            self.waitfor('click')
            x.turn_x(random.randint(0, size-1), 1)
            x.turn_x(random.randint(0, size-1), -1)
            x.turn_y(random.randint(0, size-1), 1)
            x.turn_y(random.randint(0, size-1), -1)
            x.turn_z(random.randint(0, size-1), 1)
            x.turn_z(random.randint(0, size-1), -1)
        '''

        my_cube = VCube(4, 2)

        #while True:
            #self.waitfor('click')
            #my_cube.turn_x(0, -1)
            #my_cube.turn_x(1, -1)
            #my_cube.turn_x(2, -1)
            #my_cube.turn_x(3, -1)

            #self.waitfor('click')

            #my_cube.turn_y(0, 1)


        '''
        for x in xrange(my_cube._dimension):
            for y in xrange(my_cube._dimension):
                my_cube._array[1][x][y].v_frame.pos += vector(-16,0,0)
        '''




