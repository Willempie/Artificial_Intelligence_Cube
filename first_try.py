from object_visual.v_display import VDisplay
from objects.cube.rubiks_cube import RubiksCube

#x = VDisplay()
#x.create_input_display()

from object_visual.v_rubiks_cube import VRubiksCube
from objects.cube.cube import *
from objects.cube.rubiks_cube import RubiksCube
from logic.rubiks_cube_converter import RubiksCubeConverter
from helper import Helper
from visual import *

cube = RubiksCube();

cube.turn_x(0,1)

cube.my_print()

new_cube = RubiksCubeConverter.to_code_cube(cube)
new_cube.my_print()

new_cube2 = RubiksCubeConverter.to_visual_cube(cube)
new_cube2.my_print()