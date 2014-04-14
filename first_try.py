from object_visual.v_display import VDisplay
from objects.cube.rubiks_cube import RubiksCube

x = VDisplay()
x.create_input_display()


z = RubiksCube(2)

print(z.solved())
z.turn_x(0,1)
print(z.solved())
z.turn_x(0,-1)
print(z.solved())