
class Step:

    def __init__(self, axis, rows, direction):
        if axis.lower() in ['x','y','z']:
            self.axis = axis.lower()

        if rows == 'All' or rows == -1:
            self.rows = [-1]
        elif isinstance(axis, list):
            self.rows = rows
        else:
            self.rows = [rows]

        if direction in [-1, 1]:
            self.direction = direction
