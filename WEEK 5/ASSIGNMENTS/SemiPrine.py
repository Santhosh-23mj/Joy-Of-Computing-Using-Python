#!/usr/bin/python3
"""
A semiprime number is an integer which can be expressed as a product of two distinct primes. For example 15 = 3*5 is a semiprime number but 9 = 3*3 is not .
Given an integer number N, find whether it can be expressed as a sum of two semi-primes or not (not necessarily distinct).

Input Format:
The first line contains an integer N.

Output Format:
Print 'Yes' if it is possible to represent N as a sum of two semiprimes 'No' otherwise.

Example:

Input:
30

Output:
Yes

Explanation:
N = 30 can be expressed as 15+15 where 15 is a semi-prime number (5
"""

def issemiprime(n):
    #return sum(prime_factors(n).values)==2;
    i,c=2,0;
    while(i<=int(n**0.5)):
        same=0;
        while(not n%i):
            same+=1;
            n=int(n/i);
        i+=1;
        c+=same;
        if(c>2 or same>=2):
            return False;
    if(n>=2):
        c+=1;
    if(c==2):
        return True;
    else:
        return False;

def issumsemiprime(n):
    if(n<=3):
        return False;
    for i in range(2,n):
        if(issemiprime(i) and issemiprime(n-i)):
            return True;
    return False;

n=int(input());
print('Yes' if issumsemiprime(n) else 'No',end="");
