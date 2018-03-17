class Vehicle(object):
    #de data die binnekomt van CSV is van type str --> CASTEN!

    wagenBezet = False #wagen niet op slot
    bezetTot = 0
    def __init__(self, vehicle):
        self.vehicle = int(vehicle)

    def printVehicle(self):
        print( "Vehicle: ", self.vehicle)

    def wagenOpSlot(self, bezetTot):
        self.wagenBezet = True
        self.bezetTot = bezetTot
        #print("Wagen ", self.vehicle, " is op slot gezet")

    def isWagenNogBezet(self):
        return self.bezetTot

    def wagenAfSlot(self):
        self.wagenBezet = False
        self.bezetTot = 0
        #print("Wagen ", self.vehicle, " slot is afgezet")