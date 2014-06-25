from database.file import File
from database.handler import Handler
from logic.pattern_finder import PatternFinder
import copy
import time
from objects.cube.rubiks_cube import RubiksCube


class GenerateDatabaseDisplay():

    __default_button_width = 88
    __default_button_height = 26

    __cube_size = 2

    def __init__(self):
        # generate cube
        self.cube = RubiksCube(self.__cube_size)

        # cube list
        self.copy_cubes = []

        self.pattern_finder = PatternFinder(self.__cube_size)

        file = File("C:\Users\Willem\PycharmProjects\Artificial_Intelligence_Cube\database\cube_database.db")
        self.database_handler = Handler(file)

        self.solved = False

    def turn_x(self):
        return

    def copy_cube(self):
        copy_cube = copy.deepcopy(self.cube)
        return copy_cube

    def turn_cube(self, cube, axis, row, direction):
        local_cube = copy.deepcopy(cube)
        local_cube.turn(axis,row,direction)
        return local_cube

    def generate_database(self):
        self.copy_cubes.append([self.copy_cube()])


        row_counter = 0
        start_time = time.time()
        while (row_counter + 1) < 4:

            if row_counter >= 0:
                for counter in range(len(self.copy_cubes) - 1):
                    for previous_cube in range(len(self.copy_cubes[counter])):
                        self.pattern_finder.set_base_cube(self.copy_cubes[counter][previous_cube])
                        self.pattern_finder._generate_cubes()
                        self.pattern_finder.create_next_set()
                        result = []
                        if self.copy_cubes[row_counter]:
                            for current_cube in range(len(self.copy_cubes[row_counter])):
                                self.pattern_finder.set_matching_cube(self.copy_cubes[row_counter][current_cube])
                                if not self.pattern_finder._match():
                                    result.append(self.copy_cubes[row_counter][current_cube])
                            self.copy_cubes[row_counter] = result
                        else:
                            break
                        #self.insert_in_database(('''insert into steps(parent_id, cube, code, step) values(:parent_id,:cube,:code,:step)''', \
                        #    ({'parent_id':1, 'cube':self.copy_cubes[counter][previous_cube].convert_to_string(), 'code':3, 'step':4})))
                        #
                        self.insert_in_database(("insert into steps(parent_id, cube, code, step) values(?,?,?,?);", \
                            ('1', self.copy_cubes[counter][previous_cube].convert_to_string(), '2', '3')))
                        #self.insert_in_database('''insert into steps(parent_id, cube, code, step) values(1, ''' + self.copy_cubes[counter][previous_cube].convert_to_string() + ''', 3,4)''')

                # # search same cube
                # for current_cube in range(len(self.copy_cubes[row_counter])):
                #     self.pattern_finder.set_base_cube(self.copy_cubes[row_counter][current_cube])
                #     self.pattern_finder._generate_cubes()
                #     self.pattern_finder.create_next_set()
                #     for previous_cube in range(len(self.copy_cubes[row_counter-1])):
                #         self.pattern_finder.set_matching_cube(self.copy_cubes[row_counter-1][previous_cube])
                #         counter+=1
                #
                #         print counter
                #         print self.pattern_finder._match()
                #            # print "True"
                #         # remove same cube

            self.copy_cubes.append([])
            for cube in range(len(self.copy_cubes[row_counter])):

                self.copy_cubes[row_counter+1].append(self.turn_cube(self.copy_cubes[row_counter][cube], 'x', 0, 1))
                self.copy_cubes[row_counter+1].append(self.turn_cube(self.copy_cubes[row_counter][cube], 'x', 0, -1))
                self.copy_cubes[row_counter+1].append(self.turn_cube(self.copy_cubes[row_counter][cube], 'x', 1, 1))
                self.copy_cubes[row_counter+1].append(self.turn_cube(self.copy_cubes[row_counter][cube], 'x', 1, -1))

                self.copy_cubes[row_counter+1].append(self.turn_cube(self.copy_cubes[row_counter][cube], 'y', 0, 1))
                self.copy_cubes[row_counter+1].append(self.turn_cube(self.copy_cubes[row_counter][cube], 'y', 0, -1))
                self.copy_cubes[row_counter+1].append(self.turn_cube(self.copy_cubes[row_counter][cube], 'y', 1, 1))
                self.copy_cubes[row_counter+1].append(self.turn_cube(self.copy_cubes[row_counter][cube], 'y', 1, -1))

                self.copy_cubes[row_counter+1].append(self.turn_cube(self.copy_cubes[row_counter][cube], 'z', 0, 1))
                self.copy_cubes[row_counter+1].append(self.turn_cube(self.copy_cubes[row_counter][cube], 'z', 0, 1))
                self.copy_cubes[row_counter+1].append(self.turn_cube(self.copy_cubes[row_counter][cube], 'z', 0, -1))
                self.copy_cubes[row_counter+1].append(self.turn_cube(self.copy_cubes[row_counter][cube], 'z', 1, 1))
                self.copy_cubes[row_counter+1].append(self.turn_cube(self.copy_cubes[row_counter][cube], 'z', 1, -1))


            row_counter = row_counter + 1

        print "done"
        print len(self.copy_cubes)
        print len(self.copy_cubes[row_counter])
        print time.time() - start_time


    def insert_in_database(self, cube_string):
        self.database_handler.write(cube_string)
        pass

#x = GenerateDatabaseDisplay()
#x.generate_database()


