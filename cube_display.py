from visual import *


class CubeDisplay():

    __L = 500  # length for window
    __d = 50

    __display = None

    def __init__(self, w, show_axis):
        window_size = w.win.GetSize()
        y = window_size.y-self.__L

        # init display
        self.__display = display(window=w, x=10, y=y, width=self.__L-2*self.__d,
                                 height=self.__L-2*self.__d,
                                 #background=color.gray(0.8), range=(25, 25, 25), forward=(0, 1, 2),
                                 background=color.gray(0.8), range=(25, 25, 25),
                                 lights=[], ambient=color.gray(1), userzoom = False)

        axis_frame = frame(pos=vector(0,0,0))

        axis_arrow_length = 20
        label_opacity = 0.5
        arrow_color = (0,0,0)


        arrow(frame=axis_frame, pos=(0,0,0), axis=(5,0,0), length=axis_arrow_length, shaftwidth=1, color=arrow_color)
        x_axis = label(frame=axis_frame, text="X-as +", space=0.2, pos=(axis_arrow_length,0), opacity=label_opacity)
        arrow(frame=axis_frame, pos=(0,0,0), axis=(-5,0,0), length=axis_arrow_length, shaftwidth=1, color=arrow_color)
        x_axis_min = label(frame=axis_frame, text="X-as -", space=0.2, pos=(-axis_arrow_length,0), opacity=label_opacity)

        arrow(frame=axis_frame, pos=(0,0,0), axis=(0,5,0), length=axis_arrow_length, shaftwidth=1, color=arrow_color)
        y_axis = label(frame=axis_frame, text="Y-as +", space=0.2, pos=(0,axis_arrow_length), opacity=label_opacity)
        arrow(frame=axis_frame, pos=(0,0,0), axis=(0,-5,0), length=axis_arrow_length, shaftwidth=1, color=arrow_color)
        y_axis_min = label(frame=axis_frame, text="Y-as -", space=0.2, pos=(0,-axis_arrow_length), opacity=label_opacity)

        arrow(frame=axis_frame, pos=(0,0,0), axis=(0,0,5), length=axis_arrow_length, shaftwidth=1, color=arrow_color)
        z_axis = label(frame=axis_frame, text="Z-as +", space=0.2, pos=(0,0,axis_arrow_length), opacity=label_opacity)
        arrow(frame=axis_frame, pos=(0,0,0), axis=(0,0,-5), length=axis_arrow_length, shaftwidth=1, color=arrow_color)
        z_axis_min = label(frame=axis_frame, text="Z-as -", space=0.2, pos=(0,0,-axis_arrow_length), opacity=label_opacity)

        axis_frame.visible = show_axis


    def get_display(self):
        return self.__display