import re
print(max(map(int,re.findall(r'[0-9]+',input()))),end="")