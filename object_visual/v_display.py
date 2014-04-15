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
    cube = None

    def __init__(self):
        '''
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

        # generate dropdown menu
        combo_box_items = []
        for size in range(self.cube.get_size()):
            combo_box_items.append(str(size+1))
        combo_box = gui_items.gen_combobox((150, 10), (150, -1), combo_box_items)
        # bind dropdown menu
        gui_items.bind_element(combo_box, wx.EVT_COMBOBOX, cube_handler.set_index)

        # generate radiobuttons for direction
        directions = ['Clockwise', 'Counterclockwise']
        radio_buttons = gui_items.gen_radiobox(150, 50, (180, -1), wx.RA_SPECIFY_ROWS, directions)
        # bind radiobuttons
        gui_items.bind_element(radio_buttons, wx.EVT_RADIOBOX, cube_handler.set_direction)

        mouse_handler = MouseHandler(cube_display.get_display())
        '''

    def create_input_display(self):

        # create cube display
        cube_display = CubeDisplay()

        # create GUI
        cube_gui = CubeGui("Artificial Intelligence Cube")

        # GUI items
        gui_items = GuiItems(cube_gui, cube_gui.get_window_panel())
        combo_box_items = ['Rood', 'Blauw', 'Groen', 'Geel', 'Oranje', 'Wit']
        combo_box = gui_items.gen_combobox((20, 10), (150, -1), combo_box_items)
        combo_box.SetSelection(0)

        # generate cube
        self.cube = VRubiksCube(3, None, None, None, True)

        # mouse handler
        mouse_handler = MouseHandler(cube_display.get_display())
        mouse_handler.bind_mouse_click(self.cube, combo_box)

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