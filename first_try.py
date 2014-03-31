from object_visual.v_display import VDisplay
x = VDisplay()


from objects.cube.rubiks_cube import RubiksCube

z = RubiksCube(2)

print(z.solved())
z.turn_x(0,1)
print(z.solved())
z.turn_x(0,-1)
print(z.solved())