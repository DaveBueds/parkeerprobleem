import time

from Request import Request
from Zone import Zone
from Vehicle import Vehicle
from kostfunctie import kostfunctie
from random import randint
from copy import deepcopy



def localSearch(startOpl, tijd, kost):

    requests = startOpl[0]
    zones = startOpl[1]
    vehicles = startOpl[2]

    #genereer een oplossing in de buurt
    print("----Local Search: hill climbing----\n")
    print(kost)

    #KIEZEN EN VERVANGEN ALGORITME
    cur = kostfunctie(requests, vehicles)
    print("Kost: ", cur, "\n")
    aantalAutos = len(vehicles)


    while True:
        cur = kostfunctie(requests, vehicles)
        val = cur
        count = 0


        while val >= cur and count <= 15:
            count = count + 1

            # zet random auto in andere zone
            randomAuto = randint(0, aantalAutos-1)

            #wijzig random auto zijn zone naar (random) buurzone
            auto = vehicles[randomAuto]
            autoZone = auto.zone

            if autoZone == None:
                print("None detect")
                break
            print("auto: ", auto.vehicle, "autozone: ", autoZone, "buurzonelijst: ", zones[autoZone].buurzones)
            buurzonelijst = zones[autoZone].buurzones

            #selecteer buurzone uit lijst
            randomBuurzone = randint(0, len(buurzonelijst)-1)
            swapzone = zones[buurzonelijst[randomBuurzone]]

            print("Buren: ", buurzonelijst, "array: ", randomBuurzone, "swapTo: ", swapzone.id)

            vehicles[randomAuto].swapVehicleToZone(swapzone.id)
            print("auto: ", auto.vehicle, "gaat naar zone: ", swapzone.id)
            print("Auto: ", randomAuto,"Zone: ", zones[auto.zone].id, "buurzone: ", zones[auto.zone].buurzones)


            val = kostfunctie(requests, vehicles)
            print("Valkost: ", val)

            if val > cur: #indien score niet beter
                print("\tScore slechter")
                auto.swapVehicleToZone(autoZone) #auto terug naar oorspronkelijke zone swappen
                print(auto.getVehicleToZone())
            else:
                print("\t\t\tSCORE BETER")

        if count > 15:
            break

    print("Laatste kost: " + str(cur) + "\n")



"""
    print("Vehicle assignments:")
    for veh in vehicles:
        auto = veh.getVehicleToZone()
        print("car", auto[0], ";z:", auto[1])

    print("\nVehicle assignments:")
    for req in requests:
        rv = req.getReqToVehicle()
        print("r", rv[0], ";v:", rv[1])


    for i in range(10000 * tijd):
       print("Tick")
       time.sleep(1)
"""

