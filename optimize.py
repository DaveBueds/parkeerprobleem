import time

from Request import Request
from Zone import Zone
from Vehicle import Vehicle
from kostfunctie import kostfunctie
from random import randint
from initOplossing import controleOfReqWagenHeeft
from copy import deepcopy


def optimize(startOpl, timelimit):
    requests = startOpl[0]
    zones = startOpl[1]
    vehicles = startOpl[2]
    aantalDagen = startOpl[3]

    aantalRequests = len(requests)-1
    print("aantal requests =", aantalRequests)

    print("----OPTIMIZE----\n")

    #while True:
    cur = kostfunctie(requests, vehicles)
    val = cur

    timeout = time.time() + timelimit

    # selecteer random request en geef deze een ander voertuig
    # controleer dan of oplossing feasible is
    count = 0
    while count < 1:
    #while time.time() < timeout: #counter die random volgende requests selecteert en wijzigt
        count = count + 1

        #randomRequest = requests[randint(0, aantalRequests)] #selecteer random request
        randomRequest = requests[4] #req 5
        oldVehicles = deepcopy(vehicles)
        oldRequests = deepcopy(requests)
        oldZones = deepcopy(zones)

        print("Req: ", randomRequest.id)

        # geef deze request een ander voertuig
        print("Random gekozen request is: ", randomRequest.id, ", deze geven we een ander voertuig dan voordien")
        print("_________________________________________________")
        initieleOpl = False


        # sorteer request lijst op tijd (van klein naar groot)
        requests.sort(key=lambda x: x.startTijd, reverse=False)


        # verander voor random request zijn voertuig
        # lus over request zijn vehicle list
        bestcarscore = cur
        for index, auto in enumerate(randomRequest.verhicleList):
            gekozenWagen = vehicles[auto]
            bezetVan = randomRequest.startTijd
            bezetTot = randomRequest.startTijd + randomRequest.duurTijd

            print('auto', gekozenWagen.vehicle)
            gekozenWagen.wagenOpSlot(bezetVan, bezetTot)
            gekozenWagen.vehicleToZone(randomRequest)
            randomRequest.reqToVehicle(gekozenWagen.vehicle)

            # lus voor wagens vrij te maken van vorige requests
            for auto in vehicles:
                #print("auto: ", auto.vehicle, "bezet van: ", auto.bezetVan, "bezet tot: ", auto.bezetTot, "is bezet: ", auto.wagenBezet, "zone", auto.zone)
                if auto.vehicle == gekozenWagen.vehicle:
                    pass
                else:
                    auto.resetVehicle()  # zodat terug kan gereserveerd worden
                print("auto: ", auto.vehicle, "bezet van: ", auto.bezetVan, "bezet tot: ", auto.bezetTot,
                      "is bezet: ", auto.wagenBezet, "zone", auto.zone)

            checkFeasible(requests, zones, vehicles, randomRequest)
            val = kostfunctie(requests,vehicles)
            print("Kost tussendoor:", val)

            # FIXME hier zit iets dubbel :(
            if val >= cur:  # indien score niet beter
                print("------------- SCORE,", val, " NIET BETER DAN", cur, ": RESET ------------")
                # reset alles
            else:
                print("-------------SCORE BETER------------")
                cur = val

            for auto in vehicles:
                print("auto: ", auto.vehicle, "bezet van: ", auto.bezetVan, "bezet tot: ", auto.bezetTot,
                      "is bezet: ", auto.wagenBezet, "zone", auto.zone)
            #break #MOMENTEEL ENKEL VOOR AUTO 2!!


        val = kostfunctie(requests, vehicles)
        print("Valkost: ", val)


        if val >= cur: # indien score niet beter
            print("------------- SCORE,",val," NIET BETER DAN",cur,": RESET ------------")
            #reset alles
            requests = oldRequests
            vehicles = oldVehicles
            zones = oldZones
        else:
            print("-------------SCORE BETER------------")
            cur = val

        for auto in vehicles:
            print("auto: ", auto.vehicle, "bezet van: ", auto.bezetVan, "bezet tot: ", auto.bezetTot,
                  "is bezet: ", auto.wagenBezet, "zone", auto.zone)


    return [requests, zones, vehicles, aantalDagen]



#returned of opl na swap feasible is of niet
#returned true of false
def checkFeasible(requests, zones, vehicles, randomRequest):
    print("-------------Feasible------------")
    # sorteer request lijst op tijd (van klein naar groot)
    requests.sort(key=lambda x: x.startTijd, reverse=False)

    #for req in requests: # loop door requests
    # controlleer alle daarop volgende requests
    for req in requests:
        zone = req.zone
        buuzones = zones[zone].buurzones

        if req.id == randomRequest.id:
            print("gelijk", req.id)
            auto = vehicles[req.toegewezenVoertuig]
            print("auto: ", auto.vehicle, "bezet van: ", auto.bezetVan, "bezet tot: ", auto.bezetTot,
                  "is bezet: ", auto.wagenBezet, "zone", auto.zone)

        else:
            print("else", req.id)

            if controleOfReqWagenHeeft(req):
                print("Request", req.id, " heeft wagen(s): ", req.verhicleList, ", van: ", req.startTijd, "tot ",
                      req.startTijd + req.duurTijd)

                #loop over req zijn vehiclelijst
                for index, auto in enumerate(req.verhicleList):
                    # controleer of conflict met hoe hij gepland stond
                    # check of wagen bezet is in request zijn tijdszone
                    car = vehicles[auto]

                    print("Car",car.vehicle,"bezet van",car.bezetVan,"bezet tot: ", car.bezetTot )
                    reqEinde = req.startTijd+req.duurTijd

                    if car.bezetVan >= reqEinde or car.bezetTot <= req.startTijd:
                        print("Wagen kan gereserveerd worden")
                        print("bezetTot: ", vehicles[auto].bezetTot)
                        bezetVan = req.startTijd
                        bezetTot = req.startTijd + req.duurTijd
                        # vehicles[auto].wagenOpSlot(bezetTot)
                        wagenVrij = vehicles[auto].vehicle

                        print("Gevonden wagen: ", wagenVrij, "staat in zone: ", vehicles[wagenVrij].zone)

                        if vehicles[wagenVrij].zone == None:  # als voertuig nog geen zone heeft
                            print("Voertuig heeft nog geen zone")
                            vehicles[wagenVrij].vehicleToZone(req)  # wijs to aan eigen zone
                            vehicles[auto].wagenOpSlot(bezetVan, bezetTot)
                            req.reqToVehicle(wagenVrij)  # request krijgt dat voertuig
                            break

                        elif vehicles[wagenVrij].zone == zone:  # check voertuig in eigen zone staat
                            print("Voertuig in eigen zone")
                            # voertuig zone moet niet aangepast worden
                            vehicles[auto].wagenOpSlot(bezetVan, bezetTot)
                            req.reqToVehicle(wagenVrij)  # request krijgt dat voertuig
                            break

                        else:  # check of voertuig in buurzones staat
                            for buur in buuzones:
                                if vehicles[wagenVrij].zone == buur:
                                    print("Wagen staat in buurzone", buur)
                                    vehicles[auto].wagenOpSlot(bezetVan, bezetTot)
                                    req.reqToVehicle(wagenVrij)  # request krijgt dat voertuig
                                    break
                                else:
                                    print("Wagen staat NIET in buurzone", buur)
                                    req.reqToVehicle(None)
                                    # ga verder in lijst van wagens als er nog wagens zijn
                            continue
                    else:
                        print("WAGEN", car.vehicle, "BEZET VAN: ", car.bezetVan, "TOT", car.bezetTot)


            else:
                print("ERROR: Request heeft geen lijst met wagen(s).")
        print("\n")