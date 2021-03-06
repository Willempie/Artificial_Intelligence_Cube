from visual_common.controls import color
from visual_common.cvisual import vector
from helper import Helper

class MouseHandler():

    __cube_display = None
    __drag_pos = None
    __start_position = None
    __cube = None

    __combobox_colors = None

    def __init__(self, display):
        self.__display = display
        self.__cube_display = display.cube_display.get_display()

    def bind_grab(self):
        self.__cube_display.bind('mousedown', self.grab)

    def bind_mouse_click(self, combobox):
        #self.__cube_display.bind('click', self.mouse_block_click)
        self.__combobox_colors = combobox

    def mouse_block_click(self, event, display):
        self.__display = display
        cube = self.__display._storage.current_cube
        clicked_box = cube.contains(event.pick)
        if clicked_box is not False:
            if event.button == "middle":
                cube.set_part(clicked_box[0], clicked_box[1], clicked_box[2], Helper.CUBE_DUMMIE_COLOR)
            else:
                selected_color = self.__combobox_colors.GetValue()
                current_color = Helper.CUBE_COLOR[Helper.CUBE_COLOR_NAME.index(selected_color)]
                cube.set_part(clicked_box[0], clicked_box[1], clicked_box[2], current_color)

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