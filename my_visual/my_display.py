from visual import *
from object_visual.v_cube import VCube
from my_visual.my_cube import MyCube
from objects.cube import Cube
from objects.cube_block import CubeBlock


class MyDisplay(display):

    def __init__(self):
        display.__init__(self)
        self.lights = []
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

        #my_cube = VCube(4, 2)

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




