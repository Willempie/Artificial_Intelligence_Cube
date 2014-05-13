class BCube:

    def __init__(self):
        pass

    def turn(self, xyz, direction):
        raise NotImplementedError("Should be implemented")

    def turn_x(self, direction):
        raise NotImplementedError("Should be implemented")

    def turn_y(self, direction):
        raise NotImplementedError("Should be implemented")

    def turn_z(self, direction):
        raise NotImplementedError("Should be implemented")

    def get_side(self, side):
        raise NotImplementedError("Should be implemented")

    def set_side(self, side, item):
        raise NotImplementedError("Should be implemented")

    def contains(self, item):
        raise NotImplementedError("Should be implemented")

    def set_front(self, color):
        raise NotImplementedError("Should be implemented")

    def get_front(self):
        raise NotImplementedError("Should be implemented")

    def set_back(self, color):
        raise NotImplementedError("Should be implemented")

    def get_back(self):
        raise NotImplementedError("Should be implemented")

    def set_top(self, color):
        raise NotImplementedError("Should be implemented")

    def get_top(self):
        raise NotImplementedError("Should be implemented")

    def set_bottom(self, color):
        raise NotImplementedError("Should be implemented")

    def get_bottom(self):
        raise NotImplementedError("Should be implemented")

    def set_left(self, color):
        raise NotImplementedError("Should be implemented")

    def get_left(self):
        raise NotImplementedError("Should be implemented")

    def set_right(self, color):
        raise NotImplementedError("Should be implemented")

    def get_right(self):
        raise NotImplementedError("Should be implemented")