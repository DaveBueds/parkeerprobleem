import csv

from Request import Request
from Zone import Zone
from Vehicle import Vehicle

aantalRequests = 0
aantalZones = 0
aantalVehicles = 0
aantalDays = 0

def	neemGetal(rijId):
	return ''.join(filter(lambda x: x.isdigit(), rijId)) #cast naar int


requestList = []
zoneList = []
vehicleList = []
aantalDagen = 0
def readCSV(filenaam):
    #LEZEN van de csv file
    with open(filenaam, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in csvreader:
            """ #Alles in row is van type str, zelf casten indien nodig! """
            #print (type(row[0]))
            #print(row[0])

            if "+Request" in row[0]:
                aantalRequests = int(row[0].split(": ")[1])
                print("Aantal requests:", aantalRequests)
                requestsToObject = True
                zonesToObject = False
                vehiclesToObject = False
                continue #forceer volgende for lus, anders wordt if onderaan 1x teveel uitgevoerd

            if "+Zones" in row[0]:
                aantalZones = int(row[0].split(": ")[1])
                print("Aantal zones:", aantalZones)
                requestsToObject = False
                zonesToObject = True
                vehiclesToObject = False
                continue #forceer volgende for lus, anders wordt if onderaan 1x teveel uitgevoerd


            if "+Vehicles" in row[0]:
                aantalVehicles = int(row[0].split(": ")[1])
                print("Aantal vehicles:", aantalVehicles)
                requestsToObject = False
                zonesToObject = False
                vehiclesToObject = True
                continue #forceer volgende for lus, anders wordt if onderaan 1x teveel uitgevoerd

            if "+Days" in row[0]:
                aantalDagen = int(row[0].split(": ")[1])
                print("Aantal dagen:", aantalDagen)
                requestsToObject = False
                zonesToObject = False
                vehiclesToObject = False
                break #einde van file, breek uit lees lus

            if requestsToObject:
                voertuigenlijst_string = row[5].split(',')
                voertuigenlijst_int = []
                for i in voertuigenlijst_string:
                    voertuigenlijst_int.append(int(neemGetal(i)))
                request = Request(neemGetal(row[0]),neemGetal(row[1]),row[2],row[3],row[4],voertuigenlijst_int,row[6],row[7])
                request.printReq()
                requestList.append(request)

            if zonesToObject:
                zone = Zone(neemGetal(row[0]))
                zone.printZone()
                zoneList.append(zone)

            if vehiclesToObject:
                vehicle = Vehicle(neemGetal(row[0]))
                vehicle.printVehicle()
                vehicleList.append(vehicle)

    csvfile.close()
    return [requestList, zoneList, vehicleList, aantalDagen]
