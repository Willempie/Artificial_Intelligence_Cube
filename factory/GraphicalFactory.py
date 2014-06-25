from factory.RubiksCubeG import RubiksCubeG
from factory.ShapeFactory import ShapeFactory
from object_visual.v_rubiks_cube import VRubiksCube


class GraphicalFactory(ShapeFactory):

    def generateRubiksCube(self, size):
        cube = VRubiksCube(size, None, None, None, True)
        cube.set_cube_visible(False)
        cubeG = RubiksCubeG(cube)
        return cubeG

    def generatePentagramCube(self, size):
        raise NotImplementedError("Should be implemented")