class Zone(object):
    #de data die binnekomt van CSV is van type str --> CASTEN!


    def __init__(self, id, buurzones):
        self.id = int(id)
        self.buurzones = buurzones

    def printZone(self):
        print( "Zone: ", self.id,
               "Buurzones: ", self.buurzones)
