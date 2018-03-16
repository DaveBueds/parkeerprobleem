from CSV_read import readCSV
from initOplossing import initOplossing

from Request import Request
from Zone import Zone
from Vehicle import Vehicle



def main():
    print("Welkom op het Cambio parkeer optimalisatie algoritme")
    print("We beginnen met het inlezen van de csv file, gelieve deze in dezelfde folder te plaatsen als het main script")
    #filenaam = input("Geef de filenaam van de csv: ")
    filenaam = "toy1.csv"
    print("filenaam: ", filenaam)
    print("-------------------------", "\n")


    obj = readCSV(filenaam)

    print("-------------------------", "\n")



    print("\n" + "Initieële oplossing aan het bepalen")
    print("-------------------------", "\n")
    initOplossing(obj)


if __name__ == "__main__":
    main()

