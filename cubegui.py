from visual import *


class CubeGui:

    __L = 400  # length for window
    __d = 20

    __w = None
    __display = None

    __control_panel = None

    def __init__(self, title):
        """
            # initialize GUI
        """
        self.__w = window(width=2*(self.__L+window.dwidth), height=1.5*(self.__L+window.dheight+window.menuheight),
                          menus=True, title=title)

    def get_window(self):
        return self.__w

    def get_window_frame(self):
        """
            # returns the window's frame
        """
        return self.__w.win

    def get_window_panel(self):
        """
            # return the window's panel
        """
        return self.__w.panel

    def get_window_width(self):
        return self.__L