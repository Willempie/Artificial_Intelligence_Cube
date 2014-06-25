from database.bridge import Bridge


class Handler(Bridge):

    def __init__(self, output):
        self.__output = output

    def write(self, information):
        print "handler output"
        self.__output.write(information)

    def get_output_type(self):
        return self.__output