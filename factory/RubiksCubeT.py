from factory.Shape import Shape

class RubiksCubeT(Shape):

    def __init__(self, object):
        self.object = object

    def draw(self):
        self.object.toString()
