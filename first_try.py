from object_visual.v_display import VDisplay
#x = VDisplay()

from visual import *
from objects.cube.rubiks_cube import RubiksCube
from object_visual.v_rubiks_cube import VRubiksCube
from objects.cube.cube import Cube

z = VRubiksCube()


top00 = z.get_top()

print(z.contains(z._center_box))

z.my_print()