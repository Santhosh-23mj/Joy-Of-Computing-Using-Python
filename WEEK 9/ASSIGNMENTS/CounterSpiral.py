"""
Input Format:
The first line of the input contains an integer number n which represents the number of rows and columns in the matrix.
From the second line contains n rows with each row having n elements separated by a space.

Output Format:
Print the elements in a single line with each element separated by a space

Example:

Input:
4
25 1 29 7
24 20 4 32
16 38 29 1
48 25 21 19

Output:
25 24 16 48 25 21 19 1 32 7 29 1 20 38 29 4

Explanation: 
In the above example, each row, first all the elements of the first column is printed which are 25 24 16 48 after that, remaining elements of the last row is printed which are 25 21 and 19.
After which the remaining elements of the last column is printed which are 1 32 and 7 and so on... 
"""

n=int(input());
a=[];
for i in range(n):
  a.append(list(map(int,input().split())));
di='d';
l,r,u,d=0,n-1,0,n-1
s=[];
while(True):
  if(di=='d'):
    if(u>d):
      break;
    for i in range(u,d+1):
      s.append(a[i][l]);
    l=l+1;
    di='r';
  elif(di=='r'):
    if(l>r):
      break;
    for i in range(l,r+1):
      s.append(a[d][i]);
    d=d-1;
    di='u';
  elif(di=='u'):
    if(u>d):
      break;
    for i in range(d,u-1,-1):
      s.append(a[i][r]);
    r=r-1;
    di='l';
  else:
    if(l>r):
      break;
    for i in range(r,l-1,-1):
      s.append(a[u][i]);
    di='d';
    u=u+1;
print(' '.join(map(str,s)),end='');
