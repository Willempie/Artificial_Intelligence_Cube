class FocusHandler():

    __main_window = None
    __second_focus = None

    def __init__(self, main_focus):
        self.__main_window = main_focus

    def focus_kill_function(self, event):
        self.__main_window.SetFocus()

    def focus_set_function(self, event):
        self.__main_window.SetFocus()
