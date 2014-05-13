from database_handler import DatabaseHandler

database_handler = DatabaseHandler("C:/Users/Willem/PycharmProjects/Artificial_Intelligence_Cube/database/cube_database.db")
result = database_handler.insert("INSERT INTO solve (date, size) VALUES ('8-5-2014', 5)")
print result



# sql_query_array = ["CREATE TABLE steps (id INTEGER PRIMARY KEY AUTOINCREMENT,"
#                        "parent_id INTEGER NOT NULL,"
#                        "cube VARCHAR NOT NULL,"
#                        "code VARCHAR NOT NULL,"
#                        "step VARCHAR NOT NULL,"
#                        "FOREIGN KEY(parent_id) REFERENCES solve(id));",
#
#                    "CREATE TABLE solve (id INTEGER PRIMARY KEY AUTOINCREMENT,"
#                        "date VARCHAR NOT NULL,"
#                        "size INTEGER NOT NULL )"
#                    ]
#
# database_handler.create_database("C:/Users/Willem/PycharmProjects/Artificial_Intelligence_Cube/database/",
#                                  "cube_database", sql_query_array)


#
# fileee = "C:/Users/Willem/PycharmProjects/Artificial_Intelligence_Cube/database/new_database.txt"
# # text_file = "C:/Users/Willem/PycharmProjects/Artificial_Intelligence_Cube/database/new_database.txt"
#
# opened_file = open(fileee, "r")
# print opened_file.read()