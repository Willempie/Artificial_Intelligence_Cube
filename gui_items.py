import wx


class GuiItems:

    __GUI = None
    __GUI_panel = None

    def __init__(self, gui, gui_panel):
        self.__GUI = gui
        self.__GUI_panel = gui_panel

    def gen_text(self):
        return

    def gen_button(self, text, position_x, position_y):
        return wx.Button(self.__GUI_panel, label=text, pos=(position_x, position_y))

    def gen_radiobox(self, position_x, position_y, radio_size, style, options):
        return wx.RadioBox(self.__GUI_panel, pos=(position_x, position_y), size=radio_size, choices=options, style=style)

    def gen_slider(self, panel, position, slider_size, min_value, max_value):
        return wx.Slider(panel, pos=position, size=slider_size, minValue=min_value, maxValue=max_value)

    def gen_combobox(self, position, size, choice_array):
        return wx.ComboBox(self.__GUI_panel, pos=position, size=size, choices=choice_array, style=wx.CB_READONLY)

    def gen_textbox(self):
        return

    def bind_element(self, element, event, method):
        element.Bind(event, method)

    def add_gui_item(self):
        return