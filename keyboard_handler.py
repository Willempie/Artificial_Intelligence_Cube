from numpy import random
from visual_common.create_display import rate
import wx


class KeyboardHandler():

    __frame = None
    __cube = None
    __win = None

    __x_key_code = 88
    __y_key_code = 89
    __z_key_code = 90

    __direction = 1

    def __init__(self, frame, cube, win):
        self.__frame = frame
        self.__cube = cube
        self.__win = win

    def bind_key(self, key, action):
        if self.__frame is not None:
            self.__frame.Bind(key, action)

    def set_direction(self, evt):
        if evt.ControlDown():
            self.__direction = -1
        else:
            self.__direction = 1

    def on_key_down(self, evt):
        key_code = evt.GetKeyCode()

        self.set_direction(evt)  # set direction

        if isinstance(key_code, int):
            rate(self.__cube.fps)
            if key_code == self.__x_key_code:
                self.__cube.turn_x(random.randint(0, 3), self.__direction)
                #print("x")
            elif key_code == self.__y_key_code:
                self.__cube.turn_y(random.randint(0, 3), self.__direction)
                #print("y")
            elif key_code == self.__z_key_code:
                self.__cube.turn_z(random.randint(0, 3), self.__direction)
                #print("z")
            rate(self.__cube.fps)


    def test_function(self, evt):
        print(wx.Window.FindFocus())
        wx.Window.SetFocus(self.__win)


        print("Test")
