from visual import *


class BCube:

    def __init__(self, position, dimension):

        if position is None:
            self._pos = vector(0, 0, 0)
        else:
            self._pos = position

        if dimension is None or dimension < 2:
            self._dimension = 2
        else:
            self._dimension = dimension

        self.v_frame = frame(pos=self._pos)
