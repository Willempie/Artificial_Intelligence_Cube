from database.database_handler import DatabaseHandler
from database.output import Output


class File(Output):

    def __init__(self, file_location):
        self.__database_handler = DatabaseHandler(file_location)

    def write(self, information):
        print "file output"
        self.__database_handler.connect_database()
        print(self.__database_handler.select(information))
        self.__database_handler.close_connection()


