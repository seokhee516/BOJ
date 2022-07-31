import sys
input = sys.stdin.readline

n, m = map(int, input().split())

switch = []
for _ in range(n):
    switch.append(list(map(int, input().split())))
i = 0
while i < n:
    lamp = [0] * m
    for j in range(n):
        if i == j:
            continue
        for k in range(switch[j][0]):
            # print(switch[j][k+1])
            lamp[switch[j][k+1]-1] = 1
        # print(lamp)
    if 0 not in lamp:
        print(1)
        break
    i += 1

if i == n:
    print(0)