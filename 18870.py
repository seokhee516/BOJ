import sys
N = int(sys.stdin.readline())
location = list(map(int, sys.stdin.readline().split(' ')))
loc_sor =sorted(set(location))

loc_dict = {}
for i in range(len(loc_sor)):
    loc_dict[loc_sor[i]] = i
for j in location:
    print(loc_dict[j], end = ' ')