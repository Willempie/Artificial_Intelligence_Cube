from visual import *
import gui_items
from logic.handling.step_handling import StepHandling
from object_visual.v_rubiks_cube import VRubiksCube
from cubegui import *
from cube_display import *
from cube_handler import *
from gui_items import *
from keyboard_handler import *
from mouse_handler import *
from helper import *
from objects.xml.xml_step import Step


class VDisplay():

    __default_button_width = 88
    __default_button_height = 26
    cube = None

    __edit_panel = None
    __action_panel = None

    __cube_action_textbox = None

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

    def create_input_display(self):

        # create GUI
        cube_gui = CubeGui("Artificial Intelligence Cube")

        # create cube display
        cube_display = CubeDisplay(cube_gui.get_window())

        # GUI items
        gui_items = GuiItems(cube_gui, cube_gui.get_window_panel())

        # color combobox
        action_combo_box = gui_items.gen_combobox((20, 10), (150, -1), Helper.CUBE_COLOR_NAME)
        action_combo_box.SetSelection(0)

        # generate menu
        gui_items.gen_menu(cube_gui.get_window())

        # generate cube
        self.cube = VRubiksCube(3, None, None, None, False)
        self.cube.set_front(color.red)

        # step handler
        step_handling = StepHandling(self)

        # buttons
        start_cube_button = gui_items.gen_button("Start Cube *", 20, 50)
        # gui_items.bind_element(start_cube_button, wx.EVT_BUTTON, step_handling.start_cube)
        result_cube_button = gui_items.gen_button("Result Cube *", 20, 80)
        # gui_items.bind_element(result_cube_button, wx.EVT_BUTTON, step_handling.result_cube)
        code_button = gui_items.gen_button("Code *", 20, 110)
        # gui_items.bind_element(code_button, wx.EVT_BUTTON, step_handling.cube)

        '''
            EDIT PANEL
        '''
        # new EDIT panel (color, turnable, reset)
        self.__edit_panel = gui_items.add_panel(450, 390, (200, 300))
        cube_edit_gui_items = GuiItems(cube_gui, self.__edit_panel)
        box_sizer = cube_edit_gui_items.gen_box_sizer(wx.VERTICAL)

        # color dropdown menu
        cube_color_combo_box = cube_edit_gui_items.gen_combobox((10, 10), (150, -1), Helper.CUBE_COLOR_NAME)
        cube_color_combo_box.SetSelection(0)

        # turnable checkbox
        cube_turnable_checkbox = cube_edit_gui_items.gen_radiobox(20, 20, (100, 100), wx.RA_SPECIFY_ROWS,
                                                                  ['Turnable', 'Not Turnable'])
        # reset button
        cube_reset_button = cube_edit_gui_items.gen_button("Reset", 30, 30)

        #add all elements
        box_sizer.Add(cube_color_combo_box, 0, wx.ALL)
        box_sizer.Add(cube_turnable_checkbox, 0, wx.ALL)
        box_sizer.Add(cube_reset_button, 0, wx.ALL)

        # set sizer to panel
        self.__edit_panel.SetSizer(box_sizer)
        self.__edit_panel.Layout()

        # hide panel
        self.__edit_panel.Hide()

        # bind button for showing / hiding the edit panel
        start_cube_button.Bind(wx.EVT_BUTTON, lambda event: self.change_display_edit_panel())


        '''
            ACTION PANEL
        '''
        # new ACTION panel (textbox met draaien, knop voor het uitvoeren van de draaien)
        self.__action_panel = gui_items.add_panel(450, 390, (300, 300))
        cube_action_gui_items = GuiItems(cube_gui, self.__action_panel)
        main_sizer = cube_action_gui_items.gen_box_sizer(wx.HORIZONTAL)
        axes_sizer = cube_action_gui_items.gen_box_sizer(wx.VERTICAL)
        output_sizer = cube_action_gui_items.gen_box_sizer(wx.VERTICAL)

        # uitvoer draaien knop
        cube_action_button = cube_action_gui_items.gen_button("Run actions.", 20, 20)
        cube_action_button.btn_id = 'run'
        # bind
        cube_action_gui_items.bind_element(cube_action_button, wx.EVT_BUTTON, self.execute_code)  # X

        # reset textbox button
        cube_reset_textbox_button = cube_action_gui_items.gen_button("Reset actions.", 30, 30)
        cube_action_gui_items.bind_element(cube_reset_textbox_button, wx.EVT_BUTTON, self.reset_textbox)  # X

        # textbox met draaien
        self.__cube_action_textbox = cube_action_gui_items.gen_textbox(10, 10, (200, -1), (wx.TE_READONLY | wx.TE_MULTILINE))

        # dropdown for selecting cube row
        combo_box_items = []
        for size in range(self.cube.get_size()):
            combo_box_items.append(str(size+1))
        action_combo_box = cube_action_gui_items.gen_combobox((150, 10), (150, -1), combo_box_items)
        action_combo_box.SetSelection(0)

        # turnable checkbox(clockwise, counterclockwise)
        cube_turnable_checkbox = cube_action_gui_items.gen_radiobox(20, 20, (100, 100), wx.RA_SPECIFY_ROWS,
                                                                    ['CounterClockwise', 'Clockwise'])

        # buttons voor het draaien (MET BIND)
        x_button = cube_action_gui_items.gen_button("Voer X in", 0, 0)
        x_button.btn_id = 'x'
        y_button = cube_action_gui_items.gen_button("Voer Y in", 0, 0)
        y_button.btn_id = 'y'
        z_button = cube_action_gui_items.gen_button("Voer Z in", 0, 0)
        z_button.btn_id = 'z'
        x_button.Bind(wx.EVT_BUTTON, lambda event: self.insert_into_textbox('x', action_combo_box.GetValue(),
                                                                            cube_turnable_checkbox.GetSelection()))
        y_button.Bind(wx.EVT_BUTTON, lambda event: self.insert_into_textbox('y', action_combo_box.GetValue(),
                                                                            cube_turnable_checkbox.GetSelection()))
        z_button.Bind(wx.EVT_BUTTON, lambda event: self.insert_into_textbox('z', action_combo_box.GetValue(),
                                                                            cube_turnable_checkbox.GetSelection()))
        #cube_action_gui_items.bind_element(x_button, wx.EVT_BUTTON, self.insert_into_textbox)  # X
        #cube_action_gui_items.bind_element(y_button, wx.EVT_BUTTON, self.insert_into_textbox)  # Y
        #cube_action_gui_items.bind_element(z_button, wx.EVT_BUTTON, self.insert_into_textbox)  # Z

        # add elements to box_sizers
        output_sizer.Add(self.__cube_action_textbox, 0, wx.ALL, 5)
        output_sizer.Add(cube_action_button, 0, wx.ALL, 5)
        output_sizer.Add(cube_reset_textbox_button, 0, wx.ALL, 5)
        axes_sizer.Add(x_button, 0, wx.ALL, 1)
        axes_sizer.Add(y_button, 0, wx.ALL, 1)
        axes_sizer.Add(z_button, 0, wx.ALL, 1)
        axes_sizer.Add(action_combo_box, 0, wx.ALL, 1)
        axes_sizer.Add(cube_turnable_checkbox, 0, wx.ALL, 1)

        main_sizer.Add(output_sizer)
        main_sizer.Add(axes_sizer)

        # set sizer to panel
        self.__action_panel.SetSizer(main_sizer)
        self.__action_panel.Layout()

        # hide panel
        self.__action_panel.Hide()

        # bind button for showing/hiding action panel
        code_button.Bind(wx.EVT_BUTTON, lambda event: self.change_display_action_panel())


        '''
            END PANELS
        '''

        # mouse handler
        mouse_handler = MouseHandler(cube_display.get_display())
        mouse_handler.bind_mouse_click(self.cube, action_combo_box)

    def change_display_edit_panel(self):
       if self.__edit_panel.IsShown():
           self.__edit_panel.Hide()
       else:
           self.__edit_panel.Show()

    def change_display_action_panel(self):
       if self.__action_panel.IsShown():
           self.__action_panel.Hide()
       else:
           self.__action_panel.Show()

    def insert_into_textbox(self, axis, row, direction):
        if direction == 0:
            direction = -1

        self.__steps.append(Step(axis, row, direction))
        self.__cube_action_textbox.AppendText(";" + str(axis) + "," + str(row) + "," + str(direction))

    def reset_textbox(self, event):
        self.__steps = []
        self.__cube_action_textbox.Clear()

    def execute_code(self, event):
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