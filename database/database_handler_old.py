import sqlite3
import os.path


class DatabaseHandler:

    __database_location = None
    __database_connection = None

    __database_cursor = None

    def __init__(self, database_location):
        self.__database_location = database_location

    # create database with given sql querys in an array
    def create_database(self, database_location, database_name, sql_query_array):
        database_file_location = None
        try:
            database_file_location = database_location + database_name + ".db"
            open(database_file_location, 'a')
        except IOError:
            print("File error: ")
            return

        if sql_query_array:
            if database_file_location:
                self.connect_database(database_file_location)
                cursor = self.__database_cursor()

                for query in sql_query_array:
                    cursor.execute(query)

    # connect to database
    def connect_database(self):
        if os.path.isfile(self.__database_location):
            try:
                self.__database_connection = sqlite3.connect(self.__database_location)
                # set cursor
                self.set_database_cursor()
            except sqlite3.Error:
                print "Failed to open database connection \n"
            return

    # close connection
    def close_connection(self):
        if self.__database_connection:
            self.__database_connection.close()

    # set database cursor
    def set_database_cursor(self):
        if self.__database_connection is not None:
            self.__database_cursor = self.__database_connection.cursor

    def select(self, query):
        if os.path.isfile(self.__database_location):
            # connect to database
            self.connect_database()
            cursor = self.__database_cursor()
            if cursor:
                cursor = cursor.execute(query)
                result = []
                for row in cursor:
                    result.append(row)

                return result

    def insert(self, query_array):
        if os.path.isfile(self.__database_location):
            # connect to database
            self.connect_database()
            cursor = self.__database_cursor()
            if cursor:
                if isinstance(query_array, list):
                    for query in query_array:
                        cursor = cursor.execute(query)

                    #commit changes
                    self.__database_connection.commit()
                    self.close_connection()

                    return "Inserted all querys!"
                else:
                    print query_array
                    cursor = cursor.execute(query_array)
                    #commit changes
                    self.__database_connection.commit()
                    return "Inserted one!"
        return "Insertion failed!"

    def delete(self):
        # todo
        pass

    def update(self):
        # todo
        pass
