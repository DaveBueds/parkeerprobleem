class Vehicle(object):
    #de data die binnekomt van CSV is van type str --> CASTEN naar int!

    wagenBezet = False #wagen niet op slot
    bezetTot = 0
    zone = None

    def __init__(self, vehicle):
        self.vehicle = int(vehicle)

    def getVehicle(self):
        return self

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

    def vehicleToZone(self, req):
        self.zone = req.zone
        print("Req ",req.id, "ToZone: ", req.zone, "car: ", self.vehicle)
        return self.vehicle, self.zone

    def getVehicleToZone(self):
        #print("Request ", self.id, " heeft voertuig ", self.toegewezenVoertuig)
        return self.vehicle, self.zone

    def swapVehicleToZone(self, buurzone):
        self.zone = buurzone
        return self.vehicle, self.zone