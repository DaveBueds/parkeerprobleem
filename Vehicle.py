class Vehicle(object):
    #de data die binnekomt van CSV is van type str --> CASTEN!

    wagenBezet = False #wagen niet op slot
    def __init__(self, vehicle):
        self.vehicle = int(vehicle)

    def printVehicle(self):
        print( "Vehicle: ", self.vehicle)

    def wagenOpSlot(self):
        self.wagenBezet = True
        print("Wagen %s is op slot", self.vehicle)