from visual import *
from objects.cube_block import CubeBlock
from b_cube import BCube


class VCubeBlock(CubeBlock, BCube):

    _thickness = 0.1
    _padding = 0.25

    def __init__(self, base_pos=None, base_color=None, base_dimension=None):
        CubeBlock.__init__(self)
        BCube.__init__(self, base_pos, base_dimension)

        if base_color is None:
            self.color = color.white
        else:
            self.color = base_color

        self._center_box = box(frame=self.v_frame, size=self.get_vector_size(), pos=self._pos, color=self.color)

    def get_vector_size(self):
        return vector(self._dimension, self._dimension, self._dimension)

    def set_color(self, box_color):
        self._center_box.color = box_color

    def set_front(self, box_color):
        my_pos = self._pos + vector(0, 0, self._dimension / 2)
        my_dimension = vector(self._dimension, self._dimension, self._thickness) - vector(self._padding, self._padding, 0)
        self._front = box(frame=self.v_frame, size=my_dimension, pos=my_pos, color=box_color)

    def set_back(self, box_color):
        my_pos = self._pos - vector(0, 0, self._dimension / 2)
        my_dimension = vector(self._dimension, self._dimension, self._thickness) - vector(self._padding, self._padding, 0)
        self._back = box(frame=self.v_frame, size=my_dimension, pos=my_pos, color=box_color)

    def set_top(self, box_color):
        my_pos = self._pos + vector(0,  self._dimension / 2, 0)
        my_dimension = vector(self._dimension, self._thickness, self._dimension) - vector(self._padding, 0, self._padding)
        self._top = box(frame=self.v_frame, size=my_dimension, pos=my_pos, color=box_color)

    def set_bottom(self, box_color):
        my_pos = self._pos - vector(0,  self._dimension / 2, 0)
        my_dimension = vector(self._dimension, self._thickness, self._dimension) - vector(self._padding, 0, self._padding)
        self._bottom = box(frame=self.v_frame, size=my_dimension, pos=my_pos, color=box_color)

    def set_left(self, box_color):
        my_pos = self._pos - vector(self._dimension / 2, 0, 0)
        my_dimension = vector(self._thickness, self._dimension, self._dimension) - vector(0, self._padding, self._padding)
        self._left = box(frame=self.v_frame, size=my_dimension, pos=my_pos, color=box_color)

    def set_right(self, box_color):
        my_pos = self._pos + vector(self._dimension / 2, 0, 0)
        my_dimension = vector(self._thickness, self._dimension, self._dimension) - vector(0, self._padding, self._padding)
        self._right = box(frame=self.v_frame, size=my_dimension, pos=my_pos, color=box_color)

    def rotate(self, box_angle, box_axis, box_origin):
        self.v_frame.rotate(angle=box_angle, axis=box_axis, origin=box_origin)
