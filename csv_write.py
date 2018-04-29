from Request import Request
from Zone import Zone
from Vehicle import Vehicle

from kostfunctie import kostfunctie


unassignedRequests = []

def writeCSV(filenaam, obj):
    requests = obj[0]
    zones = obj[1]
    vehicles = obj[2]

    #SCHRIJVEN van de csv file
    fw = open(filenaam, "r+")

    kost = str(kostfunctie(requests, vehicles))
    koststring = str(kost) + "\n"
    fw.writelines(koststring)

    fw.write("=+Vehicle assignments\n")
    #sorteren op voertuig oplopend
    for veh in vehicles:
        if veh.zone == None:
            #unassignedRequests.append(veh.vehicle)
            # Niet toegewezen voertuigen aan random zone toewijzen-> anders werkt validator niet
            # number of vehicle assignments does not match the number of vehicles in input

            #vehicle aan random zone toewijzen (hier zone 0)
            veh.zone = 0
            vzstring = "car"+str(veh.vehicle)+";z"+str(veh.zone)+"\n"
            fw.write(vzstring)
            continue
        else:
            vzstring = "car"+str(veh.vehicle)+";z"+str(veh.zone)+"\n"
            #print(vzstring)
            fw.write(vzstring)


    fw.write("+Assigned requests\n")

    # sorteren van requests op req.id oplopend
    #requests.sort(key=lambda x: x.id, reverse=False)

    for req in requests:
        rv = req.getReqToVehicle()
        #print("rv: ", rv)
        #controleren req in unassigned bij vehicle to zone
        if rv[0] in unassignedRequests:
            continue
        elif rv[1] == None:
            unassignedRequests.append(rv[0])
            continue #Anders schrijf je vorig voertuig 2x
        else:
            rvstring = "req"+str(rv[0])+";car"+str(rv[1])+"\n"
        fw.write(rvstring)

    fw.write("+Unassigned requests\n")
    for uv in unassignedRequests:
        fw.write("req"+str(uv)+"\n")
    fw.close()








