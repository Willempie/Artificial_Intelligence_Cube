from gui_items import *
from objects.xml.xml_step import Step


class ActionPanel:

    def __init__(self, display):
        self.steps = []
        self.display = display

        # new ACTION panel (textbox met draaien, knop voor het uitvoeren van de draaien)
        self.panel = self.display.gui_items.add_panel(450, 390, (300, 300))
        cube_action_gui_items = GuiItems(display, self.display.cube_gui, self.panel)
        main_sizer = cube_action_gui_items.gen_box_sizer(wx.HORIZONTAL)
        axes_sizer = cube_action_gui_items.gen_box_sizer(wx.VERTICAL)
        output_sizer = cube_action_gui_items.gen_box_sizer(wx.VERTICAL)

        # uitvoer draaien knop
        cube_action_button = cube_action_gui_items.gen_button("Run actions.", 20, 20)
        cube_action_button.btn_id = 'run'
        cube_action_button.Bind(wx.EVT_BUTTON, lambda event: self._button_run())

        # reset textbox button
        cube_reset_textbox_button = cube_action_gui_items.gen_button("Reset actions.", 30, 30)
        cube_reset_textbox_button.Bind(wx.EVT_BUTTON, lambda event: self._button_reset())


        # textbox met draaien
        self.cube_action_textbox = cube_action_gui_items.gen_textbox(10, 10, (200, -1), (wx.TE_MULTILINE))

        # dropdown for selecting cube row
        combo_box_items = []
        for size in range(self.display._storage.cube_size):
            combo_box_items.append(str(size+1))
        self.action_combo_box = cube_action_gui_items.gen_combobox((150, 10), (150, -1), combo_box_items)
        self.action_combo_box.SetSelection(0)

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
        x_button.Bind(wx.EVT_BUTTON, lambda event: self._button_x_y_z('x', self.action_combo_box.GetValue(),
                                                                        cube_turnable_checkbox.GetSelection()))
        y_button.Bind(wx.EVT_BUTTON, lambda event: self._button_x_y_z('y', self.action_combo_box.GetValue(),
                                                                        cube_turnable_checkbox.GetSelection()))
        z_button.Bind(wx.EVT_BUTTON, lambda event: self._button_x_y_z('z', self.action_combo_box.GetValue(),
                                                                        cube_turnable_checkbox.GetSelection()))

        # undo button
        undo_button = cube_action_gui_items.gen_button("Undo last input", 0,0)
        undo_button.Bind(wx.EVT_BUTTON, self.__undo)

        # add elements to box_sizers
        output_sizer.Add(self.cube_action_textbox, 0, wx.ALL, 5)
        output_sizer.Add(cube_action_button, 0, wx.ALL, 5)
        output_sizer.Add(cube_reset_textbox_button, 0, wx.ALL, 5)
        output_sizer.Add(undo_button, 0, wx.ALL, 5)
        axes_sizer.Add(x_button, 0, wx.ALL, 1)
        axes_sizer.Add(y_button, 0, wx.ALL, 1)
        axes_sizer.Add(z_button, 0, wx.ALL, 1)
        axes_sizer.Add(self.action_combo_box, 0, wx.ALL, 1)
        axes_sizer.Add(cube_turnable_checkbox, 0, wx.ALL, 1)

        main_sizer.Add(output_sizer)
        main_sizer.Add(axes_sizer)

        # set sizer to panel
        self.panel.SetSizer(main_sizer)
        self.panel.Layout()

        # hide panel
        self.panel.Hide()

    def __undo(self, event):
        counter = 1
        textbox_items = ""
        splitted_inserted_text = self.cube_action_textbox.GetValue().split(';')
        for current_split in splitted_inserted_text:
            if counter < len(splitted_inserted_text):
                textbox_items += ";" + current_split
                counter += 1

        # change textbox value
        self.cube_action_textbox.Clear()
        self.cube_action_textbox.AppendText(textbox_items[1:]) # minus first ; char


    def _button_run(self):
        self.read_steps()

        self.display._storage.current_cube.execute_steps(self.steps)

    def read_steps(self):
        self.steps = []

        text = str(self.cube_action_textbox.GetValue())
        if not text == "":
            for current_split in text.split(';'):
                var_split = current_split.split(',')
                self.steps.append(Step(var_split[0], int(var_split[1])-1, int(var_split[2])))
                print var_split


    def _button_reset(self):
        self.steps = []
        self.cube_action_textbox.Clear()

    def _reset_textbox(self):
        self.cube_action_textbox.Clear()
        for step in self.steps:
            self.cube_action_textbox.AppendText(";" + str(step.axis) + "," + str(step.rows) + "," + str(step.direction))

    def _button_x_y_z(self, axis, row, direction):
        if direction == 0:
            direction = -1

        if len(self.cube_action_textbox.GetValue()) == 0:
            self.cube_action_textbox.AppendText(str(axis) + "," + str(row) + "," + str(direction))
        else:
            self.cube_action_textbox.AppendText(";" + str(axis) + "," + str(row) + "," + str(direction))