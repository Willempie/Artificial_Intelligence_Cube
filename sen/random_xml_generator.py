import xml.etree.ElementTree as ET
import time
from random import randint

class RandomXmlGenerator:

    def __init__(self, filename):
        self.filename = filename

        pass

    def set_random_limits(self):
        self.vehicles = 500
        self.startTime = time
        self.timeSpan = 200
        self.spawnTimer = 5
        self.multiSpawn = True
        self.multiSpawnLimit = 5

        self.spawnRates = [1,1,1,1,1]
        print self.startTime.strftime("%Y-%m-%d %H:%M:%S")
        self.startTime.sleep(1)
        self.startTime.sleep(1)
        self.startTime.sleep(1)
        self.startTime.sleep(1)
        print self.startTime.strftime("%Y-%m-%d %H:%M:%S")
        #for x in range(10000000):
        #    randomNumb = x * x * x * x * x
        #print self.startTime.strftime("%Y-%m-%d %H:%M:%S")


    @staticmethod
    def toXml(i_type, i_location, i_direction, i_time):
            vehicle = ET.Element('Item')

            type = ET.Element('Type')
            type.text = str(i_type)
            vehicle.append(type)

            location = ET.Element('Location')
            location.text = str(i_location)
            vehicle.append(location)

            direction = ET.Element('Direction')
            direction.text = str(i_direction)
            vehicle.append(direction)

            time = ET.Element('Time')
            time.text = str(i_time)
            vehicle.append(time)

            return vehicle

    def generate(self):
        current_file_name = self.filename + " " + str(x+1) + ".xml"


        data = ET.Element("Data")
        for vehicle in range(self.vehicles):
            type = randint(0,4)
            location = randint(0,3)
            direction = randint(0,3)
            time = 0
            data.append(self.toXml(type, location, direction, time))

        tree = ET.ElementTree(data)
        tree.write(current_file_name, "utf-8", True)

x = RandomXmlGenerator("Willem")
x.set_random_limits()
#x.generate()