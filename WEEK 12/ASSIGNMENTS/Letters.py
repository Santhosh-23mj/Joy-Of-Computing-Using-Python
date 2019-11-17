#!/usr/bin/python3

"""
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Input Format:
The first line of the input contains a statement.

Output Format:
Print the number of upper case and lower case respectively separated by a space.

Example:

Input:
Hello world!

Output:
1 9
"""

string = list(input())
upperC = 0
lowerC = 0


for i in string:
  if(i.isalpha()):
    if(i.isupper()):
      upperC += 1
    if(i.islower()):
      lowerC += 1
print(upperC,lowerC,sep=" ",end="")
