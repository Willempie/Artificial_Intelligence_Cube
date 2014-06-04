from database.output import Output


class Interface(Output):

    def __init__(self):
        return

    def write(self, information):
        print "Interface output:"
        print information
