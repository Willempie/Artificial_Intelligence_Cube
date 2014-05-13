from visual import *


class CubeDisplay():

    __L = 500  # length for window
    __d = 50

    __display = None

    def __init__(self, w):
        window_size = w.win.GetSize()
        y = window_size.y-self.__L

        # init display
        self.__display = display(window=w, x=10, y=y, width=self.__L-2*self.__d,
                                 height=self.__L-2*self.__d,
                                 #background=color.gray(0.8), range=(25, 25, 25), forward=(0, 1, 2),
                                 background=color.gray(0.8), range=(25, 25, 25),
                                 lights=[], ambient=color.gray(1), userzoom = False)

    def get_display(self):
        return self.__display