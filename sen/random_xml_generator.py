import xml.etree.ElementTree as ET
from pathArray import storage
from random import randint, choice

class RandomXmlGenerator:

    def __init__(self, filename):
        self.filename = filename


    def set_random_limits(self):
        self.spawnCap = 50
        self.spawnTimer = 6
        self.multiSpawnLimit = 2
        self.spawnRates = [5,15,90,95,100]

    @staticmethod
    def toXml(i_type, i_location, i_direction, i_time):
            vehicle = ET.Element('Item')

            type = ET.Element('Type')
            type.text = str(i_type)
            vehicle.append(type)

            location = ET.Element('StartPoint')
            location.text = str(i_location)
            vehicle.append(location)

            direction = ET.Element('EndPoint')
            direction.text = str(i_direction)
            vehicle.append(direction)

            time = ET.Element('Time')
            time.text = str(i_time)
            vehicle.append(time)

            return vehicle

    def generate(self):
        current_file_name = self.filename + ".xml"


        data = ET.Element("Data")
        for time in range(self.spawnCap):

            current_time = time * self.spawnTimer
            current_spawn_set = []
            current_roads = []

            for multi in range(self.multiSpawnLimit):

                vehicle = self.getRandomVehicle()

                while vehicle in current_spawn_set or vehicle[0] in current_roads:
                    vehicle = self.getRandomVehicle()

                current_roads.append(vehicle[0])

                current_spawn_set.append(vehicle)
                vehicle = self.getRandomVehicle()

                data.append(self.toXml(vehicle[2], vehicle[0], vehicle[1], current_time))

        tree = ET.ElementTree(data)
        tree.write(current_file_name, "utf-8", True )

    def getRandomVehicle(self):
        vehicle_type = randint(1,96)

        for chance in self.spawnRates:
            if vehicle_type <= chance:
                vehicle_type = self.spawnRates.index(chance)
                break

        temp_array = []
        for road in storage.path_array:
            if isinstance(road[2], int):
                if vehicle_type is road[2]:
                    temp_array.append(road)
            else:
                if vehicle_type in road[2]:
                    temp_array.append(road)

        road = choice(temp_array)
        return [road[0], road[1], vehicle_type]

x = RandomXmlGenerator("tiny")
x.set_random_limits()

#for z in range(50):
#    print x.getRandomVehicle()
x.generate()