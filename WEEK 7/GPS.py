#!/usr/bin/python3

"""
This is a simple program to plot latitude and longitude in google maps 
it uses the gmplot library for making these things 
easier 
"""

from gmplot import gmplot
import csv

gmap = gmplot.GoogleMapPlotter(28.6971,77.3244,17)
gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"

with open('route.csv') as fp:
    reader = csv.reader(fp)
    k = 0
    
    for value in reader:
        lat = float(value[0])
        lon = float(value[1])
        
        if ( k == 0 ):
            gmap.marker(lat,lon,'yellow')
            k = 1
        else:
            gmap.marker(lat,lon,'blue')
            
gmap.marker(lat,lon,'red')

gmap.draw('map.html')
        