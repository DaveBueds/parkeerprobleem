class Vehicle(object):
    #de data die binnekomt van CSV is van type str --> CASTEN naar int!

    wagenBezet = False #wagen niet op slot
    bezetVan = 0
    bezetTot = 0
    zone = None

    def __init__(self, vehicle):
        self.vehicle = int(vehicle)

    def getVehicle(self):
        return self

    def printVehicle(self):
        print( "Vehicle: ", self.vehicle)

    def wagenOpSlot(self, bezetVan, bezetTot):
        self.wagenBezet = True
        self.bezetVan = bezetVan
        self.bezetTot = bezetTot
        #print("Wagen ", self.vehicle, " is op slot gezet")

    def isWagenNogBezet(self):
        return [self.bezetVan, self.bezetTot]

    def wagenAfSlot(self, vorigeBezetVan, vorigeBezetTot):
        self.wagenBezet = False
        self.bezetVan = vorigeBezetVan
        self.bezetTot = vorigeBezetTot
        #print("Wagen ", self.vehicle, " slot is afgezet")

    def vehicleToZone(self, req):
        self.zone = req.zone
        print("Req ",req.id, "ToZone: ", req.zone, "car: ", self.vehicle)
        return self.vehicle, self.zone

    def getVehicleToZone(self):
        #print("Request ", self.id, " heeft voertuig ", self.toegewezenVoertuig)
        return self.vehicle, self.zone

    def resetVehicle(self):
        self.wagenBezet = False
        self.bezetVan = 0
        self.bezetTot = 0
        self.zone = None