#!/usr/bin/env python
# coding=utf-8

import sys, optparse


from CSV_read import readCSV
from CSV_write import writeCSV

from initOplossing import initOplossing

from Request import Request
from Zone import Zone
from Vehicle import Vehicle



def main(argv):
    #print('ARGV:', sys.argv[1:])
    parser = optparse.OptionParser(
        "usage: %prog -i <input_file> -o <solution_file> [-t <time_limit>] [-r <random_seeds>] [-n <num_threads>]")

    parser.add_option("-i", "--input_file", dest="input",
                      default="", type="string",
                      help="[REQUIRED] pad naar het inputbestand")

    parser.add_option("-o", "--solution_file", dest="outputfile",
                      default="", type="string",
                      help="[REQUIRED] pad naar de plaats waar je algoritme de oplossing wegschrijft")

    parser.add_option("-t", "--time_limit", dest="timelimit",
                      default=60, type="int",
                      help="[OPTIONAL] tijd waarna je algoritme moet stoppen, uitgedrukt in seconden, default=60s")
    parser.add_option("-r", "--random_seed", dest="randomseeds",
                      default=100, type="int",
                      help="[OPTIONAL] random seed waarde, default=100")
    parser.add_option("-n", "--num_threads", dest="numthreads",
                      default=1, type="int",
                      help="[OPTIONAL] het maximum aantal threads dat je algoritme mag gebruiken, default=1")

    (options, args) = parser.parse_args()

    inputfile = options.input
    outputfile = options.outputfile
    timelimit = options.timelimit
    randomseeds = options.randomseeds
    numthreads = options.numthreads

    if not inputfile:
        parser.error("input_file REQUIRED")
    if not outputfile:
        parser.error("solution_file REQUIRED")

    print('Input file is: ', inputfile)
    print('Output file is: ', outputfile)
    print('Time limit is: ', timelimit)
    print('Random seeds is: ', randomseeds)
    print('Number of threads is: ', numthreads)


    print("\nWelkom op het Cambio parkeer optimalisatie algoritme")
    print("We beginnen met het inlezen van de csv file, gelieve deze in dezelfde folder te plaatsen als het main script")

    print("filenaam: ", inputfile)
    print("-------------------------", "\n")

    obj = readCSV(inputfile)
    print("-------------------------", "\n")

    print("\n" + "Initieële oplossing aan het bepalen")
    print("-------------------------", "\n")
    initOplossing(obj)

    print("\n" + "Schrijven naar csv")
    filenaamWrite = outputfile
    print("-------------------------", "\n")
    writeCSV(filenaamWrite, obj)

    print("\n" + "Optimaliseren")
    print("-------------------------", "\n")
    """
    requests = obj[0]
    zones = obj[1]
    vehicles = obj[2]
    print("Vehicle assignments:")
    for veh in vehicles:
        auto = veh.getVehicleToZone()
        print("car", auto[0], ";z:", auto[1])

    print("\nVehicle assignments:")
    for req in requests:
        rv = req.getReqToVehicle()
        print("r", rv[0], ";v:", rv[1])
    """


if __name__ == "__main__":
    main(sys.argv[1:])

