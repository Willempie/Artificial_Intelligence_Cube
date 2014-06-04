from database.bridge import Bridge
from database.file import File
from database.interface import Interface
from database.output import Output


class Handler(Bridge):

    def __init__(self, output):
        self.__output = output

    def write(self, information):
        print "handler output"
        self.__output.write(information)

    def get_output_type(self):
        return self.__output


# interface = Interface()
# dfile = File("C:\Users\Willem\PycharmProjects\Artificial_Intelligence_Cube\database\cube_database.db")
#
# handler = Handler(interface)
# handler.write("SELECT * FROM solve")
# handler = Handler(dfile)
# handler.write("SELECT * FROM solve")