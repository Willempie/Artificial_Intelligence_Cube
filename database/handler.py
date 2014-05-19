from database.bridge import Bridge
from database.file import File
from database.interface import Interface
from database.output import Output


class Handler(Bridge):

    def __init__(self, implementation):
        self.__implementation = implementation

    def write(self):
        print "handler output"
        self.__implementation.write()


interface = Interface()
dfile = File()

handler = Handler(interface)
handler.write()
handler = Handler(dfile)
handler.write()