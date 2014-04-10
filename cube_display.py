from visual import *


class CubeDisplay():

    __L = 380  # length for window
    __d = 20

    __display = None

    def __init__(self):
        # init display
        self.__display = display(x=self.__d, y=self.__d, width=self.__L-2*self.__d,
                                 height=self.__L-2*self.__d,
                                 background=color.gray(0.2))
        '''range=(25, 25, 25), forward=(0, 1, 2),'''

    def get_display(self):
        return self.__display