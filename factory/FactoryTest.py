from factory.GraphicalFactory import GraphicalFactory
from factory.ShapeFactory import ShapeFactory
from factory.Shape import Shape


f = ShapeFactory()
v = Shape()


f = GraphicalFactory()
v = f.generateRubiksCube(3)

#v.draw()