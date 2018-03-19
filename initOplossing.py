from Request import Request
from Zone import Zone
from Vehicle import Vehicle

def initOplossing(obj):
    print(obj[0][0].startTijd)
    requests = obj[0]
    zones = obj[1]
    vehicles = obj[2]

    #sorteer lijst op tijd (van klein naar groot)
    requests.sort(key=lambda x: x.startTijd, reverse=False)

    #neem eerste request in tijd
    print ("Eerste req in tijd: ", obj[0][0].id)
    for req in requests:
        if controleOfReqWagenHeeft(req):
            #Request heeft wagen
            print("Request", req.id ," heeft wagen(s), van: ", req.startTijd, "tot ", req.startTijd+req.duurTijd)
            wagenVrij = controleWagenBezet(req, vehicles)
            if not wagenVrij == None:
                req.reqToVehicle(wagenVrij)
                #vehicle to Zone
                if vehToZone(req, vehicles):
                    pass
                else:
                    req.reqToVehicleUnassign()
            else:
                print("GEEN WAGEN GEVONDEN VOOR req", req.id)


        else:
            print("ERROR: Request heeft geen wagen.")
        print ("\n")



"""Controleert of een request een lijst van wagens heeft, indien niet fout opvangen"""
def controleOfReqWagenHeeft(req):
    if not len(req.verhicleList) == 0:
        return True
    else:
        #request heeft geen wagen
        return False



"""Controleert of er een wagen in de lijst van de request beschikbaar is"""
def controleWagenBezet(req, vehicles):
    #loop door vehicle list
    for index, auto in enumerate(req.verhicleList):
        #print(index, auto)

        #print("Wagen bezet tot: ",vehicles[auto].isWagenNogBezet())
        if vehicles[auto].isWagenNogBezet() <= req.startTijd:
            #Controleren of wagen beschikbaar is nadat hij reeds gereserveerd is geweest
            #controle of er geen overlap zit in de tijd
            vehicles[auto].wagenAfSlot()

        if not vehicles[auto].wagenBezet: #wagen is niet bezet
            #print("Wagen ", vehicles[auto].vehicle ," is vrij")
            bezetTot = req.startTijd + req.duurTijd
            vehicles[auto].wagenOpSlot(bezetTot)
            return vehicles[auto].vehicle
            break
        else:
            #print("Wagen ", vehicles[auto].vehicle ," is niet vrij")
            pass
    #Indien geen vrij gevonden voertuig gevonden return None
    return None

def vehToZone(req, vehicles):
    rv = req.getReqToVehicle()

    auto = vehicles[rv[1]].getVehicle()
    #print("auto: ", auto)

    #controle zone van request, plaats voertuig in die zone
    #controle op vehicle in zone
    #print("AZ: ", auto.zone)
    if auto.zone == None:
        auto.vehicleToZone(req)
        return True
    else:
        #print("CONFLICT VEH TO ZONE")
        return False
