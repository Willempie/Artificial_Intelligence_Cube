class Side:
    _size = None
    _array = None

    def __init__(self, size, color=None):
        if size < 2:
            raise ValueError('Minimum size = 2 (Current size = '+str(size)+')')

        self._size = size
        self._array = [[color for i in xrange(size)] for j in xrange(size)]

    def get_part(self, x, y):
        return self._array[y][x]

    def set_part(self, x, y, value):
        self._array[y][x] = value

    def get_row_x(self, index):
        return_array = []
        for member in self._array:
            return_array.append(member[index])
        return return_array

    def set_row_x(self, index, values):
        for i in range(self._size):
            self._array[i][index] = values[i]

    def get_row_y(self, index):
        return self._array[index]

    def set_row_y(self, index, values):
        self._array[index] = values

    def my_print(self):
        return_string = ''
        for member in self._array:
            return_string += str(member) + '\n'
        return return_string
