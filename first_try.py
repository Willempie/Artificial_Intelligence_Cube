from object_visual.v_display import VDisplay
#x = VDisplay()


from objects.cube.rubiks_cube import RubiksCube
from objects.cube.cube import Cube

z = RubiksCube()


print(z.contains(8))

z.my_print()