#!/usr/bin/python3

"""
This program shows the usage of
the CSV library
"""

import csv

with open('route.csv','r') as fp:
    reader = csv.reader(fp)
    for value in reader:
        print(value[0])
        print(value[1])
        print(float(value[0])+float(value[1]))
        print()
