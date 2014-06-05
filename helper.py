from visual import *
import copy

class Helper:

    CUBE_SIDES = ["Front", "Back", "Top", "Bottom", "Left", "Right"]
    CUBE_COLOR_NAME = ['Rood', 'Paars', 'Geel', 'Wit', 'Blauw', 'Groen']
    CUBE_COLOR = [color.red, (1, 0, 1), color.yellow, color.white, color.blue, color.green]
    CUBE_DUMMIE_COLOR = color.gray(0.6)

    @staticmethod
    def array_2d_all_same(input_array, size):
        memory = input_array[0][0]
        for x in xrange(size):
            for y in xrange(size):
                current = input_array[x][y]
                if memory != current:
                    return False
        return True

    @staticmethod
    def _match_cube(cube_a, cube_b):
        if cube_a is None or cube_b is None:
            raise ValueError("Input doesn't match")

        for color in range(6):
            storage = []

            for side in Helper.CUBE_SIDES:
                side_a = cube_a.get_side(side)
                side_b = cube_b.get_side(side)

                storage.append(side_a == side_b)

            print storage
            if all(storage):
                return True

        return False

    @staticmethod
    def match_cube(cube_a, cube_b):
        a = copy.deepcopy(cube_a)
        b = copy.deepcopy(cube_b)

        print a.my_print()
        print b.my_print()

        if Helper._match_cube(a,b):
            return True

        #for side in range(5):
        #    if side == 0:
        #        Helper._turn_step(a,b,"y", "x")
        #    elif side == 1:
        #        Helper._turn_step(a,b,"y", "z")
        #    elif side == 2:
        #        Helper._turn_step(a,b,"y", "x")
        #    elif side == 3:
        #        Helper._turn_step(a,b,"z", "y")
        #    elif side == 4:
        #        a.turn("z", -1, 1)
        #        Helper._turn_step(a,b,"z", "y")
        #
        #    if Helper._match_cube(a,b):
        #        return True
        #
        #return False

    @staticmethod
    def _turn_step(a, b, axis, next_axis):
        a.turn(axis, -1, 1)

        if Helper._match_cube(a,b):
            return True

        for x in range(3):
            a.turn(next_axis, -1, 1)

            if Helper._match_cube(a,b):
                return True