#!/usr/bin/python3

sum = 0
lim = int(input("Enter until what number you need to sum  "))
for i in range(lim+1):
    sum += i
print("The sum until",lim,"numbers is ",sum)

