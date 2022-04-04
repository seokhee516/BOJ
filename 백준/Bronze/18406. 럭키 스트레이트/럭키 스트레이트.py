import sys
input = sys.stdin.readline
n = input().strip()
s = int(len(n)/2)
if sum(list(map(int,n[:s]))) == sum(list(map(int,n[s:]))):
    print("LUCKY")
else:
    print("READY")