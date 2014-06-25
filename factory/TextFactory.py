from factory.ShapeFactory import ShapeFactory
from factory.RubiksCubeT import RubiksCubeT
from object_visual.v_rubiks_cube import VRubiksCube


class TextFactory(ShapeFactory):

    def generateRubiksCube(self, size):
        cube = VRubiksCube(size, None, None, None, True)
        cube.set_cube_visible(False)
        cubeT = RubiksCubeT(cube)
        return cubeT

    def generatePentagramCube(self):
        raise NotImplementedError("Should be implemented")