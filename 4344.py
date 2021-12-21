import sys
C = int(sys.stdin.readline())
for _ in range(C):
    case = list(map(int, sys.stdin.readline().split(' ')))
    mean = sum(case[1:])/case[0]
    num = 0
    for c in range(1, len(case)):
        if case[c] > mean:
            num += 1
    print("{:.3f}%".format((num / case[0])*100))
