from visual import *
from cube import Cube
from visual_side import VisualSide

class VisualCube(Cube):

    x = None
    top = None

    def __init__(self):
        Cube.__init__(self,4)

        self.x=VisualSide(5,color.red,vector(0,0,0))

        top = box()
        top.size = vector(8, 1, 8)
        top.pos = vector(0, 4.5, 0)
        top.color = color.green