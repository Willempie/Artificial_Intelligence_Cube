import sqlite3


class CreateDatabase:

    def __init__(self):
        return

    def create_new_databasefile(self, database_location, database_name):
        try:
            database = open(database_location + database_name + ".db", 'w')
        except IOError:
            print("File error: ")

    def database_setup(self, database_location):
        return
