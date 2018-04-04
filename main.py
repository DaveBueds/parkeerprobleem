#!/usr/bin/env python
# coding=utf-8

import sys, optparse, multiprocessing, time

from csv_read import readCSV
from csv_write import writeCSV
from initOplossing import initOplossing
from localSearch import localSearch

from Request import Request
from Zone import Zone
from Vehicle import Vehicle



def main(argv):
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
    startOpl = initOplossing(obj)

    print("\n" + "Optimaliseren")
    print("-------------------------", "\n")
    localSearch(startOpl, 60, 300)

    print("\n" + "Schrijven naar csv")
    filenaamWrite = outputfile
    print("-------------------------", "\n")
    writeCSV(filenaamWrite, obj)



    """
    # Start localsearch als proces
    p = multiprocessing.Process(target=localSearch, name="LocalSearch", args=(obj, 10,))
    p.start()

    # Wait a maximum of x seconds for localsearch
    # Usage: join([timeout in seconds])
    p.join(10)

    # Controle indien thread al uit zichzelf is gestopt
    if p.is_alive():
        # Terminate localseach
        p.terminate()
        p.join()

    """


if __name__ == "__main__":
    main(sys.argv[1:])

