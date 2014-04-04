from numpy import random
from visual_common.create_display import rate


class CubeHandler():

    __cube = None
    __direction = 1

    def __init__(self, cube):
        self.__cube = cube

    def turn_x(self, event):
        rate(self.__cube.fps)
        self.__cube.turn_x(random.randint(0, 3), self.__direction)
        rate(self.__cube.fps)

    def turn_y(self, event):
        rate(self.__cube.fps)
        self.__cube.turn_z(random.randint(0, 3), self.__direction)
        rate(self.__cube.fps)

    def turn_z(self, event):
        rate(self.__cube.fps)
        self.__cube.turn_z(random.randint(0, 3), self.__direction)
        rate(self.__cube.fps)