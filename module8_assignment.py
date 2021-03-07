# import csv
# Weight Data for Domestic Cats
path = "/Users/giselagonzalez/desktop/catsM.csv"
file = open(path)
for line in file:
    print(line)
header_list = ["Cat", "Sex", "Bwt", "Hwt"]

import itertools
import operator
# Testing repeat function
for i in itertools.repeat("Cat"): 5
print(i)

# Testing cycle function
for header_list in itertools.cycle(header_list): 5
print(header_list)

# Testing infinite iterator
# for in loop
for a in itertools.count(2, 2):
    if i == 20:
        break
    else:
        print(i, end=" ")

# Testing copy function
# A Set of Hwt
Hwt = {"2", "2", "2.1"}
Hwt2 = Hwt

#adding a new element in the new set
Hwt2.add("2.2")

#removing an element in the new set
Hwt.remove("2.1")