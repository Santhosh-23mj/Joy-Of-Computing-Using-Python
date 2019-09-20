#!/usr/bin/python3
"""
This program simulates gambling
It calculates the net profit and net loss
It is revealed that we get more loss rather than
profit
"""

from random import randint
import matplotlib.pyplot as plt

win = loss = money = 0
x = [] 
y = []
year = 365

for i in range(1,year+1):
    x.append(i)
    # randomizing picks
    my_bet  = randint(1,10)
    win_lot = randint(1,10)
    
    if ( my_bet == win_lot ):
        win += 1
        money += 900 - 100
    else:
        loss  += 1
        money -= 100
    y.append(money)
print("At the end of 1 year of gambling you have : ",money)
print("The maximum money you had : ",max(y),"at :",y.index(max(y)))
print("The minimum money you had : ",min(y),"at :",y.index(min(y)))
plt.plot(x,y,'r--ss')
plt.plot(y.index(max(y)),max(y),'g^')
plt.plot(y.index(min(y)),min(y),'g^')
plt.show()