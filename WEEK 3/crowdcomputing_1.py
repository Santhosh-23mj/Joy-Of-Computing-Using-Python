#!/usr/bin/python3

"""
Crowd computing is just calculating the mean from 
a group of estimates.

calculating exact mean wont give correct answer so use 10% trimmed mean
that is to remove the 10% largest values and 10% smallest values then calculate 
the mean.

In python it can be done using libraries. Both are demonstrated
"""

from statistics import mean
from scipy import stats 

Estimates = [1638,1423,1720,454,1494,579,585,929,1300,809,909,169,784,782,866,1873,310,607,1323,885,853,545,1822,424,64,1218,1571,1844,1906,846,512,1101,1826,1789,1555,876,1925,1697,1805,1224,62,270,950,846,1053,1816,719,920,1981,1599,1805,390,1701,1627,814,1766,844,1942,1166,306,344,1678,964,169,1024,518,602,948,214,407,172,276,234,679,680]

# Using the manual method
# Calculating mean manually

Estimates.sort()
trimmed_value = int(len(Estimates)*0.1)

Estimates = Estimates[trimmed_value:]
Estimates = Estimates[:len(Estimates)-trimmed_value]

add = float(0)
for i in range(len(Estimates)):
    add += Estimates[i]

result = float(add/len(Estimates))
print("RESULT [MANUAL CALC] ",result)

# Using the mean() fom the library statistics

Estimates = [1638,1423,1720,454,1494,579,585,929,1300,809,909,169,784,782,866,1873,310,607,1323,885,853,545,1822,424,64,1218,1571,1844,1906,846,512,1101,1826,1789,1555,876,1925,1697,1805,1224,62,270,950,846,1053,1816,719,920,1981,1599,1805,390,1701,1627,814,1766,844,1942,1166,306,344,1678,964,169,1024,518,602,948,214,407,172,276,234,679,680]

Estimates.sort()
trimmed_value = int(len(Estimates)*0.1)

Estimates = Estimates[trimmed_value:]
Estimates = Estimates[:len(Estimates)-trimmed_value]
 
print("RESULT [MEAN LIB] ",mean(Estimates))

# Using library to calculate even the trimmed mean

Estimates = [1638,1423,1720,454,1494,579,585,929,1300,809,909,169,784,782,866,1873,310,607,1323,885,853,545,1822,424,64,1218,1571,1844,1906,846,512,1101,1826,1789,1555,876,1925,1697,1805,1224,62,270,950,846,1053,1816,719,920,1981,1599,1805,390,1701,1627,814,1766,844,1942,1166,306,344,1678,964,169,1024,518,602,948,214,407,172,276,234,679,680]

Estimates.sort()

m = stats.trim_mean(Estimates,0.1)
print("RESULT [STATS LIB] ",m)