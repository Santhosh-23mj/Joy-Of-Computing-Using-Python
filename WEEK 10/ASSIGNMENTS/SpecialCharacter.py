#!/usr/bin/python3

"""
Given a string S, check whether it contains any special character or not. Print 'YES' if it does else 'NO'.

Input Format:

The first line contains the string S

Output Format:

Print 'YES' or 'NO'

Example:

Input:
Hi$my*name

Output:
YES
"""

ques = input()
ques = ques.replace(" ","")

c = ques.isalnum()
if (c):
    print('NO',end="")
else:
    print('YES',end="")
