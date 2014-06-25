from gui_items import *
from helper import Helper
from mouse_handler import MouseHandler


class CreatePanel:

    def __init__(self, display):
        self.display = display

        # new EDIT panel (color, turnable, reset)
        self.panel = self.display.gui_items.add_panel(450, 390, (200, 300))
        cube_edit_gui_items = GuiItems(display, self.display.cube_gui, self.panel)
        box_sizer = cube_edit_gui_items.gen_box_sizer(wx.VERTICAL)

        # color dropdown menu
        cube_color_combo_box = cube_edit_gui_items.gen_combobox((10, 10), (150, -1), Helper.CUBE_COLOR_NAME)
        cube_color_combo_box.SetSelection(0)

        # turnable checkbox
        cube_turnable_checkbox = cube_edit_gui_items.gen_radiobox(20, 20, (100, 100), wx.RA_SPECIFY_ROWS,
                                                                  ['Turnable', 'Not Turnable'])
        # reset button
        cube_reset_button = cube_edit_gui_items.gen_button("Reset", 30, 30)
        cube_reset_button.Bind(wx.EVT_BUTTON, lambda event: self._action_reset_button())

        #add all elements
        box_sizer.Add(cube_color_combo_box, 0, wx.ALL)
        box_sizer.Add(cube_turnable_checkbox, 0, wx.ALL)
        box_sizer.Add(cube_reset_button, 0, wx.ALL)

        # set sizer to panel
        self.panel.SetSizer(box_sizer)
        self.panel.Layout()

        # hide panel
        self.panel.Hide()

        # mouse handler
        mouse_handler = MouseHandler(self.display)
        mouse_handler.bind_mouse_click(cube_color_combo_box)


    def _action_reset_button(self):
        #myXml = XmlParser()
        #
        #myObject = myXml.read_file("2.1.xml", True)
        ##myObject2 = myXml.read_file("tha_cube.xml", True)
        #
        #myCompare = PatternFinder(3)
        #
        #myCompare.set_base_cube(self.display._storage._base_cube)
        #myCompare.set_matching_cube(myObject._start_cube)
        #
        #print myCompare._match()
        ##myCompare.create_next_set()
        #
        ##print myCompare._match()

        print "hello I'm a reset button :D"
