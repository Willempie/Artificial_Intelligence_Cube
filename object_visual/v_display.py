from visual import *
from object_visual.v_cube import VCube
from cubegui import *

class VDisplay(display):

    def __init__(self):
        display.__init__(self)

        # set gui for cube
        cube_gui = CubeGui('Artificial Intelligence Cube')
        cube_gui.display_gui()
        cube_gui.add_gui_items()

        self.lights = []
        self.ambient = color.gray(1)
        self.background = color.gray(0.2)

        self.current_key = None
        self.action = False

        self.cube = VCube(3)

        # keyboard event handler
        keyboard_handler = KeyboardHandler(cube_gui.get_window_frame(), self.cube, cube_gui.get_window_frame())
        keyboard_handler.bind_key(wx.EVT_KEY_DOWN, keyboard_handler.on_key_down)
        keyboard_handler.bind_key(wx.EVT_KILL_FOCUS, keyboard_handler.test_function)

        print(wx.Window.FindFocus())




    '''def keyInput(self, evt):
        s = evt.key
        if evt.ctrl:
            direction = -1
        else:
            direction = 1

        if self.current_key is None and self.action is False:
            self.current_key = s
            rate(self.cube.fps)
            if s == 'x':
                self.cube.turn_x(random.randint(0, 3), direction)
            if s == 'y':
                self.cube.turn_y(random.randint(0, 3), direction)
            if s == 'z':
                self.cube.turn_z(random.randint(0, 3), direction)
            rate(self.cube.fps)
        else:
            return
    '''

    def keyRelease(self, evt):
        self.current_key = None



