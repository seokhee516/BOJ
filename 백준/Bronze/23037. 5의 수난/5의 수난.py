import sys
input = sys.stdin.readline
num = input().strip()
s = 0
for n in num:
    s += int(n)**5
print(s)
