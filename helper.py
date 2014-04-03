class Helper:

    CUBE_SIDES = ["Front", "Back", "Top", "Bottom", "Left", "Right"]

    @staticmethod
    def array_2d_all_same(input_array, size):
        memory = input_array[0][0]
        for x in xrange(size):
            for y in xrange(size):
                current = input_array[x][y]
                if memory != current:
                    return False
        return True