from visual import *
from object_visual.v_rubiks_cube import VRubiksCube
from cubegui import *
from cube_display import *
from cube_handler import *
from gui_items import *
from keyboard_handler import *
from mouse_handler import *


class VDisplay():

    __default_button_width = 88
    __default_button_height = 26

    def __init__(self):

        # create cube display
        cube_display = CubeDisplay()

        # create GUI
        cube_gui = CubeGui("Artificial Intelligence Cube")

        # generate cube
        self.cube = VRubiksCube(3)

        # create cube handler
        cube_handler = CubeHandler(self.cube)

        # create keyboard handler
        keyboard_handler = KeyboardHandler(cube_display.get_display(), self.cube)
        # bind keyboard keys to display
        displayc = cube_display.get_display()
        displayc.bind('keydown', keyboard_handler.on_key_down)

        # generate GUI items
        gui_items = GuiItems(cube_gui, cube_gui.get_window_panel())
        # generate rotate buttons
        x_button = gui_items.gen_button("- Turn X - ", 10, 10 + (self.__default_button_height*0))  # X
        y_button = gui_items.gen_button("- Turn Y -", 10, 10 + self.__default_button_height)       # Y
        z_button = gui_items.gen_button("- Turn Z -", 10, 10 + (self.__default_button_height*2))   # Z
        # bind rotate buttons
        gui_items.bind_element(x_button, wx.EVT_BUTTON, cube_handler.turn_x)  # X
        gui_items.bind_element(y_button, wx.EVT_BUTTON, cube_handler.turn_y)  # Y
        gui_items.bind_element(z_button, wx.EVT_BUTTON, cube_handler.turn_z)  # Z

        mouse_handler = MouseHandler(cube_display.get_display())



    '''
    def __init__(self):
        self.lights = []
        self.ambient = color.gray(1)
        self.background = color.gray(0.2)

        # keyboard event handler
        keyboard_handler = KeyboardHandler(cube_gui.get_window_frame(), self.cube, cube_gui.get_window_frame())
        keyboard_handler.bind_key(wx.EVT_KEY_DOWN, keyboard_handler.on_key_down)

        focus_handler = FocusHandler(keyboard_handler.get_panel())
        keyboard_handler.bind_key(wx.EVT_KILL_FOCUS, focus_handler.focus_kill_function)
        keyboard_handler.bind_key(wx.EVT_SET_FOCUS, focus_handler.focus_set_function)'''