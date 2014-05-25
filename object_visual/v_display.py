from visual import *
import gui_items
from logic.handling.panel_handling import PanelHandling
from object_visual.v_rubiks_cube import VRubiksCube
from cubegui import *
from cube_display import *
from cube_handler import *
from gui_items import *
from keyboard_handler import *
from mouse_handler import *
from helper import *
from objects.xml.xml_step import Step
from logic.handling.cube_storage import CubeStorage

class VDisplay():

    __default_button_width = 88
    __default_button_height = 26
    cube = None

    __steps = []

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

        self.create_input_display()

        self._storage = CubeStorage(3)

        self._panels = PanelHandling(self)


    def create_input_display(self):

        # create GUI
        self.cube_gui = CubeGui("Artificial Intelligence Cube")

        # create cube display
        self.cube_display = CubeDisplay(self.cube_gui.get_window())

        # GUI items
        self.gui_items = GuiItems(self.cube_gui, self.cube_gui.get_window_panel())

        # color combobox
        action_combo_box = self.gui_items.gen_combobox((20, 10), (150, -1), Helper.CUBE_COLOR_NAME)
        action_combo_box.SetSelection(0)

        # generate menu
        self.gui_items.gen_menu(self.cube_gui.get_window())

        # handle xml files
        handle_xml = HandleFiles(self.cube_gui.get_window())

        # generate cube
        self.cube = VRubiksCube(3, None, None, None, False)
        self.cube.set_front(color.red)
        self.cube.set_cube_visible(False)

        # buttons
        self.start_cube_button = self.gui_items.gen_button("Start Cube *", 20, 50)
        self.start_cube_button.Bind(wx.EVT_BUTTON, lambda event: self.actionButtonStartCube())

        self.result_cube_button = self.gui_items.gen_button("Result Cube *", 20, 80)
        self.result_cube_button.Bind(wx.EVT_BUTTON, lambda event: self.actionButtonResultCube())

        self.code_button = self.gui_items.gen_button("Code *", 20, 110)
        self.code_button.Bind(wx.EVT_BUTTON, lambda event: self.actionButtonCodeCube())


    def actionButtonStartCube(self):
        self._panels.switch_to_create()
        self._storage.switch_to_start()


        #if self.__edit_panel.IsShown():
        #    self.__edit_panel.Hide()
        #else:
        #    self.__edit_panel.Show()

    def actionButtonResultCube(self):
        self._storage.switch_to_result()

    def actionButtonCodeCube(self):
        self._panels.switch_to_action()
        self._storage.switch_to_code()

        #if self.__action_panel.IsShown():
        #    self.__action_panel.Hide()
        #else:
        #    self.__action_panel.Show()


    def insert_into_textbox(self, axis, row, direction):
        if direction == 0:
            direction = -1

        self.__steps.append(Step(axis, int(row)-1, direction))
        self.__cube_action_textbox.AppendText(";" + str(axis) + "," + str(row) + "," + str(direction))

    def reset_textbox(self, event):
        self.__steps = []
        self.__cube_action_textbox.Clear()

    def execute_code(self, event):
        self.cube.execute_steps(self.__steps)

        button_id = event.GetEventObject().btn_id

        if button_id == 'run':
            print self.__cube_action_textbox.GetValue()

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