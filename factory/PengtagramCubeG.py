from factory.Shape import Shape

class PentagramCubeG(Shape):

    def __init__(self, object):
        self.object = object

    def draw(self):
        self.object.set_cube_visible(True)

