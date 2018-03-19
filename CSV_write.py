from Request import Request
from Zone import Zone
from Vehicle import Vehicle

unassignedVehicles = []

def writeCSV(filenaam, obj):
    requests = obj[0]
    zones = obj[1]
    vehicles = obj[2]

    #SCHRIJVEN van de csv file
    fw = open(filenaam, "w")

    fw.write("=+Vehicle assignments\n")
    #sorteren op voertuig oplopend
    for veh in vehicles:
        if veh.zone == None:
            unassignedVehicles.append(veh.vehicle)
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
        if rv[0] in unassignedVehicles:
            continue
        elif rv[1] == None:
            unassignedVehicles.append(rv[0])
            continue #Anders schrijf je vorig voertuig 2x
        else:
            rvstring = "req"+str(rv[0])+";car"+str(rv[1])+"\n"
        fw.write(rvstring)

    fw.write("+Unassigned requests\n")
    for uv in unassignedVehicles:
        fw.write("req"+str(uv)+"\n")

    kostfunctie(requests, vehicles)

    fw.close()

def kostfunctie(requests, vehicles):
    totaleKost = 0

    for index, req in enumerate(requests):
        autoInt = req.toegewezenVoertuig
        print("r:",req.id,"V:",req.toegewezenVoertuig)
        if autoInt == None: #Dan zit hij in unassigned
            print("Req heeft geen toegewezen voertuig")
            # per unassigned request penalty van 100
            totaleKost += req.penalty1

        else:
            auto = vehicles[autoInt].getVehicle()

            if auto.zone == None:
                print("Vehicle heeft geen zone")
                continue

            # als req.zone == veh.zone, geen penalty van 20
            elif auto.zone == req.zone:
                print("Geen penalty")
            else: #anders penalty van 20
                print("Penalty: ", req.penalty2)
                continue

    print("Totale Kost: ", totaleKost)



