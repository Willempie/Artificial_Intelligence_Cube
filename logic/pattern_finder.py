from helper import Helper
from logic.rubiks_cube_converter import RubiksCubeConverter
from objects.cube.rubiks_cube import RubiksCube
import copy
from logic.xml_parser import XmlParser


class PatternFinder:

    def __init__(self, cube_size):
        self.cube_size = cube_size
        self.base_cube = None
        self.base_turn_cube = None
        self.match_cube = None
        self.match_turn_cube = None

    def set_base_cube(self, cube):
        if cube.get_size() == self.cube_size:
            self.base_cube = RubiksCubeConverter.to_code_cube(cube)
        else:
            raise Exception("Cube size doesn't match")

    def set_base_turn_cube(self, turn_cube):
        if turn_cube is not None:
            self.base_turn_cube = turn_cube

    def set_matching_cube(self, cube):
        if cube.get_size() == self.cube_size:
            self.match_cube = RubiksCubeConverter.to_code_cube(cube)
        else:
            raise Exception("Cube size doesn't match")

    def set_match_turn_cube(self, turn_cube):
        if turn_cube is not None:
            self.base_match_cube = turn_cube

    def _generate_cubes(self, cube):
        storage_side = []

        for x in range(6):
            storage_side.append(copy.deepcopy(cube))

        storage_side[1].turn("x", -1, 1)

        storage_side[2].turn("x", -1, 1)
        storage_side[2].turn("x", -1, 1)

        storage_side[3].turn("x", -1, -1)

        storage_side[4].turn("z", -1, 1)

        storage_side[5].turn("z", -1, -1)

        storage_turned_side = []
        for x in range(6):
            for y in range(3):
                storage_turned_side.append(copy.deepcopy(storage_side[x]))

        storage_turned_side[0].turn("y",-1,1)
        storage_turned_side[1].turn("y",-1,1)
        storage_turned_side[1].turn("y",-1,1)
        storage_turned_side[2].turn("y",-1,-1)

        storage_turned_side[3].turn("z",-1,1)
        storage_turned_side[4].turn("z",-1,1)
        storage_turned_side[4].turn("z",-1,1)
        storage_turned_side[5].turn("z",-1,-1)

        storage_turned_side[6].turn("y",-1,1)
        storage_turned_side[7].turn("y",-1,1)
        storage_turned_side[7].turn("y",-1,1)
        storage_turned_side[8].turn("y",-1,-1)

        storage_turned_side[9].turn("z",-1,1)
        storage_turned_side[10].turn("z",-1,1)
        storage_turned_side[10].turn("z",-1,1)
        storage_turned_side[11].turn("z",-1,-1)

        storage_turned_side[12].turn("x",-1,1)
        storage_turned_side[13].turn("x",-1,1)
        storage_turned_side[13].turn("x",-1,1)
        storage_turned_side[14].turn("x",-1,-1)

        storage_turned_side[15].turn("x",-1,1)
        storage_turned_side[16].turn("x",-1,1)
        storage_turned_side[16].turn("x",-1,1)
        storage_turned_side[17].turn("x",-1,-1)

        #self.generated_cubes = (storage_side + storage_turned_side)
        print len(storage_side + storage_turned_side)
        return storage_side + storage_turned_side

    def find_shadow_pattern(self, cube_a, cubes_b):

        result = []
        for side in Helper.CUBE_SIDES:
            current_side = cube_a.get_side(side)
            match_side = cubes_b.get_side(side)

            new_current_side = []
            new_match_side = []

            current_color_set = []
            match_color_set = []

            for x in range(self.cube_size):
                new_current_side.append([])
                new_match_side.append([])
                for y in range(self.cube_size):
                    if current_side[x][y] is None or match_side[x][y] is None:
                        new_current_side[x].append(None)
                        new_match_side[x].append(None)
                    else:
                        if current_side[x][y] not in current_color_set:
                            current_color_set.append(current_side[x][y])
                        if match_side[x][y] not in match_color_set:
                            match_color_set.append(match_side[x][y])

                        new_current_side[x].append(current_color_set.index(current_side[x][y]))
                        new_match_side[x].append(match_color_set.index(match_side[x][y]))
            #print current_color_set
            #print match_color_set
            result.append(new_current_side == new_match_side)

        #print result
        return all(result)

    def find_pattern(self, cube_a, cube_b):
        for cube in self._generate_cubes(cube_b):
            if self.find_shadow_pattern(cube_a, cube):
                if self.match_pattern(cube_a, cube):
                    return True

        return False

    def filter_cube(self, input_cube, xml_cube):
        temp_cube = RubiksCube(self.cube_size, False)

        for side in Helper.CUBE_SIDES:
            current_side = input_cube.get_side(side)
            match_side = xml_cube.get_side(side)

            new_side = []
            for x in range(self.cube_size):
                new_side.append([])
                for y in range(self.cube_size):
                    if match_side[x][y] is None:
                        new_side[x].append(None)
                    else:
                        new_side[x].append(current_side[x][y])

            temp_cube.set_side(side, new_side)
        return temp_cube

    def match_pattern(self, cube_a, cube_b):
        cube = self.filter_cube(cube_a, cube_b)
        #RubiksCubeConverter.to_visual_cube(cube)
        #RubiksCubeConverter.to_visual_cube(cube_b)
        #RubiksCubeConverter.to_visual_cube(cube_a)

        for turned_cube in self._generate_cubes(cube):
            result = []

            current_color_set = []
            match_color_set = []

            for side in Helper.CUBE_SIDES:
                current_side = turned_cube.get_side(side)
                match_side = cube_b.get_side(side)

                new_current_side = []
                new_match_side = []

                for x in range(self.cube_size):
                    new_current_side.append([])
                    new_match_side.append([])
                    for y in range(self.cube_size):
                        if current_side[x][y] is None or match_side[x][y] is None:
                            new_current_side[x].append(None)
                            new_match_side[x].append(None)
                        else:
                            if current_side[x][y] not in current_color_set:
                                current_color_set.append(current_side[x][y])
                            if match_side[x][y] not in match_color_set:
                                match_color_set.append(match_side[x][y])

                            new_current_side[x].append(current_color_set.index(current_side[x][y]))
                            new_match_side[x].append(match_color_set.index(match_side[x][y]))

                #print new_current_side + new_match_side
                result.append(new_current_side == new_match_side)

            #print current_color_set + match_color_set
            if all(result):
                #RubiksCubeConverter.to_visual_cube(cube_b)
                return True
        return False

    def create_next_set(self):
        self.next_set_cubes = []
        for cube in self.generated_cubes:
            for color in range(6):
                self.next_set_cubes.append(self._next_set(cube, color))

    def _match(self):
        if self.base_cube is None or self.match_cube is None:
            raise ValueError("Input doesn't match")

        for cube in self._generate_cubes():
            if self.find_pattern(cube):
                return True

        return False

    def _next_set(self, current_cube, set_num):
        local_cube = copy.deepcopy(current_cube)

        for side in Helper.CUBE_SIDES:
            current_side = local_cube.get_side(side)

            for x in range(self.cube_size):
                for y in range(self.cube_size):
                    if current_side[x][y] is not None:
                        current_side[x][y] = (current_side[x][y] + set_num) % 6

            local_cube.set_side(side, current_side)

        return local_cube

myXml = XmlParser()

myObject = myXml.read_file("2.1.xml", True)
myObject2 = myXml.read_file("xxx_cube.xml", True)

x = RubiksCube(3)
x2 = RubiksCube(3)
x2.turn_z(-1,1)

#RubiksCubeConverter.to_visual_cube(myObject._start_cube)
#RubiksCubeConverter.to_visual_cube(myObject2._start_cube)


main = PatternFinder(3)
#print main.find_pattern(x, x2)
print main.find_pattern(myObject2._start_cube, myObject._start_cube)


#print main.find_pattern(x, x2)
#print main.find_pattern(myObject._start_cube, myObject2._start_cube)
#for cube in mycubes:
