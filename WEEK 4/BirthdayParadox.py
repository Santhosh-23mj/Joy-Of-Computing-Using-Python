#!/usr/bin/python3

"""
Birthday paradox is in which a sample of nearly 30 - 40 people may have 
same dd/mm of their birthday 
it is a paradox because if we take 8 people atleast two will be born on 
same day (mon,tue..) then we should have needed atleast of 367 people to 
have their dd/mm to be same but only 30 -40 samples are enough 
That's why it is a paradox

We simulate this using a program.
We used the 'datetime' library to manipulate dates and times 

 datetime.datetime.today() - prints date and time today
         .date.today()     - prints date alone
         .date.today().strftime("%Y") - prints year alone
                                 %B   - prints month alone
                                 %d   - print date
                                 %W   - week number
                                 %w   - day of week(number)
                                 %j   - no.days till date
                                 %A   - day of week(words)
"""

import random
import datetime

dates = [0 for i in range(50)]
i = 0
while ( i < 50 ):
    year  = random.randint(1900,2019)
    month = random.randint(1,12)
    
    #Checking for leap year
    if ( year%4 == 0 and year%100 != 0 or year%400 == 0 ):
        leap = 1
    else:
        leap = 0
    
    if ( leap == 1 and month == 2 ):
        day = random.randint(1,29)
    elif ( leap == 0 and month == 2 ):
        day = random.randint(1,28)
    elif ( month == 7 or month == 8 ):       # July August = 31 days
        day = random.randint(1,31)
    elif ( month%2 == 0 and month < 7 ):     # April june = 30 days
        day = random.randint(1,30)           
    elif ( month%2 != 0 and month < 7 ):     # January March May = 31 days
        day = random.randint(1,31)
    elif ( month%2 == 0 and month > 7 ):     # October December = 31 days
        day = random.randint(1,31)
    else:                                    # September November = 30 days
        day = random.randint(1,30)
    
    date = datetime.date(year,month,day)     # Converting into date format
    day_of_year = date.timetuple().tm_yday   # Calculating day of year 
    dates[i] = day_of_year                   # Can also be done manually
    i += 1

dates.sort()                                 # Sorting to spot the similarity
for i in range(50):
    print(dates[i])
