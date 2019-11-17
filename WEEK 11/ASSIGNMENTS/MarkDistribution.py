#!/usr/bin/python3

"""
Given a list A of n elements, representing the marks. There are m students and you have to distribute the marks from the list A to m students such that:

1) Each student gets marks.
2) The difference between the maximum marks and minimum marks given to the students is minimised.

Input Format:
The first line contains the value n and m respectively separated by a space.
The second line contains the elements of list A separated by a space

Output Format:
Print the minimum difference

Example:

Input:
7 3
7 3 2 4 8 12 56

Output:
2

Explanation:
We need to pick 3 marks for three students (m=3). If we pick 2, 3 and 4, the difference is minimum which is 2. 
"""

n,m=map(int,input().split())
s=sorted(list(map(int,input().split())))
mini=s[-1]-s[0]
for i in range(n-m+1)
  if(s[i+m-1]-s[i]<mini)
    mini=s[i+m-1]-s[i]
print(mini,end="")
