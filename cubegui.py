from functools import partial
from visual import *
from visual.controls import *
from gui_items import *
from keyboard_handler import *
import wx


class CubeGui:

    __L = 380  # length for window
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

    def display_gui(self):
        """
            # set the display for the cube
        """
        self.__display = display(window=self.__w, x=self.__d, y=self.__d, width=self.__L-2*self.__d,
                                 height=self.__L-2*self.__d, range=(25, 25, 25), forward=(0, 1, 2), background=color.gray(0.2))


        '''scene2 = display(title='Examples of Tetrahedrons',
            x=0, y=0, width=600, height=200,
                center=(5,0,0), background=(0, 1, 1))'''


    def get_window(self):
        return self.__w

    def get_window_frame(self):
        """
            # returns the window's frame
        """
        return self.__w.win

    def set_display(self):
        self.__display = None

    def get_display_frame(self):
        """
            # returns the displays frame
        """
        return self.__display.win

    def add_gui_items(self):
        #create panel
        self.__control_panel = self.__w.panel

        #testingthis
        test_items = GuiItems()

        my_button = test_items.gen_button(self.__control_panel, "Test button", self.__L+10, 15)
        test_items.bind_element(my_button, wx.EVT_BUTTON, self.test_bind_method)
        '''test_items.gen_radiobox(p, 1.0*self.__L, 0.3*self.__L, (0.25*self.__L, 0.25*self.__L), wx.RA_SPECIFY_ROWS, ['Red', 'Cyan'])
        slider = test_items.gen_slider(p, (1.0*self.__L, 0.8*self.__L), (0.9*self.__L, 20), 0, 100)

        slider_method = getattr(test_items, "test")
        test_items.bind_element(slider, wx.EVT_SCROLL, slider_method)
        self.__bbutton = my_button
        test_items.bind_element(self.__bbutton, wx.EVT_BUTTON, slider_method)
        test_items.bind_element(self.__bbutton, wx.EVT_ENTER_WINDOW, self.onMouseOver)'''

    def test_bind_method(self, evt):
        print(self.__control_panel)
        print(self.__w)
        print(self.__display)

    def gen_gui_menu(self):
        return