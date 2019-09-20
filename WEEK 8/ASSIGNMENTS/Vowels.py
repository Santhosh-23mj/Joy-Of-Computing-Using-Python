#!/usr/bin/python3
"""
Given a string S of lowercase letters, remove consecutive vowels from S. After removing, the order of the list should be maintained.

Input Format:
Sentence S in a single line

Output Format:
Print S after removing consecutive vowels

Example:
Input:
your article is in queue

Output:
yor article is in qu

Explanation:
In the first word, 'o' and 'u' are appearing together, hence the second letter 'u' is removed. In the fifth word, 'u', 'e', 'u' and 'e' are appearing together, hence 'e', 'u', 'e' are removed. 
"""
"""
a = "queue"
a = list(a)

vowels = ['a','e','i','o','u']
for j in range(len(a)):
    for i in range(len(vowels)):
        try:
            ind = a.index(vowels[i])
            if ( a[ind+1] in vowels ):
                del(a[ind+1])
        except:
            pass
for i in range(len(a)):
    print(a[i],end="")
failed in private testcase
"""

vowels = 'aeiou'
s=input();
i=0;
n=len(s);
while(i<n):
  print(s[i],end='');
  if(s[i] in vowels):
    while(i<n and s[i] in vowels):
      i+=1;
    continue;
  i+=1;