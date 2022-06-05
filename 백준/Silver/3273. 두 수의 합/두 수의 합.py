import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
x = int(input())
result = 0
if n > 1:
    arr.sort()
    for i in range(n-1, 0, -1):
        if arr[i] < x:
            k = i
            break
    for i in range(k):
        for j in range(k, i, -1):
            if arr[i] + arr[j] == x:
                result += 1
                k = j-1
                break

print(result)