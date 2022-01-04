import sys
N = int(sys.stdin.readline())
cus = {}
for i in range(N):
    age, name = map(str, sys.stdin.readline().strip().split(' '))
    cus[i] = (int(age), name)
cus = sorted(cus.items(), key=lambda x : (x[1][0], x[0]))

for v in cus:
    print(v[1][0], v[1][1])
