#!/usr/bin/env python3

import sys

# make sure we received the right number of arguments
if len(sys.argv) < 2:
    print("error, no file name specified")
    print("correct usage: python3 fp.py [filename.txt]")
    sys.exit()

# this function creates an initial tour using nearest neighbor
def neighbor(c):


# this function returns the euclidean distance between a and b
def distance(a, b):

# this function computes the total length of a given tour
def tourLength(t):


# this function performs a 'swap' between vertices a and b
def swap(t, a, b):


# this function contains the 2-opt algorithm that optimizes our tour
def twoOpt(t):


# read input file into an array
inputfile = open(str(sys.argv[1]))
lines = inputfile.readlines()
inputfile.close()

# read all cities and store them in an array
cities = []
for line in lines:
    city = [int(n) for n in line.split()] # 0 is the city identifier, 1 is x, 2 is y
    cities.append(city)

# construct the initial tour
cities = neighbor(cities)

# optimize it with twoOpt
cities = twoOpt(cities)

# output results
outputfile = open(sys.argv[1] + ".tour", 'w')
outputfile.write(str(tourLength(cities)) + '\n')
for city in cities:
    outputfile.write(city[0] + "\n")
outputfile.close()