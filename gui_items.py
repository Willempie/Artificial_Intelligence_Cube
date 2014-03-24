import wx

class GuiItems:

    __gui_itemlist = None


    def __init__(self):
        self.__gui_itemlist = []
        return

    def gen_text(self):
        return

    def gen_button(self, panel, text, position_x, position_y):
        button = wx.Button(panel, label=text, pos=(position_x, position_y))

    def gen_radiobox(self, panel, position_x, position_y, radio_size, style, options):
        radiobox = wx.RadioBox(panel, pos=(position_x, position_y), size=radio_size, choices=options, style=style)

    def gen_slider(self, panel, position, slider_size, min_value, max_value):
        slider = wx.Slider(panel, pos=position, size=slider_size, minValue=min_value, maxValue=max_value)
        slider.Bind(self, event, handler, source , id, id2)
        return wx.Slider(panel, pos=position, size=slider_size, minValue=min_value, maxValue=max_value)

    def gen_textbox(self):
        return

    def bind_element(self, element, method):
        return