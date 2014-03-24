from functools import partial
from visual import *
from visual.controls import *
from gui_items import *
import wx


class CubeGui:

    __L = 320  # length for window
    __d = 20
    __w = None
    __control_panel = None

    def __init__(self):

        #initialize gui
        self.__w = window(width=2*(self.__L+window.dwidth), height=self.__L+window.dheight+window.menuheight, menus=True
                          , title='Artificial Intelligence Cube')

    def display_gui(self):
        #display for the cube
        display(window=self.__w, x=self.__d, y=self.__d, width=self.__L-2*self.__d, height=self.__L-2*self.__d, forward=
                -vector(0, 1, 2))

    def add_gui_items(self):
        #create panel
        p = self.__w.panel

        #testingthis
        test_items = GuiItems()
        test_items.gen_button(p, "Test button", self.__L+10, 15)
        test_items.gen_radiobox(p, 1.0*self.__L, 0.3*self.__L, (0.25*self.__L, 0.25*self.__L), wx.RA_SPECIFY_ROWS, ['Red', 'Cyan'])
        slider = test_items.gen_slider(p, (1.0*self.__L, 0.8*self.__L), (0.9*self.__L, 20), 0, 100)


        #add buttons
        #left = wx.Button(p, label='Rotate left', pos=(self.__L+10, 15))
        #left.Bind(wx.EVT_BUTTON, setleft)

    def gen_gui_menu(self):
        return