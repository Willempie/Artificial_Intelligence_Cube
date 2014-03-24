from visual import *

class BFps:

    def __init__(self, fps=24, rate=24):

        self.degrees90 = pi / 2
        self.degrees180 = pi

        if fps is None or fps < 1:
            self.fps = 1
        else:
            self.fps = fps

        if rate is None or rate < 1:
            self.rate = 1
        else:
            self.rate = rate