class Zone(object):
    #de data die binnekomt van CSV is van type str --> CASTEN!

    def __init__(self, zone):
        self.zone = int(zone)

    def printZone(self):
        print( "Zone: ", self.zone)