import sys
input = sys.stdin.readline
arr = input().strip()
result = set()
for s in range(len(arr)):
    for e in range(s, len(arr)):
        result.add(arr[s:e+1])
print(len(result))