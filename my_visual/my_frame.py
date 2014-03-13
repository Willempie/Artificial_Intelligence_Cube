from visual import *


class MyFrame:

    object_frame = None

    def __init__(self, position):
        self.object_frame = frame(pos=position)

    def set_position(self, position):
        self.object_frame.pos = position

    def set_rotation(self, f_angle, f_axis, f_origin):
        self.object_frame.rotate(angle=f_angle, axis=f_axis, origin=f_origin)
