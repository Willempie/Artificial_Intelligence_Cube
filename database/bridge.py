from database.abstract_handler import AbstractHandler


class Bridge(AbstractHandler):

    def __init__(self):
        self.__implementation = None