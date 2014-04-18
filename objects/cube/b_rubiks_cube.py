from b_cube import BCube


class BRubiksCube(BCube):

    def __init__(self):
        BCube.__init__(self)

    def reset_array(self, set_color):
        raise NotImplementedError("Should be implemented")

    def set_part(self, side, x, y, color):
        raise NotImplementedError("Should be implemented")

    def get_size(self):
        raise NotImplementedError("Should be implemented")

    def check_front(self):
        raise NotImplementedError("Should be implemented")

    def set_front_part(self, x, y):
        raise NotImplementedError("Should be implemented")

    def check_back(self):
        raise NotImplementedError("Should be implemented")

    def set_back_part(self, x, y):
        raise NotImplementedError("Should be implemented")

    def check_top(self):
        raise NotImplementedError("Should be implemented")

    def set_top_part(self, x, y):
        raise NotImplementedError("Should be implemented")

    def check_bottom(self):
        raise NotImplementedError("Should be implemented")

    def set_bottom_part(self, x, y):
        raise NotImplementedError("Should be implemented")

    def check_left(self):
        raise NotImplementedError("Should be implemented")

    def set_left_part(self, x, y):
        raise NotImplementedError("Should be implemented")

    def check_right(self):
        raise NotImplementedError("Should be implemented")

    def set_right_part(self, x, y):
        raise NotImplementedError("Should be implemented")
