from Request import Request
from Zone import Zone
from Vehicle import Vehicle

def kostfunctie(requests, vehicles):
    totaleKost = 0

    for index, req in enumerate(requests):
        autoInt = req.toegewezenVoertuig
        print("r:",req.id,"c:",req.toegewezenVoertuig)
        if autoInt == None: #Dan zit hij in unassigned
            print("\t\t\t\tReq", req.id," heeft geen toegewezen voertuig")
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
                pass
            else: #anders penalty van 20
                print("Penalty: ", req.penalty2)
                totaleKost += req.penalty2
                continue

    print("Totale Kost: ", totaleKost, "\n\n")
    return totaleKost