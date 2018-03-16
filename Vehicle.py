class Vehicle(object):
    #de data die binnekomt van CSV is van type str --> CASTEN!

    def __init__(self, vehicle):
        self.vehicle = int(vehicle)

    def printVehicle(self):
        print( "Vehicle: ", self.vehicle)