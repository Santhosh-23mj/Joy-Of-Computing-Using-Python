#!/usr/bin/python3
"""
A panagram is a sentence containing every 26 letters in the English alphabet. Given a string S, check if it is panagram or not.

Input Format:
The first line contains the sentence S.

Output Format:
Print 'YES' or 'NO' accordingly

Example:

Input:
The quick brown fox jumps over the lazy dog

Output:
YES
"""
import string
S = input()
S = S.lower()
S = S.replace(" ","")
S = list(S)
S.sort()
ls = []
for i in range(len(S)):
    if ( S[i] not in ls ):
        ls.append(S[i])
temp = list(string.ascii_lowercase)
if ( ls == temp ):
    print("YES")
else:
    print("NO")