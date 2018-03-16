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
        print("Reqloop: ", req.printReq())
        if controleOfReqWagenHeeft(req):
            #Request heeft wagen
            print("Request heeft wagen")
            controleWagenBezet(req, vehicles)

        else:
            print("ERROR: Request heeft geen wagen.")
        print ("\n")


def controleOfReqWagenHeeft(req):
    if not len(req.verhicleList) == 0:
        return True
    else:
        #request heeft geen wagen
        return False

def controleWagenBezet(req, vehicles):
    print("Controle slot wagen vrij")
    for index, auto in enumerate(req.verhicleList):
        print(index, auto)
        #als wagen op slot
        if not vehicles[auto].wagenBezet: #wagen is niet bezet
            print("Wagen is vrij")
            vehicles[auto].wagenOpSlot()
        else:
            print("Wagen is niet vrij")