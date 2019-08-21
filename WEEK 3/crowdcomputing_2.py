#!/usr/bin/python3

"""
Using Matplot for plotting the values in a graph

plot() - takes three args
    1. list as y-axes
    2. list as x-axes
    3. type of plotting(red dot (ro) ,blue square (bs) ,green triangle (g^) ,red dashes (r--))
"""

import matplotlib.pyplot as plt
import statistics

Estimates = [1638,1423,1720,454,1494,579,585,929,1300,809,909,169,784,782,866,1873,310,607,1323,885,853,545,1822,424,64,1218,1571,1844,1906,846,512,1101,1826,1789,1555,876,1925,1697,1805,1224,62,270,950,846,1053,1816,719,920,1981,1599,1805,390,1701,1627,814,1766,844,1942,1166,306,344,1678,964,169,1024,518,602,948,214,407,172,276,234,679,680]

trim_value = int(len(Estimates)*0.1)
Estimates = Estimates[trim_value:]
Estimates = Estimates[:len(Estimates)-trim_value]

# Filling y axes with contant values

yaxes = []
for i in range(len(Estimates)):
    yaxes.append(5)

# Plotting Values using list
plt.plot(Estimates,yaxes,'r--')

# plotting trimmed mean
plt.plot(statistics.mean(Estimates),5,'g^')

# plotting median
plt.plot(statistics.median(Estimates),5,'ro')