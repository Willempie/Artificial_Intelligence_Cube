from visual import *
from logic.handling.cube_storage import CubeStorage
from mouse_handler import MouseHandler
from object_visual.v_rubiks_cube import VRubiksCube
from cubegui import *
from cube_display import *
from cube_handler import *
from gui_items import *
from keyboard_handler import *


__author__ = 'Willem'


class SolveDisplay():

    __default_button_width = 88
    __default_button_height = 26

    def __init__(self):

        # create GUI
        self.cube_gui = CubeGui("Artificial Intelligence Cube")

        # create cube display
        self.cube_display = CubeDisplay(self.cube_gui.get_window(), False)

        #Cube Storage
        self._storage = CubeStorage(self, 2)

        # generate cube
        self.cube = VRubiksCube(2)

        # xml handler
        self.handle_xml = HandleFiles(self)

        # create cube handler
        cube_handler = CubeHandler(self.cube)

        self.create_gui_items(cube_handler, self.cube_gui)

        # create keyboard handler
        keyboard_handler = KeyboardHandler(self.cube_display.get_display(), self.cube)
        # bind keyboard keys to display
        displayc = self.cube_display.get_display()
        displayc.bind('keydown', keyboard_handler.on_key_down)

        mouse_handler = MouseHandler(self)

    def create_gui_items(self, cube_handler, cube_gui):

        # generate GUI items
        gui_items = GuiItems(self, cube_gui, cube_gui.get_window_panel())

        # generate GUI Menu
        gui_items.gen_menu(cube_gui.get_window())

        # generate rotate buttons
        x_button = gui_items.gen_button("- Turn X - ", 10, 10 + (self.__default_button_height*0))  # X
        y_button = gui_items.gen_button("- Turn Y -", 10, 10 + self.__default_button_height)       # Y
        z_button = gui_items.gen_button("- Turn Z -", 10, 10 + (self.__default_button_height*2))   # Z
        # bind rotate buttons
        gui_items.bind_element(x_button, wx.EVT_BUTTON, cube_handler.turn_x)  # X
        gui_items.bind_element(y_button, wx.EVT_BUTTON, cube_handler.turn_y)  # Y
        gui_items.bind_element(z_button, wx.EVT_BUTTON, cube_handler.turn_z)  # Z

        # generate solve button
        solve_button = gui_items.gen_button("Solve Cube!", 10, 10 + (self.__default_button_height*5))
        # bind solve button
        gui_items.bind_element(solve_button, wx.EVT_BUTTON, cube_handler.solve)

        # generate dropdown menu
        combo_box_items = []
        for size in range(self.cube.get_size()):
            combo_box_items.append(str(size+1))
        combo_box = gui_items.gen_combobox((150, 10), (150, -1), combo_box_items)
        combo_box.SetSelection(0)
        # bind dropdown menu
        gui_items.bind_element(combo_box, wx.EVT_COMBOBOX, cube_handler.set_index)

        # generate radiobuttons for direction
        directions = ['Clockwise', 'Counterclockwise']
        radio_buttons = gui_items.gen_radiobox(150, 50, (180, -1), wx.RA_SPECIFY_ROWS, directions)
        # bind radiobuttons
        gui_items.bind_element(radio_buttons, wx.EVT_RADIOBOX, cube_handler.set_direction)