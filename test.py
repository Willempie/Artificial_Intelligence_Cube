from visual import *


class MyBox:
    my_frame =None

    def __init__(self):
        self.my_frame = frame()
        a = box(frame=self.my_frame)

    def add_box(self):
        b = box(pos=vector(2,0,0),frame=self.my_frame)

d = MyBox()
d.add_box()
for l in xrange(5):
    d.my_frame.rotate(angle=pi / 2 / 12, axis=vector(1, 0, 0), origin=vector(0,0,0))



'''
def get_start_vector(center, size, block_size):
    x = center.x - ( size * block_size / 2)
    y = center.y - ( size * block_size / 2)
    z = center.z - ( size * block_size / 2)
    return vector(x,y,z)

def get_block_pos(start_pos, block_size, x, y, z):
    x = start_pos.x + block_size / 2 + block_size * x
    y = start_pos.y + block_size / 2 + block_size * y
    z = start_pos.z + block_size / 2 + block_size * z
    return vector(x,y,z)

size = 10
block_size = 2
center = vector(0, 0, 0)
start_vector = get_start_vector(center,size,block_size)

_array = [[[None for k in xrange(size)] for i in xrange(size)] for j in xrange(size)]




print(_array)

for x in xrange(size):
    for y in xrange(size):
        for z in xrange(size):
            my_box = box()
            my_box.size = vector(block_size, block_size, block_size)
            my_box.pos = get_block_pos(start_vector,block_size,x,y,z)
            _array[x][y][z] = my_box

fps = 24
angle = pi / 2

while True:
    key = scene.kb.getkey()
    for r in xrange(fps):
        rate(fps)
        if key == 'a':
                for x in xrange(size):
                    for y in xrange(size):

        if key == 'b':
            for x in xrange(size):
                for y in xrange(size):
                    _array[x][y][0].rotate(angle=angle/fps, axis=vector(0,0,1),origin=(0, 0, 0))



my_box = box()
my_box.size = vector(8,8,8)

my_side = box()
my_side.size = vector(7.5,1,7.5)
my_side.pos = vector(0,3.75,0)
my_side.color = color.red

fps = 24
angle = pi / 2

while True:
    key = scene.kb.getkey()
    if key == 'a':
        my_box.rotate(angle=angle/fps, axis=vector(1,0,0),origin=(0, 0, 0))
        my_side.rotate(angle=angle/fps, axis=vector(1,0,0),origin=(0, 0, 0))


fps = 24

# Map keypresses to corresponding face colors and normal vectors.
faces = {'r': (color.red, (1, 0, 0)),
         'o': (color.orange, (-1, 0, 0)),
         'y': (color.yellow, (0, 1, 0)),
         'b': (color.blue, (0, -1, 0)),
         'w': (color.white, (0, 0, 1)),
         'g': (color.green, (0, 0, -1))}

# Create colored stickers on each face, one cubie at a time.
stickers = []
for face_color, axis in faces.itervalues():
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):

            # Start with all stickers on the top face, then rotate them "down"
            # to the appropriate face.
            sticker = box(color=face_color, pos=(x, y, 1.5),
                          length=0.98, height=0.98, width=0.05)
            cos_angle = dot((0, 0, 1), axis)
            pivot = (cross((0, 0, 1), axis) if cos_angle == 0 else (1, 0, 0))
            sticker.rotate(angle=acos(cos_angle), axis=pivot, origin=(0, 0, 0))
            stickers.append(sticker)

# Get keyboard moves and rotate the corresponding face.
while True:
    key = scene.kb.getkey()
    if faces.has_key(key.lower()):
        face_color, axis = faces[key.lower()]
        angle = ((pi / 2) if key.isupper() else -pi / 2)
        for r in arange(0, angle, angle / fps):
            rate(fps)
            for sticker in stickers:
                if dot(sticker.pos, axis) > 0.5:
                    sticker.rotate(angle=angle / fps, axis=axis,
                                   origin=(0, 0, 0))

'''
