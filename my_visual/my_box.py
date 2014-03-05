from visual import *


class MyBox:

    __color = None
    __size = 2
    __thickness = 0.1
    __padding = 0.25
    my_frame = None

    center_box = None
    front_box = None
    back_box = None
    top_box = None
    bottom_box = None
    left_box = None
    right_box = None


    def __init__(self, base_pos=None, base_color=None, base_size=None):
        if base_pos is None:  # set default position
            self.pos = vector(0, 0, 0)
        else:
            self.pos = base_pos

        if base_color is None:  # set default color
            self.__color = color.white
        else:
            self.__color = base_color

        if base_size is None or base_size < 2:  # set default size
            self.__size = 2
        else:
            self.__size = base_size

        self.my_frame = frame(pos=self.pos)
        self.center_box = box(frame=self.my_frame,size=self.get_vector_size(), pos=self.pos, color=self.__color)

    def get_vector_size(self):
        return vector(self.__size, self.__size, self.__size)

    def set_front(self, box_color):
        my_pos = self.pos + vector(0, 0, self.__size / 2)
        my_size = vector(self.__size, self.__size, self.__thickness) - vector(self.__padding, self.__padding, 0)
        self.front_box = box(frame=self.my_frame,size=my_size, pos=my_pos, color=box_color)

    def set_back(self, box_color):
        my_pos = self.pos - vector(0, 0, self.__size / 2)
        my_size = vector(self.__size, self.__size, self.__thickness) - vector(self.__padding, self.__padding, 0)
        self.back_box = box(frame=self.my_frame,size=my_size, pos=my_pos, color=box_color)

    def set_top(self, box_color):
        my_pos = self.pos + vector(0,  self.__size / 2, 0)
        my_size = vector(self.__size, self.__thickness, self.__size) - vector(self.__padding, 0, self.__padding)
        self.top_box = box(frame=self.my_frame,size=my_size, pos=my_pos, color=box_color)

    def set_bottom(self, box_color):
        my_pos = self.pos - vector(0,  self.__size / 2, 0)
        my_size = vector(self.__size, self.__thickness, self.__size) - vector(self.__padding, 0, self.__padding)
        self.bottom_box = box(frame=self.my_frame,size=my_size, pos=my_pos, color=box_color)

    def set_left(self, box_color):
        my_pos = self.pos - vector(self.__size / 2, 0, 0)
        my_size = vector(self.__thickness, self.__size, self.__size) - vector(0, self.__padding, self.__padding)
        self.left_box = box(frame=self.my_frame,size=my_size, pos=my_pos, color=box_color)

    def set_right(self, box_color):
        my_pos = self.pos + vector(self.__size / 2, 0, 0)
        my_size = vector(self.__thickness, self.__size, self.__size) - vector(0, self.__padding, self.__padding)
        self.right_box = box(frame=self.my_frame,size=my_size, pos=my_pos, color=box_color)

    def rotate(self, box_angle, box_axis, box_origin):
        self.my_frame.rotate(angle=box_angle, axis=box_axis, origin=box_origin)

