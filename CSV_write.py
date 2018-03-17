from Request import Request
from Zone import Zone
from Vehicle import Vehicle

def writeCSV(filenaam, obj):
    requests = obj[0]
    zones = obj[1]
    vehicles = obj[2]

    unassignedVehicles = []

    #SCHRIJVEN van de csv file
    fw = open(filenaam, "w")

    fw.write("+Assigned requests\n")

    # sorteren van requests op req.id oplopend
    requests.sort(key=lambda x: x.id, reverse=False)

    for req in requests:
        rv = req.getReqToVehicle()
        if rv[1] == None:
            unassignedVehicles.append(rv[0])
            continue #Anders schrijf je vorig voertuig 2x
        else:
            rvstring = "req"+str(rv[0])+";car"+str(rv[1])+"\n"
        fw.write(rvstring)

    fw.write("+Unassigned requests\n")
    for uv in unassignedVehicles:
        fw.write("req"+str(uv)+"\n")

    fw.close()