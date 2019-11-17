#!/usr/bin/python3

"""
One day Ajit got a strange feeling of jumping from one point to another. The jumping will be done in one ­dimension only. 
He will start from a point 0 and from there he will perform a lot of jumps. He can only jump in a specific sequence: 
1­jump, 2­jump, 3­jump, 1­jump, 2­jump, 3­jump, 1­jump, and so on. (1­>2­>3­>1­>2­>3­>1.....)

1-­jump means that if Ajit is at the point x, he will jump to the point x+1. 
2­-jumps mean that if Ajit is at the point x, he will jump to the point x+2. 
3­-jumps mean that if Ajit is at the point x, he will jump to the point x+3. 

Before the start Ajit asks you: will he arrive at the point a after some number of jumps?

Input Format:
The first line contains a single number a denoting the point Ajit asks about.

Output Format:
Output "YES" without a quotes if Ajit can arrive at point a or "NO" without quotes 
otherwise.

Example-1:

Input:
0

Output:
YES

Explanation:
He started at point 0
"""

a = int(input())
ls = [0,1,3]

if ( (a % 6) in ls ):
    print('YES',end="")
else:
    print('NO',end="")
