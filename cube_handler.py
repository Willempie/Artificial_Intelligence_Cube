from visual_common.create_display import rate


class CubeHandler():

    __cube = None
    __direction = 1

    __index = 0

    def __init__(self, cube):
        self.__cube = cube

    def turn_x(self, event):
        rate(self.__cube.fps)
        self.__cube.turn_x(self.__index, self.__direction)
        rate(self.__cube.fps)

    def turn_y(self, event):
        rate(self.__cube.fps)
        self.__cube.turn_y(self.__index, self.__direction)
        rate(self.__cube.fps)

    def turn_z(self, event):
        rate(self.__cube.fps)
        self.__cube.turn_z(self.__index, self.__direction)
        rate(self.__cube.fps)

    def set_index(self, event):
        itemvalue = event.GetSelection()
        self.__index = itemvalue

    def set_direction(self, event):
        item = event.GetSelection()
        if item == 0:
            self.__direction = 1
        else:
            self.__direction = -1

    def solve(self, event):
        # SOLVE THE CUBE
        pass

