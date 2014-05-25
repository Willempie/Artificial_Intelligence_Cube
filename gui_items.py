import wx
from logic.handling.files import HandleFiles


class GuiItems:

    __GUI = None
    __GUI_panel = None

    def __init__(self, gui, gui_panel):
        self.__GUI = gui
        self.__GUI_panel = gui_panel

    def gen_menu(self, window):

        handle_files = HandleFiles(window.win)

        m = window.menubar  # Refers to the menubar, which can have several menus

        # remove default file menu
        m.Remove(0)

        menu = wx.Menu()
        menu_item_new = menu.Append(-1, 'New', 'New XML file for Cube')

        menu_item_open = menu.Append(-1, 'Open', 'Open XML file for Cube')
        window.win.Bind(wx.EVT_MENU, getattr(handle_files, "open"), menu_item_open  )

        menu_item_save = menu.Append(-1, 'Save', 'Save XML file for Cube')
        window.win.Bind(wx.EVT_MENU, getattr(handle_files, "save"), menu_item_save)

        menu_item_close = menu.Append(-1, 'Close', 'Close XML file for Cube')

        m.Insert(0, menu, "Bestand")

    def add_panel(self, position_x, position_y, panel_size):
        return wx.Panel(parent=self.__GUI_panel, pos=(position_x, position_y), size=panel_size)

    def gen_box_sizer(self, orient):
        return wx.BoxSizer(orient)

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

    def gen_textbox(self, position_x, position_y, textbox_size, style):
        return wx.TextCtrl(self.__GUI_panel, pos=(position_x, position_y), size=textbox_size, style=style)

    def bind_element(self, element, event, method):
        element.Bind(event, method)

    def add_gui_item(self):
        return