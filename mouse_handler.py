from visual_common.cvisual import vector

__author__ = 'Willem'


class MouseHandler():

    __cube_display = None
    __drag_pos = None
    __start_position = None

    def __init__(self, cube_display):
        self.__cube_display = cube_display

    def bind_grab(self):
        self.__cube_display.bind('mousedown', self.grab)

    def bind_mouse_click(self):
        self.__cube_display.bind('click', self.mouse_click)

    def mouse_click(self, event):
        print("Object address: ", event.pick)

    def grab(self, event):
        #print("Block Address: ", event.pick)
        self.__start_position = event.pickpos
        print("Startposition: ", self.__start_position)
        self.__drag_pos = event.pickpos
        # bind mouse movement
        self.__cube_display.bind('mousemove', self.move, event.pick)
        self.__cube_display.bind('mouseup', self.drop)

    def move(self, event, obj):
        new_pos = self.__cube_display.mouse.project(normal=(0, 0, 1))
        if new_pos != self.__drag_pos:
            #obj.pos += new_pos - self.__drag_pos
            #print("X-as: ", new_pos.x)
            #print("Y-as: ", new_pos.y)
            #print("Z-as: ", new_pos.z)
            self.__drag_pos = new_pos

    def calc_direction(self, last_position):
        direction = None
        x_start_position = self.__start_position.x
        y_start_position = self.__start_position.y

        x_last_position = last_position.x
        y_last_position = last_position.y

        difference_x = x_last_position - x_start_position
        difference_y = y_last_position - y_start_position

        if abs(difference_x) > abs(difference_y):
            # x is the direction
            if difference_x < 0:
                print("turn x left")
            else:
                print("turn x right")
        else:
            # y is the direction
            if difference_y < 0:
                print("turn y bottom")
            else:
                print("turn y top")

    def drop(self, event):
        # unbind mousemovement
        self.__cube_display.unbind('mousemove', self.move)
        self.__cube_display.unbind('mouseup', self.drop)

        self.calc_direction(event.pickpos)