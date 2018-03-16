class Request(object):

    #de data die binnekomt van CSV is van type str --> CASTEN!

    def __init__(self, id, zone, dag, startTijd, duurTijd, vehicleList, penalty1, penalty2):
        self.id = int(id)
        self.zone = int(zone)
        self.dag = int(dag)
        self.startTijd = int(startTijd)
        self.duurTijd = int(duurTijd)
        self.verhicleList = vehicleList
        self.penalty1 = int(penalty1)
        self.penalty2 = int(penalty2)

    def printReq(self):
        print( "id: ", self.id,
               " zone: ",self.zone,
               " dag: ", self.dag,
               " starttijd: ", self.startTijd,
               " duurtijd: ", self.duurTijd,
               " voertuigenlijst: ", self.verhicleList,
               " penalty1: ", self.penalty1,
               " penalty2: ", self.penalty2
               )