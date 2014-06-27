from visual import *
import gui_items
from logic.handling.files import HandleFiles
from logic.handling.panel_handling import PanelHandling
from object_visual.v_rubiks_cube import VRubiksCube
from cubegui import *
from cube_display import *
from cube_handler import *
from gui_items import *
from keyboard_handler import *
from logic.handling.cube_storage import CubeStorage

class Controller():

    __default_button_width = 88
    __default_button_height = 26

    def __init__(self):
        self.create_input_display()
        self._panels = PanelHandling(self)

    def create_input_display(self):

        # create GUI
        self.cube_gui = CubeGui("Artificial Intelligence Cube")

        # create cube display
        self.cube_display = CubeDisplay(self.cube_gui.get_window(), True)

        # GUI items
        self.gui_items = GuiItems(self, self.cube_gui, self.cube_gui.get_window_panel())

        #Cube Storage
        self._storage = CubeStorage(self, 3)

        # Xml Handler
        self.handle_xml = HandleFiles(self)

        # generate menu
        self.gui_items.gen_menu(self.cube_gui.get_window())

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

    def actionButtonResultCube(self):
        self._panels.switch_to_create()
        self._storage.switch_to_result()

    def actionButtonCodeCube(self):
        self._panels.switch_to_action()
        self._storage.switch_to_code()