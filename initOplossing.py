from Request import Request
from Zone import Zone
from Vehicle import Vehicle

def initOplossing(obj, initieleOpl):
    #print(obj[0][0].startTijd)
    requests = obj[0]
    zones = obj[1]
    vehicles = obj[2]
    aantalDagen = obj[3]

    #sorteer request lijst op tijd (van klein naar groot)
    requests.sort(key=lambda x: x.startTijd, reverse=False)

    #neem eerste request in tijd
    #print ("Eerste req in tijd: ", obj[0][0].id)
    for req in requests: #loop over alle requests en wijs deze toe
        maakOplossing(req, vehicles, zones, initieleOpl)
        #print("\n")

    for auto in vehicles:
        print("auto: ", auto.vehicle, "bezet van: ", auto.bezetVan,"bezet tot: ", auto.bezetTot)

    return [requests, zones, vehicles, aantalDagen]


"""Controleert of een request een lijst van wagens heeft, indien niet fout opvangen"""
def controleOfReqWagenHeeft(req):
    if not len(req.verhicleList) == 0:
        return True
    else:
        return False #request heeft geen wagen

def maakOplossing(req, vehicles, zones, initieleOpl):
    zone = req.zone
    buuzones = zones[zone].buurzones
    #print("Req: ", req.id, "zone: ", zone, "buren: ", buuzones)

    if not initieleOpl:
        print("optimize opl")


    if controleOfReqWagenHeeft(req):  # Request heeft wagen
        #print("Request", req.id, " heeft wagen(s): ", req.verhicleList, ", van: ", req.startTijd, "tot ", req.startTijd + req.duurTijd)

        for index, auto in enumerate(req.verhicleList):  # loop door vehiclelist
            vorigeBezetVan = vehicles[auto].bezetVan
            vorigeBezetTot = vehicles[auto].bezetTot
            #print("auto: ", auto, "bezetTot: ", vehicles[auto].bezetTot)

            if vehicles[auto].isWagenNogBezet()[1] <= req.startTijd:
                vehicles[auto].wagenAfSlot(vorigeBezetVan, vorigeBezetTot)

            if not vehicles[auto].wagenBezet:  # indien wagen vrij
                #print("bezetTot: ", vehicles[auto].bezetTot)
                bezetVan = req.startTijd
                bezetTot = req.startTijd + req.duurTijd
                #vehicles[auto].wagenOpSlot(bezetTot)
                wagenVrij = vehicles[auto].vehicle

               # print("Gevonden wagen: ", wagenVrij, "staat in zone: ", vehicles[wagenVrij].zone)

                if vehicles[wagenVrij].zone == None:  # als voertuig nog geen zone heeft
                   # print("Voertuig heeft nog geen zone")
                    vehicles[wagenVrij].vehicleToZone(req)  # wijs to aan eigen zone
                    vehicles[auto].wagenOpSlot(bezetVan, bezetTot)
                    req.reqToVehicle(wagenVrij)  # request krijgt dat voertuig
                    break

                elif vehicles[wagenVrij].zone == zone: # check voertuig in eigen zone staat
                   # print("Voertuig in eigen zone")
                    # voertuig zone moet niet aangepast worden
                    vehicles[auto].wagenOpSlot(bezetVan, bezetTot)
                    req.reqToVehicle(wagenVrij)  # request krijgt dat voertuig
                    break

                else:  # check of voertuig in buurzones staat
                    for buur in buuzones:
                        if vehicles[wagenVrij].zone == buur:
                           # print("Wagen staat in buurzone", buur)
                            vehicles[auto].wagenOpSlot(bezetVan, bezetTot)
                            req.reqToVehicle(wagenVrij)  # request krijgt dat voertuig
                            break
                        else:
                            print("Wagen staat NIET in buurzone", buur)
                            # ga verder in lijst van wagens als er nog wagens zijn

            else:
               print("WAGEN", vehicles[auto].vehicle, "BEZET TOT: ", vehicles[auto].bezetTot)

            if index == len(req.verhicleList)-1:
               print("EINDE LIJST")

    else:
        print("ERROR: Request heeft geen lijst met wagen(s).")