import sys
music = [i for i in map(int, sys.stdin.readline().strip().split(' '))]
asc = [1,2,3,4,5,6,7,8]
desc = [8,7,6,5,4,3,2,1]

if music == asc:
    print("ascending")
elif music == desc:
    print("descending")
else:
    print("mixed")