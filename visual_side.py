from visual import *
from side import Side


class VisualSide(Side):

    _array_edge = None
    _array_block = None

    def __init__(self, size, color, center):
        Side.__init__(self,size,color)

        self._array_block = [[None for i in xrange(size)] for j in xrange(size)]
        for x in xrange(self._size):
            for y in xrange(self._size):
                print(str(x)+"-"+str(y))

                local_box = box()
                local_box.size = vector(3, 3, 0.5)


                l_x = x * 5 + center.x
                l_y = y * 5 + center.y

                local_box.pos = vector(l_x,l_y,center.z)

                self._array_block[y][x] = local_box

    @staticmethod
    def __base(center):
        return 5