from side import Side


class Cube:
    CONST_DIRECTION = ('up', 'down', 'left', 'right')
    
    __size = 2

    _front = None
    __back = None
    __top = None
    __bottom = None
    __left = None
    __right = None

    def __init__(self, size=2):
        self.__size = size

        self._front = Side(size, 1)
        self.__back = Side(size, 2)
        self.__top = Side(size, 3)
        self.__bottom = Side(size, 4)
        self.__left = Side(size, 5)
        self.__right = Side(size, 6)

    def turn_x(self, index, direction):
        front = self._front.get_row_x(index)
        top = self.__top.get_row_x(index)
        back = self.__back.get_row_x(index)
        bottom = self.__bottom.get_row_x(index)

        if direction == self.CONST_DIRECTION[3]: #right
            self._front.set_row_x(index, bottom)
            self.__top.set_row_x(index, front)
            self.__back.set_row_x(index, top)
            self.__bottom.set_row_x(index, back)

            if index == 0:
                self.__right = zip(*self.__right[::-1])
            elif index == self.__size-1:
                self.__left = zip(*self.__left[::1])

        elif direction == self.CONST_DIRECTION[2]: #left
            self._front.set_row_x(index, top)
            self.__top.set_row_x(index, back)
            self.__back.set_row_x(index, bottom)
            self.__bottom.set_row_x(index, front)

    def turn_y(self, index, direction):
        front = self._front.get_row_y(index)
        right = self.__right.get_row_y(index)
        back = self.__back.get_row_y(index)
        left = self.__left.get_row_y(index)

        if direction == self.CONST_DIRECTION[3]: #right
            self._front.set_row_y(index, right)
            self.__right.set_row_y(index, back)
            self.__back.set_row_y(index, left)
            self.__left.set_row_y(index, front)
        elif direction == self.CONST_DIRECTION[2]: #left
            self._front.set_row_y(index, left)
            self.__right.set_row_y(index, front)
            self.__back.set_row_y(index, right)
            self.__left.set_row_y(index, back)

    def turn_z(self, index, direction):
        top = self.__top.get_row_y(index)
        right = self.__right.get_row_y(index)
        bottom = self.__bottom.get_row_y(index)
        left = self.__left.get_row_y(index)

        if direction == self.CONST_DIRECTION[3]: #right
            self.__top.set_row_y(index, left)
            self.__right.set_row_y(index, top)
            self.__bottom.set_row_y(index, right)
            self.__left.set_row_y(index, bottom)
        elif direction == self.CONST_DIRECTION[2]: #left
            self.__top.set_row_y(index, right)
            self.__right.set_row_y(index, bottom)
            self.__bottom.set_row_y(index, left)
            self.__left.set_row_y(index, top)

    def my_print(self):
        return_string = 'top \n'
        return_string += self.__top.my_print() + '\n'
        return_string += 'front \n'
        return_string += self._front.my_print() + '\n'
        return_string += 'bottom \n'
        return_string += self.__bottom.my_print() + '\n'
        return_string += 'back \n'
        return_string += self.__back.my_print() + '\n'

        return_string += 'left \n'
        return_string += self.__left.my_print() + '\n'
        return_string += 'right \n'
        return_string += self.__right.my_print() + '\n'
        return return_string