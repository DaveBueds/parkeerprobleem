from Request import Request
from Zone import Zone
from Vehicle import Vehicle

def initOplossing(obj):
    #print(obj[0][0].startTijd)
    requests = obj[0]
    zones = obj[1]
    vehicles = obj[2]
    aantalDagen = obj[3]

    #sorteer request lijst op tijd (van klein naar groot)
    requests.sort(key=lambda x: x.startTijd, reverse=False)

    #neem eerste request in tijd
    print ("Eerste req in tijd: ", obj[0][0].id)
    for req in requests:
        zone = req.zone
        buuzones = zones[zone].buurzones
        print("Req: ", req.id, "zone: ", zone, "buren: ", buuzones)

        if controleOfReqWagenHeeft(req): #Request heeft wagen
            print("Request", req.id ," heeft wagen(s): ", req.verhicleList ,", van: ", req.startTijd, "tot ", req.startTijd+req.duurTijd)

            for index, auto in enumerate(req.verhicleList): #loop door vehiclelist
                print("auto: ", auto)
                if vehicles[auto].isWagenNogBezet() <= req.startTijd:
                    vehicles[auto].wagenAfSlot()

                if not vehicles[auto].wagenBezet: #indien wagen vrij
                    bezetTot = req.startTijd + req.duurTijd
                    vehicles[auto].wagenOpSlot(bezetTot)
                    wagenVrij = vehicles[auto].vehicle

                    print("Gevonden wagen: ", wagenVrij, "staat in zone: ", vehicles[wagenVrij].zone)

                    if vehicles[wagenVrij].zone == None:  # als voertuig nog geen zone heeft
                        print("Voertuig heeft nog geen zone")
                        vehicles[wagenVrij].vehicleToZone(req)  # wijs to aan eigen zone
                        req.reqToVehicle(wagenVrij)  # request krijgt dat voertuig
                        break
                    # check voertuig in eigen zone staat
                    elif vehicles[wagenVrij].zone == zone:
                        print("Voertuig in eigen zone")
                        # voertuig zone moet niet aangepast worden
                        req.reqToVehicle(wagenVrij)  # request krijgt dat voertuig
                        break
                    else:  # check of voertuig in buurzones staat
                        for buur in buuzones:
                            if vehicles[wagenVrij].zone == buur:
                                print("Wagen staat in buurzone", buur)
                                req.reqToVehicle(wagenVrij)  # request krijgt dat voertuig
                                break
                            else:
                                print("Wagen staat NIET in buurzone", buur)
                                # ga verder in lijst van wagens als er nog wagens zijn

                else:
                    print("WAGEN", vehicles[auto].vehicle,"BEZET TOT: ", vehicles[auto].bezetTot)

                if index == len(req.verhicleList):
                    print("EINDE LIJST")

        else:
            print("ERROR: Request heeft geen lijst met wagen(s).")
        print("\n")

    return [requests, zones, vehicles, aantalDagen]


"""Controleert of een request een lijst van wagens heeft, indien niet fout opvangen"""
def controleOfReqWagenHeeft(req):
    if not len(req.verhicleList) == 0:
        return True
    else:
        return False #request heeft geen wagen
