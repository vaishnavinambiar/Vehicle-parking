import logging
logging.basicConfig(filename='parking.log',level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')

types = ['Car', 'Bike', 'Van', 'Bus']
vehicles = []

class Vehicle:
    def __init__(self,types):
        self.types=types

    def getTypes(self):
        """To get which type of vehicle is coming to park"""
        if self.types in types:
            return "Parking allowed"
        else:
            return "no parking"

    def addvehicle(self):
        """To park the vehicle"""
        try:
            if self.types in types:
                vehicles.append(self.types)
                logging.info("Type of vehicle parked is: %s ",vehicles)
                return vehicles
        except:
            return "None"

            
class ParkingLevel:
    def __init__(self, types, level_number, limit):
        self.types=types
        self.level_number = level_number
        self.limit = limit

    def getLevel(self):
        """To get the level to park the vehicle"""
        if self.types in types:
            logging.info("Available level is: %s",self.level_number)
            return 'park '+ self.types + ' in level ' + self.level_number
        else:
           return "not allowed"

    def createlevel(self):
        """To create new level"""
        types_limit = { 'Car': 20, 'Bike': 50, 'Van':10, 'Bus':7}
        if self.types in types_limit.keys() and self.limit> types_limit[self.types]:
            return "go to next level and bus restricted"
        else:
            return "Invalid"

        
class Exitpanel:
    def __init__(self, types):
        self.types = types

    def removevehicle(self):
        """To unpark the vehicle"""
        user_option = raw_input("Do you want to unpark? y/n ")
        try:
            if user_option == 'y':
                del vehicles[:]
                return vehicles
        except ValueError:
            return "OK"

vehicle = Vehicle('Car')
print vehicle.getTypes()
print vehicle.addvehicle()
level = ParkingLevel('Car', '3', 22)
print level.getLevel()
print level.createlevel()
exitpanel = Exitpanel('Car')
print exitpanel.removevehicle()
       
                

