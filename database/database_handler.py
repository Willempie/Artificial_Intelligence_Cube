import sqlite3
import os.path


class Database:

    __database_location = None
    __database_connection = None

    def __init__(self, database_location):
        self.__database_location = database_location

    def create_database(self):
        return

    # connect to database
    def connect_database(self):
        if os.path.isfile(self.__database_location):
            try:
                self.__database_connection = sqlite3.connect(self.__database_location)
            except sqlite3.Error:
                print "Failed to open database connection \n"
            return

    # get database cursor for fetching results
    def get_database_cursor(self):
        if self.__database_connection is not None:
            return self.__database_connection.cursor


database = Database("/database.db")
database.connect_database()